# Canvas-Design ↔ Document-Skills 통합 예시

## 📋 목차
1. [Canvas 폰트 사용법](#1-canvas-폰트-사용법)
2. [Canvas → DOCX 통합](#2-canvas--docx-통합)
3. [Canvas → PPTX 통합](#3-canvas--pptx-통합)
4. [Canvas → PDF 통합](#4-canvas--pdf-통합)
5. [완전한 워크플로우](#5-완전한-워크플로우)

---

## 1. Canvas 폰트 사용법

### 사용 가능한 폰트 목록

```bash
# Canvas-fonts 디렉토리 구조
canvas-design/canvas-fonts/
├── Sans-serif
│   ├── InstrumentSans-Regular.ttf
│   ├── InstrumentSans-Bold.ttf
│   ├── WorkSans-Regular.ttf
│   ├── Outfit-Regular.ttf
│   └── ArsenalSC-Regular.ttf
│
├── Serif
│   ├── CrimsonPro-Regular.ttf
│   ├── Lora-Regular.ttf
│   ├── LibreBaskerville-Regular.ttf
│   └── YoungSerif-Regular.ttf
│
├── Monospace
│   ├── JetBrainsMono-Regular.ttf
│   ├── GeistMono-Regular.ttf
│   └── IBMPlexMono-Regular.ttf
│
└── Display
    ├── Gloock-Regular.ttf
    ├── NationalPark-Bold.ttf
    └── PoiretOne-Regular.ttf
```

### Python (PIL/Pillow) 사용

```python
from PIL import Image, ImageDraw, ImageFont

# 캔버스 생성 (1920x1080)
img = Image.new('RGB', (1920, 1080), color='#F4F6F6')
draw = ImageDraw.Draw(img)

# Canvas 폰트 로드
font_title = ImageFont.truetype('./canvas-fonts/InstrumentSans-Bold.ttf', 72)
font_body = ImageFont.truetype('./canvas-fonts/CrimsonPro-Regular.ttf', 24)
font_accent = ImageFont.truetype('./canvas-fonts/JetBrainsMono-Regular.ttf', 18)

# 텍스트 그리기
draw.text((100, 100), "DESIGN PHILOSOPHY", fill='#1C2833', font=font_title)
draw.text((100, 200), "Minimal. Precise. Intentional.", fill='#2E4053', font=font_body)
draw.text((100, 900), "2025 — Concrete Poetry", fill='#AAB7B8', font=font_accent)

# 저장
img.save('/workspace/canvas-output.png')
print("✅ PNG 생성 완료: /workspace/canvas-output.png")
```

### Python (ReportLab) PDF 생성

```python
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

# 폰트 등록
pdfmetrics.registerFont(TTFont('InstrumentSans', './canvas-fonts/InstrumentSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lora', './canvas-fonts/Lora-Regular.ttf'))
pdfmetrics.registerFont(TTFont('JetBrains', './canvas-fonts/JetBrainsMono-Regular.ttf'))

# PDF 생성
c = canvas.Canvas("/workspace/canvas-output.pdf", pagesize=letter)
width, height = letter

# 배경색
c.setFillColorRGB(0.96, 0.97, 0.97)
c.rect(0, 0, width, height, fill=1, stroke=0)

# 텍스트 작성
c.setFillColorRGB(0.11, 0.16, 0.2)
c.setFont('InstrumentSans', 48)
c.drawString(100, height - 100, "MINIMAL DESIGN")

c.setFillColorRGB(0.18, 0.25, 0.33)
c.setFont('Lora', 18)
c.drawString(100, height - 150, "Form follows function")

c.setFillColorRGB(0.67, 0.72, 0.72)
c.setFont('JetBrains', 12)
c.drawString(100, 50, "Document ID: CDP-2025-001")

c.save()
print("✅ PDF 생성 완료: /workspace/canvas-output.pdf")
```

---

## 2. Canvas → DOCX 통합

### 예시 A: Canvas 헤더를 DOCX에 삽입

```python
# Step 1: Canvas-design으로 헤더 생성
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (2400, 300), color='#1C2833')
draw = ImageDraw.Draw(img)

font = ImageFont.truetype('./canvas-fonts/InstrumentSans-Bold.ttf', 60)
draw.text((100, 100), "CORPORATE REPORT 2025", fill='#F4F6F6', font=font)

header_path = './document-skills/docx/scripts/templates/images/headers/corporate-header.png'
img.save(header_path)
print(f"✅ 헤더 저장: {header_path}")

# Step 2: DOCX 문서에 헤더 추가
from docx import Document
from docx.shared import Inches

doc = Document()

# Templates 헤더 추가
doc.add_picture(header_path, width=Inches(6.5))

# 내용 추가
doc.add_heading('Executive Summary', 1)
doc.add_paragraph('This report outlines the strategic initiatives...')

doc.save('/workspace/corporate-report.docx')
print("✅ DOCX 생성 완료: /workspace/corporate-report.docx")
```

### 예시 B: 여러 Canvas 디자인을 페이지로 추가

```python
from docx import Document
from docx.shared import Inches

# Canvas-design에서 여러 페이지 생성 (가정)
pages = [
    './workspace/cover-design.png',
    './workspace/section1-design.png',
    './workspace/section2-design.png',
]

doc = Document()

for page_path in pages:
    # 전체 페이지 이미지
    doc.add_picture(page_path, width=Inches(7.5))
    doc.add_page_break()

doc.save('/workspace/design-document.docx')
print("✅ 디자인 문서 생성 완료")
```

---

## 3. Canvas → PPTX 통합

### 예시 A: Canvas 배경을 슬라이드에 적용

```javascript
// Node.js 스크립트: create-presentation.js

const PptxGenJS = require('pptxgenjs');
const pptx = new PptxGenJS();

// Canvas-design 배경 경로
const backgrounds = [
    './document-skills/pptx/scripts/templates/images/backgrounds/abstract-1.png',
    './document-skills/pptx/scripts/templates/images/backgrounds/abstract-2.png',
    './document-skills/pptx/scripts/templates/images/backgrounds/minimal.png',
];

// 슬라이드 1: 타이틀 (배경 1)
const slide1 = pptx.addSlide();
slide1.background = { path: backgrounds[0] };
slide1.addText('DESIGN PHILOSOPHY', {
    x: 1, y: 2, w: 8, h: 1.5,
    fontSize: 48, bold: true, color: 'FFFFFF',
    fontFace: 'Arial'
});

// 슬라이드 2: 콘텐츠 (배경 2)
const slide2 = pptx.addSlide();
slide2.background = { path: backgrounds[1] };
slide2.addText('Core Principles', { x: 0.5, y: 0.5, fontSize: 36, bold: true });
slide2.addText([
    { text: 'Minimal design\n', options: { fontSize: 20 } },
    { text: 'Intentional composition\n', options: { fontSize: 20 } },
    { text: 'Expert craftsmanship', options: { fontSize: 20 } }
], { x: 1, y: 2, w: 8, h: 3 });

// 슬라이드 3: 마무리 (배경 3)
const slide3 = pptx.addSlide();
slide3.background = { path: backgrounds[2] };
slide3.addText('Thank You', {
    x: 3, y: 3, w: 4, h: 1,
    fontSize: 44, align: 'center', color: '1C2833'
});

pptx.writeFile('/workspace/design-presentation.pptx');
console.log('✅ PPTX 생성 완료: /workspace/design-presentation.pptx');
```

실행:
```bash
cd /home/user/skills
node create-presentation.js
```

### 예시 B: Python으로 PPTX 생성 (python-pptx)

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from PIL import Image

# 새 프레젠테이션
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# 빈 레이아웃
blank_layout = prs.slide_layouts[6]

# 슬라이드 1: Canvas 배경 + 텍스트
slide1 = prs.slides.add_slide(blank_layout)

# Canvas 배경 이미지
bg_path = './document-skills/pptx/scripts/templates/images/backgrounds/gradient-1.png'
slide1.shapes.add_picture(bg_path, 0, 0, width=prs.slide_width, height=prs.slide_height)

# 텍스트 박스
txBox = slide1.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(2))
tf = txBox.text_frame
tf.text = "GEOMETRIC SILENCE"
p = tf.paragraphs[0]
p.font.size = Pt(60)
p.font.bold = True
p.font.color.rgb = RGBColor(255, 255, 255)

prs.save('/workspace/python-pptx-output.pptx')
print("✅ Python PPTX 생성 완료")
```

---

## 4. Canvas → PDF 통합

### 예시 A: 여러 Canvas PDF를 하나로 병합

```python
from pypdf import PdfWriter, PdfReader

# Canvas-design에서 생성한 개별 PDF들
canvas_pdfs = [
    '/workspace/canvas-cover.pdf',
    '/workspace/canvas-page1.pdf',
    '/workspace/canvas-page2.pdf',
    '/workspace/canvas-page3.pdf',
]

writer = PdfWriter()

for pdf_path in canvas_pdfs:
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        writer.add_page(page)

output_path = '/workspace/complete-design-book.pdf'
with open(output_path, 'wb') as f:
    writer.write(f)

print(f"✅ PDF 병합 완료: {output_path}")
print(f"   총 페이지: {len(writer.pages)}")
```

### 예시 B: Canvas 이미지를 PDF 배경으로 사용

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

# Canvas-design 배경 이미지
bg_image_path = './document-skills/pdf/scripts/templates/images/watermarks/abstract-bg.png'

c = canvas.Canvas('/workspace/report-with-bg.pdf', pagesize=letter)
width, height = letter

# 배경 이미지 삽입 (투명도 조정 가능)
c.drawImage(bg_image_path, 0, 0, width=width, height=height, preserveAspectRatio=True, mask='auto')

# 위에 텍스트 작성
c.setFillColorRGB(0, 0, 0)
c.setFont('Helvetica-Bold', 36)
c.drawString(100, height - 100, "Annual Report")

c.setFont('Helvetica', 14)
c.drawString(100, height - 150, "With custom canvas background")

c.save()
print("✅ 배경 포함 PDF 생성 완료")
```

---

## 5. 완전한 워크플로우

### 시나리오: 회사 브로셔 제작

**Step 1: Canvas-design으로 디자인 에셋 생성**

```python
# design-assets.py
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.pagesizes import letter

# 1. 로고 생성
logo = Image.new('RGB', (400, 100), color='#1C2833')
draw = ImageDraw.Draw(logo)
font = ImageFont.truetype('./canvas-fonts/InstrumentSans-Bold.ttf', 48)
draw.text((50, 20), "ACME Corp", fill='#F4F6F6', font=font)
logo.save('./document-skills/docx/scripts/templates/images/logos/acme-logo.png')
print("✅ 로고 생성")

# 2. 헤더 디자인
header = Image.new('RGB', (2400, 200), color='#2E4053')
draw = ImageDraw.Draw(header)
font_header = ImageFont.truetype('./canvas-fonts/WorkSans-Bold.ttf', 60)
draw.text((100, 60), "COMPANY BROCHURE 2025", fill='#FFFFFF', font=font_header)
header.save('./document-skills/docx/scripts/templates/images/headers/brochure-header.png')
print("✅ 헤더 생성")

# 3. PPTX 배경 생성
for i in range(3):
    bg = Image.new('RGB', (1920, 1080), color=f'#{["E8B4B8", "87A96B", "98ACB5"][i]}')
    bg.save(f'./document-skills/pptx/scripts/templates/images/backgrounds/slide-bg-{i+1}.png')
print("✅ 슬라이드 배경 생성")

# 4. PDF 커버 페이지
c = pdf_canvas.Canvas('./workspace/brochure-cover.pdf', pagesize=letter)
width, height = letter
c.setFillColorRGB(0.11, 0.16, 0.2)
c.rect(0, 0, width, height, fill=1)
c.setFillColorRGB(0.96, 0.97, 0.97)
c.setFont('Helvetica-Bold', 72)
c.drawCentredString(width/2, height/2, "ACME")
c.save()
print("✅ PDF 커버 생성")
```

**Step 2: DOCX 문서 생성**

```python
# create-docx.py
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# 헤더 이미지
doc.add_picture('./document-skills/docx/scripts/templates/images/headers/brochure-header.png',
                width=Inches(6.5))

# 로고
doc.add_picture('./document-skills/docx/scripts/templates/images/logos/acme-logo.png',
                width=Inches(2))

# 내용
heading = doc.add_heading('About ACME Corporation', 1)
heading.alignment = WD_ALIGN_PARAGRAPH.LEFT

para = doc.add_paragraph()
para.add_run('We are a leading provider of innovative solutions...').font.size = Pt(12)

doc.save('/workspace/acme-brochure.docx')
print("✅ DOCX 브로셔 생성")
```

**Step 3: PPTX 프레젠테이션 생성**

```python
# create-pptx.py
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
blank_layout = prs.slide_layouts[6]

backgrounds = [
    './document-skills/pptx/scripts/templates/images/backgrounds/slide-bg-1.png',
    './document-skills/pptx/scripts/templates/images/backgrounds/slide-bg-2.png',
    './document-skills/pptx/scripts/templates/images/backgrounds/slide-bg-3.png',
]

titles = ['Welcome to ACME', 'Our Services', 'Contact Us']

for i, (bg, title) in enumerate(zip(backgrounds, titles)):
    slide = prs.slides.add_slide(blank_layout)
    slide.shapes.add_picture(bg, 0, 0, width=prs.slide_width, height=prs.slide_height)

    txBox = slide.shapes.add_textbox(Inches(1), Inches(1), Inches(8), Inches(1.5))
    tf = txBox.text_frame
    tf.text = title
    tf.paragraphs[0].font.size = Pt(48)
    tf.paragraphs[0].font.bold = True

prs.save('/workspace/acme-presentation.pptx')
print("✅ PPTX 프레젠테이션 생성")
```

**Step 4: PDF 최종 문서 생성**

```python
# create-final-pdf.py
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# 커버 (Canvas-design)
cover = PdfReader('./workspace/brochure-cover.pdf')

# 내용 페이지 생성
content = canvas.Canvas('/tmp/content.pdf', pagesize=letter)
width, height = letter

content.setFont('Helvetica-Bold', 24)
content.drawString(100, height - 100, "Our Services")

content.setFont('Helvetica', 12)
y = height - 150
for service in ['Consulting', 'Development', 'Support']:
    content.drawString(120, y, f"• {service}")
    y -= 30

content.save()

# PDF 병합
writer = PdfWriter()
writer.add_page(cover.pages[0])

content_reader = PdfReader('/tmp/content.pdf')
for page in content_reader.pages:
    writer.add_page(page)

with open('/workspace/acme-final.pdf', 'wb') as f:
    writer.write(f)

print("✅ 최종 PDF 생성 완료")
```

**전체 실행:**

```bash
cd /home/user/skills

# 1. 디자인 에셋 생성
python design-assets.py

# 2. 문서 생성
python create-docx.py
python create-pptx.py
python create-final-pdf.py

echo "✅ 모든 브로셔 자료가 생성되었습니다!"
ls -lh /workspace/acme-*
```

---

## 📊 요약표

| Canvas 출력 | Document-Skills 저장 위치 | 용도 | 코드 예시 |
|-----------|------------------------|------|---------|
| PNG (로고) | `docx/scripts/templates/images/logos/` | DOCX/PPTX/PDF 로고 | `doc.add_picture()` |
| PNG (헤더) | `docx/scripts/templates/images/headers/` | DOCX 헤더 | `doc.add_picture()` |
| PNG (배경) | `pptx/scripts/templates/images/backgrounds/` | PPTX 슬라이드 배경 | `slide.background = {path}` |
| PNG (워터마크) | `pdf/scripts/templates/images/watermarks/` | PDF 워터마크 | `page.merge_page()` |
| PDF (디자인) | `pdf/scripts/templates/designs/` | PDF 페이지 | `writer.add_page()` |
| PDF (폼) | `pdf/scripts/templates/forms/` | PDF 템플릿 | `PdfReader()` |

---

## 🎯 핵심 포인트

1. **Canvas 폰트**: `./canvas-fonts/*.ttf` 경로에서 로드
2. **Templates**: 생성한 디자인을 적절한 templates 디렉토리에 저장
3. **재사용**: 한 번 생성한 에셋을 여러 문서에서 재사용
4. **통합**: Canvas-design(디자인) + Document-skills(문서 생성) 조합

```
Canvas-Design        Templates           Document-Skills
    │                    │                      │
    │  PNG/PDF 생성      │                      │
    ├──────────────────→ │ 저장                 │
    │                    │                      │
    │                    │  재사용              │
    │                    ├────────────────────→ │
    │                    │                      │
    │                    │                 DOCX/PPTX/PDF
```

완성! 🎉
