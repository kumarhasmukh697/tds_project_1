import os
import requests
import subprocess
import json

with open("config.json") as f:
    config = json.load(f)

GITHUB_TOKEN = config["github_token"]
GITHUB_USER = config["github_username"]

def create_and_deploy_repo(task, app_dir):
    repo_name = task.replace(" ", "-")

    # 1️⃣ Create repo via GitHub API
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"name": repo_name, "private": False, "auto_init": False}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 201:
        raise Exception(f"Failed to create repo: {r.text}")

    repo_url = r.json()["html_url"]
    clone_url = r.json()["clone_url"]

    # 2️⃣ Push generated files
    subprocess.run(["git", "init"], cwd=app_dir)
    subprocess.run(["git", "remote", "add", "origin", clone_url], cwd=app_dir)
    subprocess.run(["git", "add", "."], cwd=app_dir)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=app_dir)
    subprocess.run(["git", "branch", "-M", "main"], cwd=app_dir)
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=app_dir)

    # 3️⃣ Enable GitHub Pages
    pages_api = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}/pages"
    pages_data = {"source": {"branch": "main", "path": "/"}}
    requests.post(pages_api, headers=headers, json=pages_data)

    pages_url = f"https://{GITHUB_USER}.github.io/{repo_name}/"

    # 4️⃣ Get commit SHA
    commit_sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=app_dir
    ).decode().strip()

    return repo_url, commit_sha, pages_url
