import os
import time
import requests
import pickle
from git import Repo
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader
import concurrent.futures
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

dir_path = os.path.dirname(os.path.realpath(__file__))

class RateLimitExceededException(Exception):
    pass

abort_flag = False

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

def get_headers():
    headers = {}
    if 'GITHUB_TOKEN' in os.environ:
        headers['Authorization'] = f"token {os.environ['GITHUB_TOKEN']}"
    return headers

def make_request(url, headers):
    global abort_flag
    while True:
        if abort_flag:
            raise RateLimitExceededException("Aborted by another thread.")
            
        response = session.get(url, headers=headers)
        
        if response.status_code in [403, 429]:
            retry_after = response.headers.get('Retry-After')
            if retry_after:
                wait_time = int(retry_after)
            elif response.headers.get('X-RateLimit-Remaining') == '0':
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time() + 60))
                wait_time = reset_time - int(time.time()) + 1
            else:
                # Secondary rate limit or abuse detection without explicit headers
                wait_time = 60
                
            if wait_time > 0:
                if wait_time > 900: # Abort if wait is > 15 minutes to save CI minutes
                    print(f"[!] Rate limit reached. Required wait time {wait_time}s is too long. Aborting gracefully.")
                    abort_flag = True
                    raise RateLimitExceededException()
                
                print(f"[!] Rate limited (Status {response.status_code}). Waiting {wait_time}s before retrying...")
                time.sleep(wait_time)
                continue
                
        return response

