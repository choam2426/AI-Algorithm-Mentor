import openai

from .prompt import get_prompt


def get_code_review_by_openai(api_key: str, file_contents: dict):
    client = openai.OpenAI(
        api_key=api_key,
    )
    prompt = get_prompt(file_contents)
    completion = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0,
        messages=prompt,
    )
    response = completion.choices[0].message.content
    return response
