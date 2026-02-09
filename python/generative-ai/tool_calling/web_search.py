from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.responses.create(
    input="What is the latest news in the world of AI?",
    tools=[{"type": "web_search_preview"}],
    model="gpt-5"
)

print(response.output_text)
