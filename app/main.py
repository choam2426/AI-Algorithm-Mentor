from src.consts import *
from src.use_github_api import get_commit_data

if __name__ == "__main__":
    get_commit_data(GITHUB_REPOSITORY, COMMIT_SHA, GITHUB_TOKEN)
