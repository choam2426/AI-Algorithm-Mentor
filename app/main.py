from src.consts import *
from src.use_github_api import get_commit_by_sha

print(GITHUB_REPOSITORY)

print(GITHUB_TOKEN)

print(OPENAI_KEY)

print(MODEL)

print(COMMIT_SHA)


print(get_commit_by_sha(GITHUB_REPOSITORY, COMMIT_SHA, GITHUB_TOKEN))
