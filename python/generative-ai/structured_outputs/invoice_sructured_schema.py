import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import base64
import json


load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")


client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://ems-mga4iqxk-eastus2.cognitiveservices.azure.com/",
    api_key=api_key,
)

with open("invoice.jpg", "rb") as image_file:
    document_details = base64.b64encode(image_file.read()).decode("utf-8")

tools = [{
    "type": "function",
    "function": {
        "name": "return_invoice_fields",
        "description": "Return only the extracted invoice fields.",
        "parameters": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "invoice_number": {"type": "string"},
                "invoice_date": {"type": "string", "description": "YYYY-MM-DD if possible"},
                "company_name": {"type": "string"},
                "total_due": {"type": "number"}
            },
            "required": ["invoice_number", "invoice_date", "company_name", "total_due"]
        }
    }
}]


messages = [
    {"role": "system", "content": "Extract structured info from invoices accurately and concisely."},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": (
                    "Extract the following and return them via the function call:\n"
                    "- invoice_number (string)\n"
                    "- invoice_date (YYYY-MM-DD if possible)\n"
                    "- company_name (string)\n"
                    "- total_due (number only)\n"
                    "If fields are missing, infer carefully from context."
                ),
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{document_details}"},
            },
        ],
    },
]

result = client.chat.completions.create(
    model="gpt-5-chat",
    messages=messages,
    tools=tools,
    tool_choice={"type": "function", "function": {
        "name": "return_invoice_fields"}},
    temperature=0
)


choice = result.choices[0]
tool_call = choice.message.tool_calls[0]
args = json.loads(tool_call.function.arguments)
print(
    args["invoice_number"],
    args["invoice_date"],
    args["company_name"],
    args["total_due"]
)
