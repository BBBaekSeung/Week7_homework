# Picture Diary

## 프로젝트 소개

일기 내용을 입력하면 장면을 추출하고 이미지를 생성하는 그림 일기 프로젝트입니다.

파이프라인은 다음 순서로 동작합니다.

1. 일기 텍스트 입력
2. 장면 추출
3. 이미지 생성
4. 영상 생성(구조 구현)

---

## 빠른 시작

### 1. 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

프로젝트 루트의 `.env` 파일에 OpenAI API 키를 설정합니다.

```env
OPENAI_API_KEY=YOUR_API_KEY
```

### 3. 실행

```bash
python pipeline.py
```

---

## 결과 미리보기

생성 결과는 `outputs/` 폴더에 저장됩니다.

예시 파일

```text
outputs/diary_scene_1.png
outputs/diary_scene_1.mp4
```

---

## 파일 구조

```text
picture_diary/
├── pipeline.py
├── agents/
│   ├── scene.py
│   ├── image.py
│   └── video.py
├── domains/
│   └── product_prompts.json
├── outputs/
├── README.md
├── requirements.txt
└── week7_retrospective.md
```

---

## 도메인 응용

선택 도메인: Product

주요 프롬프트 요소

* close-up
* eye-level
* studio lighting
* 50mm macro lens
* clean professional mood

제품 이미지를 카탈로그 스타일로 생성하도록 구성하였습니다.

---

## 보안 체크리스트

* API 키는 `.env` 파일에 저장
* `.env` 파일은 GitHub에 업로드하지 않음
* API 키 하드코딩 금지
* `.gitignore`에 `.env` 포함 확인
