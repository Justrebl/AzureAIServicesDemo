# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=os.environ["ENDPOINT_URL"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

result = client.images.generate(
    model="dall-e-3",  # the name of your DALL-E 3 deployment
    prompt="Create an image of a classic vintage car, reminiscent of a mid-20th-century design, infused with a vibrant and dynamic pop art style. The car should be depicted in bold, vivid colors with striking patterns that include swirling lines and abstract shapes, giving it an energetic and lively appearance. The background should complement the car with splashes of color and paint splatters, enhancing the overall sense of motion and excitement. The setting should be a minimalistic backdrop that allows the car's colors and patterns to stand out prominently. The image should evoke a sense of nostalgia while simultaneously offering a modern, artistic twist, capturing the essence of a retro yet timeless aesthetic.",
    style="vivid",
    quality="hd",
    size="1792x1024",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
revised_prompt = json.loads(result.model_dump_json())[
    'data'][0]['revised_prompt']

# ...existing code...

print(f"Image URL: {image_url}")
print(f"Revised Prompt: {revised_prompt}")
