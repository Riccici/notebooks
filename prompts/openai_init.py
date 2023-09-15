import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

MODEL = "gpt-4"


def chat_with_gpt4(messages):
    # 调用 Completion API
    response = openai.ChatCompletion.create(model=MODEL, messages=messages)

    return response.choices[0].message.content
