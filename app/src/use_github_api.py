import requests


def get_commit_data(repository: str, commit_sha: str, token: str) -> str:
    url = f"https://api.github.com/repos/{repository}/commits"

    headers = {
        "Authorization": f"token {token}",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        commits = response.json()
        if commits:
            recent_commit = commits[0]
            print(recent_commit)
    else:
        return ""
