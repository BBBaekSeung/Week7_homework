from pathlib import Path

from agents.scene import extract_scenes
from agents.image import generate_image
from agents.video import generate_video


def picture_diary_pipeline(diary_text: str) -> dict:
    """파이프라인: 장면 -> 이미지 -> 영상"""

    print("그림 일기 생성 시작")

    Path("outputs").mkdir(exist_ok=True)

    scenes = extract_scenes(diary_text)

    images = []
    videos = []

    for index, scene in enumerate(scenes, start=1):
        print(f"{index}번째 장면 생성 중")

        image_path = f"outputs/diary_scene_{index}.png"
        video_path = f"outputs/diary_scene_{index}.mp4"

        image_result = generate_image(
            prompt=scene["prompt_en"],
            output_path=image_path,
            model="dalle"
        )

        video_result = generate_video(
            image_path=image_result,
            output_path=video_path
        )

        images.append(image_result)
        videos.append(video_result)

    return {
        "scenes": scenes,
        "images": images,
        "videos": videos
    }


if __name__ == "__main__":
    diary = input("오늘의 일기~ ")

    result = picture_diary_pipeline(diary)

    print(result)