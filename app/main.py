from src import *

if __name__ == "__main__":
    file_contents = get_commit_data(REPOSITORY_NAME, COMMIT_SHA, GITHUB_TOKEN)

    llm_response = get_code_review_by_openai(api_key=OPENAI_API_KEY, file_contents=file_contents)

    write_comment_in_commit(repository=REPOSITORY_NAME, commit_sha=COMMIT_SHA, token=GITHUB_TOKEN, comment=llm_response)
