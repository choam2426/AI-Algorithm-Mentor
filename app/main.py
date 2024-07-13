from src import *

if __name__ == "__main__":
    diffs = get_commit_data(GITHUB_REPOSITORY, COMMIT_SHA, GITHUB_TOKEN)
    print(diffs)
    llm_response = get_code_review_by_openai(api_key=OPENAI_API_KEY, diffs=diffs)
