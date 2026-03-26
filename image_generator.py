from openai import OpenAI
import base64
import os
from datetime import datetime

client = OpenAI(api_key="TA_CLE_API")

def generate_image(prompt):
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    filename = f"images/dream_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    with open(filename, "wb") as f:
        f.write(image_bytes)

    return filename