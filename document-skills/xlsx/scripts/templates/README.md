# XLSX Templates

이 디렉토리는 Excel 스프레드시트 생성 시 재사용 가능한 템플릿을 저장합니다.

## 디렉토리 구조

```
templates/
├── workbooks/              # Excel 워크북 템플릿
│   ├── financial-model.xlsx
│   └── dashboard-template.xlsx
│
└── images/                 # 이미지 에셋
    ├── logos/             # 로고 (canvas-design 출력 가능)
    └── charts/            # 차트 이미지
```

## Canvas-Design 통합

Canvas-design에서 생성한 로고나 차트 이미지 저장:

```bash
# Canvas-design 로고 복사
cp /workspace/company-logo.png images/logos/
```

## 사용 예시

```python
from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
sheet = wb.active

# Templates 로고 추가
img = Image('templates/images/logos/company-logo.png')
img.width = 150
img.height = 50
sheet.add_image(img, 'A1')

# 데이터 추가
sheet['A5'] = 'Company Report'

wb.save('report.xlsx')
```