def fetchjson(urlstr):
    response = make_request(urlstr, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return {}

def is_manifest(path):
    return path.endswith('.json') or path.endswith('.yaml') or path.endswith('.yml')

def process_repo(repo_data, last_run, dir_path, existing_cache_entry):
    global abort_flag
    if abort_flag:
        return None

    name = repo_data['name']
    full_name = repo_data['full_name']
    repofoldername = full_name.replace('/','+')
    
    if existing_cache_entry and 'ignored_until' in existing_cache_entry:
        ignored_until = datetime.strptime(existing_cache_entry['ignored_until'], '%Y-%m-%dT%H:%M:%SZ')
        if datetime.now() < ignored_until:
            return repofoldername, existing_cache_entry, False
        else:
            existing_cache_entry = None

    git_clone_url = repo_data['git_url']
    html_url = repo_data['html_url']
    repo_score = repo_data['score']
    last_updated = datetime.strptime(repo_data['updated_at'],'%Y-%m-%dT%H:%M:%SZ')
    default_branch = repo_data.get('default_branch', 'master')
    
    repo_path = os.path.join(dir_path, 'cache', repofoldername)
    entries = []
    
    if not existing_cache_entry:
        topics = repo_data.get('topics', [])
        is_official = 'scoop-bucket' in topics or 'shovel-bucket' in topics or 'scoop-apps' in topics
        
        looks_like_bucket = is_official
        
        if not is_official:
            try:
                tree_url = f"https://api.github.com/repos/{full_name}/git/trees/{default_branch}"
                resp = make_request(tree_url, headers=get_headers())
                if resp.status_code == 200:
                    tree_data = resp.json().get('tree', [])
                    for item in tree_data:
                        if (item['path'] == 'bucket' and item['type'] == 'tree') or is_manifest(item['path']):
                            looks_like_bucket = True
                            break
            except RateLimitExceededException:
                # Let the exception bubble up to the main executor thread
                raise
        
        if looks_like_bucket:
            if abort_flag: return None
            try:
                Repo.clone_from(git_clone_url, repo_path, depth=1)
            except Exception:
                pass
            
            if os.path.isdir(repo_path):
                for d in [repo_path, os.path.join(repo_path, 'bucket')]:
                    if os.path.isdir(d):
                        for f in os.listdir(d):
                            file_path = os.path.join(d, f)
                            if os.path.isfile(file_path) and is_manifest(f):
                                entries.append(os.path.splitext(f)[0])
                                
            return repofoldername, {'name': name, 'url': html_url, 'score': float(repo_score), 'entries': entries}, True
        else:
            ignored_until = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
            return repofoldername, {'name': name, 'url': html_url, 'score': float(repo_score), 'entries': [], 'ignored_until': ignored_until}, True

    else:
        if last_updated > last_run:
            if abort_flag: return None
            if os.path.isdir(repo_path):
                try:
                    repo = Repo(repo_path)
                    o = repo.remotes.origin
                    o.pull(depth=1)
                except Exception:
                    pass
            else:
                try:
                    Repo.clone_from(git_clone_url, repo_path, depth=1)
                except Exception:
                    pass
            
            if os.path.isdir(repo_path):
                for d in [repo_path, os.path.join(repo_path, 'bucket')]:
                    if os.path.isdir(d):
                        for f in os.listdir(d):
                            file_path = os.path.join(d, f)
                            if os.path.isfile(file_path) and is_manifest(f):
                                entries.append(os.path.splitext(f)[0])
                existing_cache_entry['entries'] = entries
            existing_cache_entry['score'] = float(repo_score)
            return repofoldername, existing_cache_entry, True
        else:
            existing_cache_entry['score'] = float(repo_score)
            return repofoldername, existing_cache_entry, False

def main():
    global abort_flag
    try:
        with open(os.path.join(dir_path,'cache.pickle'), "rb") as input_file:
            cache = pickle.load(input_file)
    except (EnvironmentError, EOFError):
        cache = {}
        cache['last_run'] = datetime(2000, 1, 1).strftime('%Y-%m-%dT%H:%M:%SZ')

    last_run = datetime.strptime(cache.get('last_run', '2000-01-01T00:00:00Z'), '%Y-%m-%dT%H:%M:%SZ')
    
    os.makedirs(os.path.join(dir_path, 'cache'), exist_ok=True)

    query = 'topic:scoop-bucket OR topic:shovel-bucket OR topic:scoop-apps OR scoop bucket in:name,description OR shovel bucket in:name,description OR scoop apps in:name,description'
    base_search_url = f'https://api.github.com/search/repositories?q={requests.utils.quote(query)}&per_page=100'
    
    repos_data = []
    page = 1
    try:
        while True:
            search_url = f"{base_search_url}&page={page}"
            print(f"Fetching search page {page}...")
            response_data = fetchjson(search_url)
            items = response_data.get('items', [])
            if not items:
                break
            repos_data.extend(items)
            if len(items) < 100:
                break
            page += 1
    except RateLimitExceededException:
        print("[!] Rate limit exceeded during repository search. Proceeding with currently fetched repos.")
    
    updated_count = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for repo_data in repos_data:
            repofoldername = repo_data['full_name'].replace('/', '+')
            existing_entry = cache.get(repofoldername)
            futures.append(executor.submit(process_repo, repo_data, last_run, dir_path, existing_entry))
            
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if result:
                    repofoldername, entry, updated = result
                    cache[repofoldername] = entry
                    if updated:
                        updated_count += 1
            except RateLimitExceededException:
                print("[!] Rate limit exception caught in thread. Shutting down pool cleanly...")
                abort_flag = True

    if not abort_flag:
        cache['last_run'] = datetime.strftime(datetime.now().replace(hour=0, minute=0, second=0),'%Y-%m-%dT%H:%M:%SZ')

    try:
        with open(os.path.join(dir_path,'cache.pickle'), "wb") as input_file:
            pickle.dump(cache, input_file)
    except EnvironmentError:
        pass
        
    print(f'{updated_count} repos updated')

    repos = [repo for repo in cache.keys() if repo != 'last_run']
    actual_repos = [repo for repo in repos if len(cache[repo].get('entries', [])) > 0]
    actual_repos = sorted(actual_repos, key=lambda repo: cache[repo]['score'], reverse=True)
    print(f'{len(actual_repos)} valid repositories found.')

    TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(dir_path, 'template')),
        trim_blocks=False)
    
    context = {
        'sortedrepos': actual_repos,
        'cache': cache
    }
    
    markdown_content = TEMPLATE_ENVIRONMENT.get_template('ReadmeTemplate.tpl').render(context)
    with open(os.path.join(dir_path,'..','README.md'), "w", encoding='utf-8') as readme_file:
        readme_file.write(markdown_content)

    print('[INFO] Script Finished...')

if __name__ == '__main__':
    main()