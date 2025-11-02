# Document-Skills Templates 구조 가이드

## 📁 확장된 Templates 디렉토리 구조

```
document-skills/
│
├── docx/
│   └── scripts/
│       └── templates/
│           ├── xml/                      # 기존 XML 템플릿
│           │   ├── comments.xml
│           │   ├── commentsExtended.xml
│           │   ├── commentsExtensible.xml
│           │   ├── commentsIds.xml
│           │   └── people.xml
│           │
│           ├── images/                   # ✨ 이미지 템플릿 (새로 추가)
│           │   ├── headers/
│           │   │   ├── corporate-header.png
│           │   │   └── minimal-header.png
│           │   ├── footers/
│           │   │   └── company-footer.png
│           │   ├── logos/
│           │   │   ├── logo-color.png
│           │   │   └── logo-mono.png
│           │   └── backgrounds/
│           │       ├── watermark.png
│           │       └── letterhead.png
│           │
│           └── pdf/                      # ✨ PDF 템플릿 (새로 추가)
│               ├── letterheads/
│               │   ├── corporate-letterhead.pdf
│               │   └── modern-letterhead.pdf
│               └── certificates/
│                   └── certificate-template.pdf
│
├── pptx/
│   └── scripts/
│       └── templates/                    # ✨ PPTX 템플릿 디렉토리 (새로 생성)
│           ├── presentations/            # 전체 프레젠테이션 템플릿
│           │   ├── corporate.pptx
│           │   ├── minimal.pptx
│           │   └── creative.pptx
│           │
│           ├── slides/                   # 개별 슬라이드 템플릿
│           │   ├── title-slides/
│           │   ├── content-slides/
│           │   └── closing-slides/
│           │
│           └── images/                   # PPTX용 이미지 에셋
│               ├── backgrounds/
│               │   ├── gradient-1.png
│               │   └── minimal-bg.png
│               ├── icons/
│               └── charts/
│
├── pdf/
│   └── scripts/
│       └── templates/                    # ✨ PDF 템플릿 디렉토리 (새로 생성)
│           ├── forms/                    # PDF 폼 템플릿
│           │   ├── invoice-template.pdf
│           │   └── contract-template.pdf
│           │
│           ├── designs/                  # 디자인 템플릿
│           │   ├── poster-template.pdf
│           │   └── flyer-template.pdf
│           │
│           └── images/                   # PDF에 삽입할 이미지
│               ├── watermarks/
│               └── signatures/
│
└── xlsx/
    └── scripts/
        └── templates/                    # ✨ XLSX 템플릿 디렉토리 (새로 생성)
            ├── workbooks/                # Excel 템플릿
            │   ├── financial-model.xlsx
            │   └── dashboard-template.xlsx
            │
            └── images/                   # 차트/그래프 이미지
                ├── logos/
                └── charts/
```

## 🔗 Canvas-Design과 연동하기

### 1. Canvas-Design에서 생성한 디자인을 Document-Skills에서 사용

```python
# canvas-design에서 PNG 생성
# output: /workspace/poster-design.png

# DOCX에 이미지 삽입 예시
from docx import Document
from docx.shared import Inches

doc = Document()

# Canvas-design에서 생성한 이미지 추가
doc.add_picture('/workspace/poster-design.png', width=Inches(6))

# 또는 templates에 복사해서 재사용
# cp /workspace/poster-design.png document-skills/docx/scripts/templates/images/headers/
```

### 2. PPTX에 Canvas 디자인 삽입

```python
from pptxgenjs import PptxGenJS

pptx = PptxGenJS()

# 슬라이드 추가
slide = pptx.addSlide()

# Canvas-design 결과물을 배경으로 사용
slide.background = {'path': '/workspace/canvas-art.png'}

# 또는 이미지로 추가
slide.addImage({
    'path': '/workspace/canvas-art.png',
    'x': 0,
    'y': 0,
    'w': '100%',
    'h': '100%'
})

pptx.writeFile('presentation.pptx')
```

### 3. PDF에 Canvas 디자인 삽입

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# PDF 생성
c = canvas.Canvas("output.pdf", pagesize=letter)
width, height = letter

# Canvas-design 이미지 삽입
img = ImageReader('/workspace/canvas-art.png')
c.drawImage(img, 0, 0, width=width, height=height, preserveAspectRatio=True)

