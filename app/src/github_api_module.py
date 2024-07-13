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
        print(commit_data)
        files = commit_data["files"]
        for file in files:
            filename = file["filename"]
            diff = file["changes"]
            diffs[filename] = diff
        return diffs
    else:
        raise "github api requests error"
