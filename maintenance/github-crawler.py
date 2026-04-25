import os
import requests
import pickle
from git import Repo
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import concurrent.futures

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_headers():
    headers = {}
    if 'GITHUB_TOKEN' in os.environ:
        headers['Authorization'] = f"token {os.environ['GITHUB_TOKEN']}"
    return headers

def fetchjson(urlstr):
    response = requests.get(url=urlstr, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    return {}

def process_repo(repo_data, last_run, dir_path, existing_cache_entry):
    name = repo_data['name']
    full_name = repo_data['full_name']
    repofoldername = full_name.replace('/','+')
    git_clone_url = repo_data['git_url']
    html_url = repo_data['html_url']
    repo_score = repo_data['score']
    last_updated = datetime.strptime(repo_data['updated_at'],'%Y-%m-%dT%H:%M:%SZ')
    default_branch = repo_data.get('default_branch', 'master')
    
    repo_path = os.path.join(dir_path, 'cache', repofoldername)
    entries = []
    updated = False
    
    if not existing_cache_entry:
        # First time probing: Use Trees API
        tree_url = f"https://api.github.com/repos/{full_name}/git/trees/{default_branch}?recursive=1"
        resp = requests.get(tree_url, headers=get_headers())
        if resp.status_code == 200:
            tree_data = resp.json().get('tree', [])
            for item in tree_data:
                path = item['path']
                if path.endswith('.json'):
                    parts = path.split('/')
                    if len(parts) == 1 or (len(parts) == 2 and parts[0] == 'bucket'):
                        entries.append(os.path.basename(path)[:-5])
        
        return repofoldername, {'name': name, 'url': html_url, 'score': float(repo_score), 'entries': entries}, True

    else:
        # Existing repo
        if last_updated > last_run:
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
                            if os.path.isfile(file_path) and file_path.endswith('.json'):
                                entries.append(os.path.basename(f)[:-5])
                existing_cache_entry['entries'] = entries
            existing_cache_entry['score'] = float(repo_score)
            return repofoldername, existing_cache_entry, True
        else:
            existing_cache_entry['score'] = float(repo_score)
            return repofoldername, existing_cache_entry, False

def main():
    # Load cache
    try:
        with open(os.path.join(dir_path,'cache.pickle'), "rb") as input_file:
            cache = pickle.load(input_file)
    except (EnvironmentError, EOFError):
        cache = {}
        cache['last_run'] = datetime(2000, 1, 1).strftime('%Y-%m-%dT%H:%M:%SZ')

    last_run = datetime.strptime(cache.get('last_run', '2000-01-01T00:00:00Z'), '%Y-%m-%dT%H:%M:%SZ')
    
    os.makedirs(os.path.join(dir_path, 'cache'), exist_ok=True)

    # Fetch repos
    search_url = 'https://api.github.com/search/repositories?q=scoop+buckets&per_page=100'
    repos_data = fetchjson(search_url).get('items', [])
    
    updated_count = 0
    
    # Process concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for repo_data in repos_data:
            repofoldername = repo_data['full_name'].replace('/', '+')
            existing_entry = cache.get(repofoldername)
            futures.append(executor.submit(process_repo, repo_data, last_run, dir_path, existing_entry))
            
        for future in concurrent.futures.as_completed(futures):
            repofoldername, entry, updated = future.result()
            cache[repofoldername] = entry
            if updated:
                updated_count += 1

    # Update last run
    cache['last_run'] = datetime.strftime(datetime.now().replace(hour=0, minute=0, second=0),'%Y-%m-%dT%H:%M:%SZ')

    try:
        with open(os.path.join(dir_path,'cache.pickle'), "wb") as input_file:
            pickle.dump(cache, input_file)
    except EnvironmentError:
        pass
        
    print(f'{updated_count} repos updated')

    # Sort Repos by github score
    repos = [repo for repo in cache.keys() if repo != 'last_run']
    actual_repos = [repo for repo in repos if len(cache[repo].get('entries', [])) > 0]
    actual_repos = sorted(actual_repos, key=lambda repo: cache[repo]['score'], reverse=True)
    print(f'{len(actual_repos)} valid repositories found.')

    # Update Readme file
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