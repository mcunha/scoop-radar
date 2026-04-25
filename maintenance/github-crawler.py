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

def upgrade_cache_entry(repofoldername, entry):
    if 'full_name' not in entry:
        entry['full_name'] = repofoldername.replace('+', '/')
    if 'git_url' not in entry:
        entry['git_url'] = f"git://github.com/{entry['full_name']}.git"
    if 'html_url' not in entry:
        entry['html_url'] = entry.get('url', f"https://github.com/{entry['full_name']}")
    if 'default_branch' not in entry:
        entry['default_branch'] = 'master'
    if 'topics' not in entry:
        entry['topics'] = []
    if 'last_checked' not in entry:
        entry['last_checked'] = '2000-01-01T00:00:00Z'
    return entry

def process_repo(repofoldername, cache_entry, dir_path):
    global abort_flag
    if abort_flag:
        return None

    cache_entry = upgrade_cache_entry(repofoldername, cache_entry)

    if 'ignored_until' in cache_entry:
        ignored_until = datetime.strptime(cache_entry['ignored_until'], '%Y-%m-%dT%H:%M:%SZ')
        if datetime.now() < ignored_until:
            cache_entry['last_checked'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            return repofoldername, cache_entry, False
        else:
            del cache_entry['ignored_until']

    full_name = cache_entry['full_name']
    git_clone_url = cache_entry['git_url']
    default_branch = cache_entry['default_branch']
    
    repo_path = os.path.join(dir_path, 'cache', repofoldername)
    entries = []
    
    is_first_time = cache_entry['last_checked'] == '2000-01-01T00:00:00Z'
    
    if is_first_time:
        topics = cache_entry['topics']
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
                                
            cache_entry['entries'] = entries
            cache_entry['last_checked'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            return repofoldername, cache_entry, True
        else:
            ignored_until = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
            cache_entry['entries'] = []
            cache_entry['ignored_until'] = ignored_until
            cache_entry['last_checked'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            return repofoldername, cache_entry, True

    else:
        # Existing repo update
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
            cache_entry['entries'] = entries
            
        cache_entry['last_checked'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        return repofoldername, cache_entry, True

def main():
    global abort_flag
    MAX_REPOS_TO_PROCESS = 60 # Process 60 repos per hourly slice
    
    try:
        with open(os.path.join(dir_path,'cache.pickle'), "rb") as input_file:
            cache = pickle.load(input_file)
    except (EnvironmentError, EOFError):
        cache = {}
        
    os.makedirs(os.path.join(dir_path, 'cache'), exist_ok=True)

    # 1. SEARCH SLICE (Find new repositories)
    search_page = cache.get('search_page', 1)
    query = 'topic:scoop-bucket OR topic:shovel-bucket OR topic:scoop-apps OR scoop bucket in:name,description OR shovel bucket in:name,description OR scoop apps in:name,description'
    search_url = f'https://api.github.com/search/repositories?q={requests.utils.quote(query)}&per_page=100&page={search_page}'
    
    print(f"[*] Discovery Phase: Fetching search page {search_page}...")
    try:
        response_data = fetchjson(search_url)
        items = response_data.get('items', [])
        if not items:
            print("[*] Reached end of search results. Resetting search page to 1.")
            cache['search_page'] = 1
        else:
            cache['search_page'] = search_page + 1
            for item in items:
                repofoldername = item['full_name'].replace('/', '+')
                if repofoldername not in cache:
                    cache[repofoldername] = {
                        'name': item['name'],
                        'full_name': item['full_name'],
                        'git_url': item['git_url'],
                        'html_url': item['html_url'],
                        'score': float(item['score']),
                        'default_branch': item.get('default_branch', 'master'),
                        'topics': item.get('topics', []),
                        'last_checked': '2000-01-01T00:00:00Z',
                        'entries': []
                    }
                else:
                    # Refresh score and topics if it exists
                    cache[repofoldername]['score'] = float(item['score'])
                    cache[repofoldername]['topics'] = item.get('topics', [])
    except RateLimitExceededException:
        print("[!] Rate limit exceeded during repository search. Skipping search this run.")
        abort_flag = False # Reset abort flag so we can try processing cached ones

    # 2. PROCESSING SLICE (Update existing/new repositories)
    repo_keys = [k for k in cache.keys() if k not in ('search_page', 'last_run')]
    # Ensure they are cleanly upgraded
    for k in repo_keys:
        cache[k] = upgrade_cache_entry(k, cache[k])
        
    # Sort repos by 'last_checked' ascending (oldest checked first)
    repo_keys.sort(key=lambda k: cache[k]['last_checked'])
    
    repos_to_process = repo_keys[:MAX_REPOS_TO_PROCESS]
    print(f"[*] Processing Phase: Updating {len(repos_to_process)} out of {len(repo_keys)} total known repositories...")
    
    updated_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for repofoldername in repos_to_process:
            futures.append(executor.submit(process_repo, repofoldername, cache[repofoldername], dir_path))
            
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

    # Save cache
    try:
        with open(os.path.join(dir_path,'cache.pickle'), "wb") as input_file:
            pickle.dump(cache, input_file)
    except EnvironmentError:
        pass
        
    print(f'[*] Slice complete. {updated_count} repos actually updated their data/files.')

    # 3. GENERATE README (Always generate a fresh README with whatever state the cache is in)
    actual_repos = [cache[repo] for repo in repo_keys if len(cache[repo].get('entries', [])) > 0]
    actual_repos = sorted(actual_repos, key=lambda repo: repo['score'], reverse=True)
    print(f'[*] {len(actual_repos)} valid repositories found.')

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