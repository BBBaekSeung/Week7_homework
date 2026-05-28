# 그림 일기 (Picture Diary)

텍스트로 작성한 일기를 AI가 자동으로 이미지와 영상으로 변환해주는 멀티미디어 일기 생성 파이프라인입니다.

## 개요

사용자가 한국어로 일기를 입력하면, AI 에이전트들이 순차적으로 동작하여 일기의 장면을 추출하고 DALL-E를 통해 일러스트 이미지를 생성한 뒤, 최종적으로 영상 파일로 저장합니다.

```
일기 텍스트 입력
    ↓
장면 추출 (Scene Extraction)
    ↓
이미지 생성 (DALL-E)
    ↓
영상 생성 (Video Generation)
    ↓
outputs/ 폴더에 결과물 저장
```

## 기술 스택

- **Python 3.x**
- **OpenAI API** — DALL-E 이미지 생성 (`gpt-image-1`)
- **Pillow** — 이미지 처리 및 검증
- **requests** — HTTP 클라이언트
- **python-dotenv** — 환경 변수 관리

## 프로젝트 구조

```
picture_diary/
├── agents/
│   ├── scene.py        # 일기 텍스트에서 장면 추출
│   ├── image.py        # DALL-E를 이용한 이미지 생성
│   └── video.py        # 이미지로부터 영상 생성
├── domains/
│   └── product_prompts.json  # 프롬프트 템플릿
├── outputs/            # 생성된 이미지/영상 저장 경로
├── pipeline.py         # 메인 실행 파이프라인
├── requirements.txt
└── .env                # 환경 변수 설정
```

## 설치 및 실행

### 1. 가상환경 생성 및 활성화

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install openai pillow requests python-dotenv
```

### 3. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 OpenAI API 키를 입력합니다.

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. 실행

```bash
python pipeline.py
```

프롬프트가 표시되면 한국어로 일기를 입력합니다.

```
오늘의 일기~ 오늘 날씨가 맑아서 공원을 산책했다.
```

## 출력 결과

실행 후 `outputs/` 폴더에 장면별 파일이 저장됩니다.

```
outputs/
├── diary_scene_1.png
├── diary_scene_1.mp4
├── diary_scene_2.png
└── diary_scene_2.mp4
```

## 에이전트 설명

| 에이전트 | 파일 | 역할 |
|---------|------|------|
| Scene Agent | `agents/scene.py` | 일기 텍스트를 분석하여 장면과 영어 프롬프트 생성 |
| Image Agent | `agents/image.py` | DALL-E API로 1024×1024 PNG 이미지 생성 |
| Video Agent | `agents/video.py` | 생성된 이미지를 기반으로 영상 파일 생성 |

## 주의사항

- `outputs/`, `.env`, 생성된 이미지/영상 파일은 `.gitignore`에 등록되어 있으므로 Git에 커밋되지 않습니다.
- 영상 생성 기능(`video.py`)은 현재 플레이스홀더로 구현되어 있으며, 외부 영상 생성 API 연동 시 완성될 예정입니다.
- OpenAI API 사용량에 따라 비용이 발생할 수 있습니다.
