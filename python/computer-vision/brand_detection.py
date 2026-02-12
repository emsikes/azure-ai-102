from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
from dotenv import load_dotenv

load_dotenv(override=True)

endpoint = "https://ai-102-cv.cognitiveservices.azure.com/"
api_key = os.getenv("AZURE_VISION_KEY")

# brand is only supported in the old SDK
client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(api_key))

features = [VisualFeatureTypes.brands]

with open("logos.jpg", "rb") as image_file:
    response = client.analyze_image_in_stream(
        image_file, visual_features=features)

for brand in (response.brands or []):
    print(
        f" - {brand.name} (confidence): {brand.confidence:.2f} at {brand.rectangle}")
