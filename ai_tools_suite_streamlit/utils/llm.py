import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

def get_llm_response(prompt):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "⚠ OPENAI_API_KEY not found in .env file."

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content