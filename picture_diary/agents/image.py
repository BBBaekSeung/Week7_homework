import base64
from io import BytesIO
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image

load_dotenv()


def _image_agent(prompt: str, output_path: str) -> str:
    """프롬프트 -> 이미지 생성"""

    client = OpenAI()

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024",
        n=1
    )

    image_base64 = response.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    Image.open(BytesIO(image_bytes)).verify()

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(image_bytes)

    print(f"[image] 저장 완료: {path}")

    return str(path)


def generate_image(
    prompt: str,
    output_path: str,
    model: str = "dalle"
) -> str:
    """공개 함수"""

    return _image_agent(prompt, output_path)