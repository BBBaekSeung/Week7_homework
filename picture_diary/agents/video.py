from pathlib import Path
import requests


def _save_video(video_url: str, output_path: str) -> str:
    """영상 URL -> 로컬 mp4 저장"""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(video_url, timeout=30)
    response.raise_for_status()

    path.write_bytes(response.content)

    print(f"[video] 저장 완료: {path}")

    return str(path)


def generate_video(image_path: str, output_path: str) -> str:
    """이미지 -> 영상 생성 -> 로컬 저장"""

    # 지금은 실제 영상 API 연결 전이라 임시 URL 대신 로컬 저장 구조만 맞춘다.
    # 나중에 fal/kling 결과 video_url이 생기면 _save_video(video_url, output_path)를 호출하면 된다.

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        f"video source image: {image_path}",
        encoding="utf-8"
    )

    print(f"[video] 임시 영상 파일 저장: {path}")

    return str(path)