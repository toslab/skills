# DOCX Templates

이 디렉토리는 Word 문서 생성 시 재사용 가능한 템플릿을 저장합니다.

## 디렉토리 구조

```
templates/
├── xml/                      # XML 템플릿 (기존)
│   ├── comments.xml
│   ├── commentsExtended.xml
│   ├── commentsExtensible.xml
│   ├── commentsIds.xml
│   └── people.xml
│
├── images/                   # 이미지 에셋
│   ├── headers/             # 헤더 이미지 (canvas-design 출력 가능)
│   ├── footers/             # 푸터 이미지
│   ├── logos/               # 로고
│   └── backgrounds/         # 배경/워터마크
│
└── pdf/                     # PDF 템플릿
    ├── letterheads/         # 레터헤드 템플릿
    └── certificates/        # 인증서 템플릿
```

## Canvas-Design 통합

Canvas-design에서 생성한 PNG/PDF를 여기에 저장하고 재사용:

```bash
# Canvas-design 출력물 복사
cp /workspace/header-design.png images/headers/
cp /workspace/letterhead.pdf pdf/letterheads/
```

## 사용 예시

```python
from docx import Document
from docx.shared import Inches

doc = Document()

# Templates에서 헤더 이미지 추가
doc.add_picture('templates/images/headers/header-design.png', width=Inches(6))

doc.save('output.docx')
```
