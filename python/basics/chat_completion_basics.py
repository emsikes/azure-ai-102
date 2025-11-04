from openai import AzureOpenAI
import os
from dotenv import load_dotenv
# import json
import base64

load_dotenv(override=True)

openai_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_ENDPOINT")
deployment = "gpt-5-chat"

with open("sd4.jpeg", "rb") as image_file:
    image_details = base64.b64encode(image_file.read()).decode("utf-8")

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=azure_endpoint,
    api_key=openai_key
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content":
            [
                {
                    "type": "text",
                    "text": "Give me a description of what is in this image, name the location if you know it."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_details}"
                    }
                }
            ]
        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)

# json_response = response.model_dump()

# print(json.dumps(json_response, indent=2))
