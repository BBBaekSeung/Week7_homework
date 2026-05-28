def _scene_agent(diary_text: str) -> list[dict]:
    """일기 -> 장면 추출"""

    scene = {
        "scene_kr": diary_text,
        "prompt_en": (
            f"picture diary illustration, warm lighting, cozy mood, "
            f"{diary_text}"
        )
    }

    return [scene]


def extract_scenes(diary_text: str) -> list[dict]:
    """공개 함수"""

    return _scene_agent(diary_text)