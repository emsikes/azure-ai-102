import os
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://ems-mga4iqxk-eastus2.cognitiveservices.azure.com/",
    api_key=api_key,
)

# Convert invoice to base64 image
with open("invoice.jpg", "rb") as f:
    document_details = base64.b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="gpt-5-chat",
    max_tokens=10000,
    temperature=0.7,
    top_p=1.0,
    messages=[
        {
            "role": "system",
            "content": "Extract structured info from invoices accurately and concisely."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Extract the details from this invoice."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{document_details}"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
