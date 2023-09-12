import openai
from typing import Dict


def get_response(api_key: str,
                 content: str,
                 model_name="gpt-3.5-turbo") -> Dict[str, str]:
    openai.api_key = api_key

    try:
        chat_completion = openai.ChatCompletion.create(
            model=model_name, messages=[
                {"role": "user",
                 "content": content}])
    except Exception as e:
        return {"response": e,
                "tokens_used": None,
                "model_used": model_name}
    model_used = chat_completion["model"]
    tokens_used = chat_completion["usage"]["total_tokens"]
    responses = {}
    for index, k in enumerate(chat_completion["choices"]):
        responses["Response"+str(index+1)] = k["message"]["content"]
    return {"response": responses,
            "tokens_used": tokens_used,
            "model_used": model_used}
