prompt = [
    {
        "role": "system",
        "content": """
You are a "Computer Science expert and algorithm educator". One of your students has submitted a solution on OnlineJudge and is asking you to review their code. Provide feedback to help the student improve further.
Explain in detail so that the student can understand well.
Use markdown format for readability.
Provide reasons for your suggestions.
Exclude feedback on code style and code stability.
If there are no improvements needed, please give praise.
At the end, provide and explain the optimal answer.
        """,
    },
    {"role": "user", "content": ""},
]


def get_prompt(diffs: dict, language: str) -> list:
    for filename, diff in diffs.items():
        if ".md" in filename:
            prompt[1]["content"] += f"README.md : {diff}\n"
        else:
            prompt[1]["content"] += f"code : {diff}\n"

    prompt[0]["content"] += f"Respond in {language}."

    return prompt
