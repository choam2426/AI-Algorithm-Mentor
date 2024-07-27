import json

import requests


def get_commit_data(repository: str, commit_sha: str, token: str) -> dict:
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.json",
    }
    url = f"https://api.github.com/repos/{repository}/commits/{commit_sha}"
    response = requests.get(url, headers=headers)
    file_contents = {}
    commit_data = response.json()
    files = commit_data["files"]
    for file in files:
        filename = file["filename"]
        url = f"https://api.github.com/repos/{repository}/contents/{filename}"
        response = requests.get(url, headers=headers)
        file_contents[filename] = response.text
    return file_contents


def write_comment_in_commit(repository: str, commit_sha: str, token: str, comment: str) -> None:
    url = f"https://api.github.com/repos/{repository}/commits/{commit_sha}/comments"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"body": comment}

    response = requests.post(url, headers=headers, data=json.dumps(data))
