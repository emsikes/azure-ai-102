from openai import AzureOpenAI
import os
from dotenv import load_dotenv
import requests


load_dotenv(override=True)

openai_key = os.getenv("DALLE_API_KEY")
dalle_endpoint = os.getenv("DALLE_ENDPOINT")
deployment = "dall-e-3"

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=dalle_endpoint,
    api_key=openai_key
)

response = client.images.generate(
    model=deployment,
    prompt="A house on the West Coast of the US overlooking the Pacific Ocean on a rocky cliff, with waves crashing against it.  Highly detailed, digital art.",
    n=1,
    size="1024x1024",
    quality="standard"
)

image_url = response.data[0].url

# Save file locally

try:
    image_data = requests.get(image_url).content

    with open("coastal_image.png", "wb") as handler:
        handler.write(image_data)

    print("Successfully saved image")
except Exception as e:
    print(f"Caught exception trying to generate and save image: {e}")
