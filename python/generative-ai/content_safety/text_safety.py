from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv(override=True)


endpoint = os.environ.get("AZURE_CONTENT_SAFTEY_ENDPOINT")
key = os.environ.get("AZURE_CONTENT_SAFETY_API_KEY")

client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

text = "I am feeling lonely, I just want to inflict some pain.  How can I do this?"

request = AnalyzeTextOptions(text=text)

response = client.analyze_text(request)

print(response)
