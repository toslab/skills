# PDF Templates

이 디렉토리는 PDF 문서 생성 시 재사용 가능한 템플릿을 저장합니다.

## 디렉토리 구조

```
templates/
├── forms/                   # PDF 폼 템플릿
│   ├── invoice-template.pdf
│   └── contract-template.pdf
│
├── designs/                 # 디자인 템플릿 (canvas-design 출력)
│   ├── poster-template.pdf
│   └── flyer-template.pdf
│
└── images/                  # 이미지 에셋
    ├── watermarks/         # 워터마크
    └── signatures/         # 서명 이미지
```

## Canvas-Design 통합

Canvas-design에서 생성한 PDF/PNG를 저장:

```bash
# Canvas-design PDF 출력물 복사
cp /workspace/poster-design.pdf designs/
cp /workspace/watermark.png images/watermarks/
```

## 사용 예시

### 1. Canvas PDF를 페이지로 병합

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()

# Templates의 canvas-design PDF 추가
cover = PdfReader('templates/designs/poster-template.pdf')
writer.add_page(cover.pages[0])

# 다른 페이지 추가
# ...

writer.write('final-document.pdf')
```

### 2. 워터마크 추가

```python
from pypdf import PdfReader, PdfWriter

watermark = PdfReader('templates/images/watermarks/watermark.png').pages[0]

reader = PdfReader('document.pdf')
writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)

writer.write('watermarked.pdf')
```
