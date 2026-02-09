from openai import AzureOpenAI
import os
from dotenv import load_dotenv


load_dotenv(override=True)

openai_key = os.getenv("OPENAI_FOUR_ONE_KEY")
azure_endpoint = os.getenv("AZURE_FOUR_ONE_ENDPOINT")
deployment = "gpt-4.1"
search_url = ""
search_key = ""


client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=azure_endpoint,
    api_key=openai_key
)

# Additional parameters to apply RAG pattern using the AI Search index
rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": search_url,
                "index_name": "index_name",
                "authentication": {
                    "type": "api_key",
                    "key": search_key,
                }
            }
        }
    ],
}

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What are decision trees?"
        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model=deployment,
    extra_body=rag_params
)

print(response.choices[0].message.content)
