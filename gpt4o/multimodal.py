
import os
import base64
from openai import AzureOpenAI
from prompts import SAFETY_SYSTEM_MESSAGE, SYSTEM_PROMPT

endpoint = os.environ["ENDPOINT_URL"]
deployment = os.environ["AOAI_DEPLOYMENT_NAME"]
subscription_key = os.environ["AZURE_OPENAI_API_KEY"]

# Initialize Azure OpenAI Service client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

IMAGE_PATH = os.path.join(os.getcwd(), os.environ["IMAGE_EXAMPLE_PATH"])
encoded_image = base64.b64encode(
    open(IMAGE_PATH, 'rb').read()).decode('ascii')

# Prepare the chat prompt
messages = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": f"""{SYSTEM_PROMPT}"""
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Here's the image i want you to generate a prompt for :\n"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                }
            }
        ]
    }
]

# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

result = completion.to_json()
print(result)