c.save()
```

## 💡 추천 워크플로우

### A. 디자인 에셋으로 활용
```bash
# 1. Canvas-design으로 헤더/로고 생성
canvas-design → header.png

# 2. Templates 디렉토리로 복사
cp header.png document-skills/docx/scripts/templates/images/headers/

# 3. 모든 문서에서 재사용
docx/pptx/pdf 생성 시 header.png 참조
```

### B. 페이지별 디자인
```bash
# 1. Canvas-design으로 각 페이지 디자인
canvas-design → page1.pdf, page2.pdf, page3.pdf

# 2. PDF 병합
pypdf로 개별 PDF 병합 → final.pdf
```

### C. 프레젠테이션 슬라이드 배경
```bash
# 1. Canvas-design으로 슬라이드 배경 생성
canvas-design → slide-bg-1.png, slide-bg-2.png

# 2. PPTX templates에 저장
cp slide-bg-*.png document-skills/pptx/scripts/templates/images/backgrounds/

# 3. html2pptx로 프레젠테이션 생성 시 배경 적용
```

## 🛠️ Templates 디렉토리 생성 스크립트

```bash
#!/bin/bash

# DOCX templates
mkdir -p document-skills/docx/scripts/templates/{xml,images/{headers,footers,logos,backgrounds},pdf/{letterheads,certificates}}

# PPTX templates
mkdir -p document-skills/pptx/scripts/templates/{presentations,slides/{title-slides,content-slides,closing-slides},images/{backgrounds,icons,charts}}

# PDF templates
mkdir -p document-skills/pdf/scripts/templates/{forms,designs,images/{watermarks,signatures}}

# XLSX templates
mkdir -p document-skills/xlsx/scripts/templates/{workbooks,images/{logos,charts}}

echo "✅ Templates 디렉토리 구조가 생성되었습니다!"
```

## 📝 사용 예시

### 예시 1: Canvas 아트를 DOCX 커버로 사용
```python
from docx import Document
from docx.shared import Inches

# Canvas-design으로 생성한 커버 이미지
cover_path = 'canvas-design/output/abstract-cover.png'

doc = Document()

# 첫 페이지에 전체 크기 이미지
doc.add_picture(cover_path, width=Inches(8.5))
doc.add_page_break()

# 나머지 내용
doc.add_heading('Document Title', 0)
doc.add_paragraph('Content here...')

doc.save('document-with-canvas-cover.docx')
```

### 예시 2: 여러 Canvas 디자인을 PDF로 병합
```python
from pypdf import PdfWriter, PdfReader

# Canvas-design으로 생성한 개별 페이지들
pages = [
    'canvas-design/output/cover.pdf',
    'canvas-design/output/page1.pdf',
    'canvas-design/output/page2.pdf',
]

writer = PdfWriter()

for pdf_file in pages:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

writer.write('complete-document.pdf')
```

### 예시 3: Canvas 배경을 사용한 PPTX
```javascript
// html2pptx 사용
const pptx = new PptxGenJS();

// Canvas-design 배경 이미지
const bgImage = '/workspace/canvas-bg.png';

// 각 슬라이드에 배경 적용
const slide1 = pptx.addSlide();
slide1.background = { path: bgImage };
slide1.addText('Title', { x: 1, y: 1, fontSize: 44, bold: true });

pptx.writeFile('presentation.pptx');
```

## 🎨 Canvas-Design + Document-Skills 통합 전략

| Canvas-Design 출력 | Document-Skills 용도 | 파일 위치 |
|-------------------|---------------------|----------|
| 로고/헤더 PNG | DOCX/PPTX에 삽입 | `templates/images/headers/` |
| 배경 디자인 PNG | PPTX 슬라이드 배경 | `templates/images/backgrounds/` |
| 포스터 PDF | PDF 병합 또는 변환 | `templates/pdf/designs/` |
| 아이콘 PNG | 모든 문서 타입 | `templates/images/icons/` |
| 전체 페이지 PDF | 다중 페이지 PDF 생성 | `templates/pdf/` |

## ✅ 결론

**Canvas-Design의 출력물(PNG/PDF)을 Document-Skills templates에 저장하고 재사용할 수 있습니다!**

- **PNG**: 이미지로 DOCX/PPTX/PDF에 삽입
- **PDF**: 페이지로 병합하거나 배경/워터마크로 사용
- **Templates**: 재사용 가능한 디자인 에셋 라이브러리 구축
