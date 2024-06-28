import requests


def get_commit_by_sha(repository: str, commit_sha: str, token: str) -> str:
    url = f"https://api.github.com/repos/{repository}/commits/{commit_sha}"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.diff",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return ""
