import json

import requests


def get_commit_data(repository: str, commit_sha: str, token: str) -> dict:
    url = f"https://api.github.com/repos/{repository}/commits/{commit_sha}"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.json",
    }

    response = requests.get(url, headers=headers)
    diffs = {}
    if response.status_code == 200:
        commit_data = response.json()
        files = commit_data["files"]
        for file in files:
            filename = file["filename"]
            diff = file["patch"]
            diffs[filename] = diff
        return diffs
    else:
        raise "github api requests error"


def write_comment_in_commit(repository: str, commit_sha: str, token: str, comment: str) -> None:
    url = f"https://api.github.com/repos/{repository}/commits/{commit_sha}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
    }
    data = {"body": comment}

    response = requests.post(url, headers=headers, data=json.dumps(data))
