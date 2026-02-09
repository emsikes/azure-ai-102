from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv(override=True)


endpoint = os.environ.get("AZURE_CONTENT_SAFTEY_ENDPOINT")
key = os.environ.get("AZURE_CONTENT_SAFETY_API_KEY")

client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

with open("IMG_8856.jpeg", "rb") as image_file:
    request = AnalyzeImageOptions(image=ImageData(content=image_file.read()))

response = client.analyze_image(request)
print(response)
