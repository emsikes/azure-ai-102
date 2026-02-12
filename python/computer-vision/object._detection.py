from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures

import os
from dotenv import load_dotenv
import json

load_dotenv(override=True)

endpiont = "https://ai-102-cv.cognitiveservices.azure.com/"
api_key = os.getenv("AZURE_VISION_KEY")

client = ImageAnalysisClient(
    endpoint=endpiont, credential=AzureKeyCredential(api_key))

with open("fruits.jpg", "rb") as image_file:
    image_details = image_file.read()

response = client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.OBJECTS]
)

print(json.dumps(response.as_dict(), indent=4))
