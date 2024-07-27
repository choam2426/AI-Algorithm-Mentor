from src import *

if __name__ == "__main__":
    file_contents = get_commit_data(GITHUB_REPOSITORY, COMMIT_SHA, GITHUB_TOKEN)

    llm_response = get_code_review_by_openai(api_key=OPENAI_API_KEY, diffs=file_contents)

    write_comment_in_commit(repository=GITHUB_REPOSITORY, commit_sha=COMMIT_SHA, token=GITHUB_TOKEN, comment=llm_response)
