import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def clone_repo(repo):
    full_name = repo.get('full_name')
    git_url = repo.get('git_url')
    if not full_name or not git_url:
        return full_name, False, "Missing info"
        
    repo_folder = full_name.replace('/', '+')
    cache_dir = os.path.join('maintenance', 'cache')
    dest_path = os.path.join(cache_dir, repo_folder)
    
    if os.path.exists(dest_path) and os.path.isdir(dest_path):
        return full_name, True, "Already exists"
        
    try:
        # Clone repo with depth 1
        result = subprocess.run(
            ["git", "clone", "--depth", "1", git_url, dest_path],
            capture_output=True,
            text=True,
            check=True
        )
        return full_name, True, "Cloned successfully"
    except subprocess.CalledProcessError as e:
        return full_name, False, f"Git clone failed: {e.stderr.strip()}"
    except Exception as e:
        return full_name, False, f"Error: {e}"

def main():
    with open('all.json', encoding='utf-8') as f:
        data = json.load(f)
        
    repos = data.get('all', [])
    
    cache_dir = os.path.join('maintenance', 'cache')
    os.makedirs(cache_dir, exist_ok=True)
    
    existing_folders = {d for d in os.listdir(cache_dir) if os.path.isdir(os.path.join(cache_dir, d))}
    
    missing_repos = [repo for repo in repos if repo.get('full_name') and repo['full_name'].replace('/', '+') not in existing_folders]
    
    print(f"Found {len(missing_repos)} missing repos to clone. Starting...")
    
    success_count = 0
    fail_count = 0
    
    import time
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {}
        for repo in missing_repos:
            futures[executor.submit(clone_repo, repo)] = repo
            time.sleep(1.0) # Be polite to GitHub
        
        for future in as_completed(futures):
            full_name, success, msg = future.result()
            if success:
                success_count += 1
                print(f"[OK] {full_name}")
            else:
                fail_count += 1
                print(f"[FAIL] {full_name} - {msg}")
                
    print(f"\nFinished. Successfully cloned: {success_count}. Failed: {fail_count}.")

if __name__ == '__main__':
    main()
