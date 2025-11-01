# Canva Integration Skill 설계

## 개요
Canva REST API를 사용하여 Claude에서 Canva 디자인을 생성/편집하는 Skill

## Canva API 기능

### 지원 기능:
1. **Design 생성**
   - 템플릿에서 디자인 생성
   - 빈 캔버스에서 시작

2. **Design 편집**
   - 텍스트 수정
   - 이미지 추가/교체
   - 요소 추가

3. **Design Export**
   - PNG, JPG, PDF 내보내기
   - 다양한 해상도

4. **Brand Kit**
   - 브랜드 색상 적용
   - 로고 추가
   - 폰트 적용

## Skill 구조

```
canva-integration/
├── SKILL.md
├── scripts/
│   ├── canva_client.py        # Canva API 클라이언트
│   ├── create_design.py       # 디자인 생성
│   ├── edit_design.py         # 디자인 편집
│   └── export_design.py       # 디자인 내보내기
├── references/
│   ├── canva_api.md           # API 문서
│   ├── templates.md           # 템플릿 목록
│   └── brand_assets.md        # 브랜드 자산
└── assets/
    └── examples/              # 예시 디자인
```

## API 인증

### 필요한 것:
1. Canva 계정 (Pro 이상 권장)
2. API 키 (Canva Developer Portal에서 생성)
3. Access Token

### 설정:
```bash
# 환경 변수 설정
export CANVA_API_KEY="your_api_key"
export CANVA_ACCESS_TOKEN="your_token"
```

## 사용 시나리오

### 시나리오 1: 소셜 미디어 포스트 생성
```
사용자: "Canva에서 인스타그램 포스트를 만들어줘.
        제목은 'New Product Launch', 파란색 배경으로"

Claude (canva-integration 사용):
1. Canva API로 Instagram Post 템플릿 선택
2. 텍스트 "New Product Launch" 추가
3. 배경색을 파란색으로 변경
4. 디자인 URL 반환
5. (선택) PNG로 내보내기
```

### 시나리오 2: 브랜드 템플릿 적용
```
사용자: "toslab 브랜드로 프레젠테이션을 만들어줘"

Claude:
1. Canva에서 Presentation 템플릿 선택
2. Brand Kit에서 toslab 브랜드 자산 적용
3. 제목 슬라이드 생성
4. Canva 편집 링크 제공
```

### 시나리오 3: 일괄 생성
```
사용자: "이 데이터로 10개의 소셜 미디어 포스트를 만들어줘"

Claude:
1. 데이터 파싱
2. 각 항목에 대해 Canva 디자인 생성
3. 텍스트/이미지 자동 채우기
4. 모든 디자인 링크 반환
```

## Python 구현 예시

### canva_client.py
```python
import requests
import os

class CanvaClient:
    def __init__(self, api_key=None, access_token=None):
        self.api_key = api_key or os.getenv('CANVA_API_KEY')
        self.access_token = access_token or os.getenv('CANVA_ACCESS_TOKEN')
        self.base_url = "https://api.canva.com/v1"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def create_design(self, design_type, title=None):
        """
        디자인 생성

        Args:
            design_type: 'instagram-post', 'presentation', 'poster', etc.
            title: 디자인 제목

        Returns:
            디자인 ID 및 편집 URL
        """
        endpoint = f"{self.base_url}/designs"
        payload = {
            "design_type": design_type,
            "title": title or f"New {design_type}"
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        data = response.json()
        return {
            "design_id": data["design"]["id"],
            "edit_url": data["design"]["urls"]["edit_url"],
            "view_url": data["design"]["urls"]["view_url"]
        }

    def add_text(self, design_id, text, font_size=None, color=None):
        """
        텍스트 추가
        """
        endpoint = f"{self.base_url}/designs/{design_id}/elements"
        payload = {
            "type": "text",
            "content": text,
            "font_size": font_size,
            "color": color
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def set_background_color(self, design_id, color):
        """
        배경색 설정
        """
        endpoint = f"{self.base_url}/designs/{design_id}/background"
        payload = {
            "type": "color",
            "color": color
        }

        response = requests.put(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def export_design(self, design_id, format="png", quality="high"):
        """
        디자인 내보내기

        Args:
            design_id: 디자인 ID
            format: 'png', 'jpg', 'pdf'
            quality: 'high', 'medium', 'low'

        Returns:
            다운로드 URL
        """
        endpoint = f"{self.base_url}/designs/{design_id}/export"
        payload = {
            "format": format,
            "quality": quality
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        data = response.json()
        return data["export"]["url"]

    def apply_brand_kit(self, design_id, brand_kit_id):
        """
        브랜드 킷 적용
        """
        endpoint = f"{self.base_url}/designs/{design_id}/brand-kit"
        payload = {
            "brand_kit_id": brand_kit_id
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()


# 사용 예시
if __name__ == "__main__":
    client = CanvaClient()

    # 1. 디자인 생성
    design = client.create_design("instagram-post", "New Product Launch")
    print(f"Design created: {design['edit_url']}")

    # 2. 텍스트 추가
    client.add_text(
        design["design_id"],
        "New Product Launch",
        font_size=48,
        color="#0066CC"
    )

    # 3. 배경색 설정
    client.set_background_color(design["design_id"], "#F0F8FF")

    # 4. 내보내기
    export_url = client.export_design(design["design_id"], format="png")
    print(f"Export URL: {export_url}")
```

### create_design.py (실행 스크립트)
```python
#!/usr/bin/env python3
"""
Canva 디자인 생성 스크립트

Usage:
    create_design.py <design-type> [options]

Examples:
    create_design.py instagram-post --title "Summer Sale" --bg-color "#FFE4E1"
    create_design.py presentation --title "Q1 Review" --brand-kit toslab
"""

import argparse
from canva_client import CanvaClient

def main():
    parser = argparse.ArgumentParser(description='Create Canva design')
    parser.add_argument('design_type',
                        choices=['instagram-post', 'instagram-story',
                                'facebook-post', 'presentation', 'poster',
                                'linkedin-post', 'twitter-post'],
                        help='Type of design to create')
    parser.add_argument('--title', help='Design title')
    parser.add_argument('--text', help='Text to add')
    parser.add_argument('--bg-color', help='Background color (hex)')
    parser.add_argument('--brand-kit', help='Brand kit ID to apply')
    parser.add_argument('--export', choices=['png', 'jpg', 'pdf'],
                        help='Export format')

    args = parser.parse_args()

    # Canva 클라이언트 생성
    client = CanvaClient()

    # 디자인 생성
    print(f"Creating {args.design_type}...")
    design = client.create_design(args.design_type, args.title)
    print(f"✅ Design created: {design['edit_url']}")

    # 텍스트 추가
    if args.text:
        print(f"Adding text: {args.text}")
        client.add_text(design['design_id'], args.text)

    # 배경색 설정
    if args.bg_color:
        print(f"Setting background color: {args.bg_color}")
        client.set_background_color(design['design_id'], args.bg_color)

    # 브랜드 킷 적용
    if args.brand_kit:
        print(f"Applying brand kit: {args.brand_kit}")
        client.apply_brand_kit(design['design_id'], args.brand_kit)

    # 내보내기
    if args.export:
        print(f"Exporting as {args.export}...")
        export_url = client.export_design(design['design_id'], args.export)
        print(f"✅ Export URL: {export_url}")

    print("\n🎨 Design URL:", design['edit_url'])

if __name__ == "__main__":
    main()
```

## SKILL.md 예시

```markdown
---
name: canva-integration
description: |
  Integrates with Canva API to create, edit, and export designs programmatically.
  Use this skill when users want to:
  - Create Canva designs (posts, presentations, posters)
  - Edit existing Canva designs
  - Apply brand kits and templates
  - Export designs to PNG/JPG/PDF
  - Batch create multiple designs

  Requires Canva API credentials.

  Keywords: Canva, design, social media, poster, presentation, Instagram,
  Facebook, brand kit, export, graphic design
allowed-tools: [Bash, Read, Write]
---

# Canva Integration

## Overview
Create and manage Canva designs directly from Claude using Canva REST API.

## Prerequisites

1. **Canva Account** (Pro or Enterprise recommended)
2. **API Credentials**:
   ```bash
   export CANVA_API_KEY="your_api_key"
   export CANVA_ACCESS_TOKEN="your_token"
   ```

   Get credentials at: https://www.canva.com/developers/

## Workflow

### Creating a Design

To create a new Canva design:

```bash
python scripts/create_design.py <design-type> [options]
```

**Supported design types:**
- `instagram-post` (1080x1080)
- `instagram-story` (1080x1920)
- `facebook-post` (940x788)
- `linkedin-post` (1200x627)
- `twitter-post` (1024x512)
- `presentation` (1920x1080)
- `poster` (custom sizes)

**Examples:**
```bash
# Simple Instagram post
python scripts/create_design.py instagram-post --title "Summer Sale"

# With text and background color
python scripts/create_design.py instagram-post \
  --title "Product Launch" \
  --text "Coming Soon!" \
  --bg-color "#0066CC"

# Apply brand kit
python scripts/create_design.py presentation \
  --title "Q1 Review" \
  --brand-kit toslab-brand

# Create and export
python scripts/create_design.py poster \
  --title "Event Flyer" \
  --export png
```

### Editing a Design

To edit existing design:

```bash
python scripts/edit_design.py <design-id> [options]
```

### Exporting a Design

To export design:

```bash
python scripts/export_design.py <design-id> --format png --quality high
```

## Common Workflows

### 1. Social Media Post Campaign
```
User: "Canva로 여름 세일 캠페인을 만들어줘.
      Instagram, Facebook, LinkedIn 각각 필요해"

Steps:
1. Create Instagram post with "Summer Sale" title
2. Create Facebook post with same branding
3. Create LinkedIn post variant
4. Apply toslab brand kit to all
5. Export all as PNG
6. Return all URLs
```

### 2. Presentation from Outline
```
User: "이 아웃라인으로 Canva 프레젠테이션을 만들어줘"

Steps:
1. Create presentation design
2. For each outline point:
   - Add new slide
   - Add title and content
3. Apply brand kit
4. Return edit URL
```

### 3. Batch Content Creation
```
User: "이 CSV 데이터로 각 제품마다 포스터 만들어줘"

Steps:
1. Read CSV data
2. For each product:
   - Create poster design
   - Add product name and description
   - Add product image
3. Export all
4. Return ZIP file with all designs
```

## Brand Kit Integration

To use toslab brand kit:

1. **Setup brand kit in Canva** (one-time)
   - Add brand colors
   - Add logo
   - Add fonts
   - Note brand kit ID

2. **Apply to designs**:
   ```bash
   python scripts/create_design.py presentation \
     --brand-kit toslab-brand
   ```

## API Rate Limits

Canva API limits:
- **Free tier**: 50 requests/hour
- **Pro tier**: 500 requests/hour
- **Enterprise**: Custom limits

The skill automatically handles rate limiting with retries.

## Troubleshooting

**"Authentication failed"**
→ Check CANVA_API_KEY and CANVA_ACCESS_TOKEN environment variables

**"Design type not supported"**
→ Use one of the supported types listed above

**"Rate limit exceeded"**
→ Wait or upgrade to higher tier

## References

- `references/canva_api.md` - Complete API documentation
- `references/templates.md` - Available template types
- `references/brand_assets.md` - Brand kit setup guide
```

## 설치 및 사용

### 1. Skill 생성
```bash
python skill-creator/scripts/init_skill.py canva-integration \
  --path toslab-skills/3-design/
```

### 2. 스크립트 추가
```bash
# canva_client.py와 create_design.py를 scripts/ 폴더에 추가
```

### 3. Dependencies 설치
```bash
# requirements.txt
requests>=2.31.0
python-dotenv>=1.0.0

pip install -r toslab-skills/3-design/canva-integration/requirements.txt
```

### 4. API 키 설정
```bash
# .env 파일 생성
echo "CANVA_API_KEY=your_key" > .env
echo "CANVA_ACCESS_TOKEN=your_token" >> .env
```

### 5. Claude Code에서 사용
```bash
/plugin install /home/user/skills/toslab-skills/3-design/canva-integration

# 사용
"Canva로 Instagram 포스트를 만들어줘. 제목은 'Summer Sale'로"
```

## 고급 기능

### 템플릿 사용
```python
# 특정 템플릿에서 시작
client.create_from_template(template_id="AABBccDD")
```

### 이미지 업로드
```python
# 로컬 이미지를 Canva에 업로드
client.upload_image(design_id, image_path="./product.jpg")
```

### 폴더 관리
```python
# 디자인을 특정 폴더로 이동
client.move_to_folder(design_id, folder_id="campaign-2024")
```

## 제약사항

1. **API 접근**: Canva Pro 이상 필요
2. **Rate Limits**: 시간당 요청 제한
3. **편집 제한**: 일부 고급 편집 기능은 API에서 지원 안 됨
4. **템플릿**: 모든 템플릿이 API로 접근 가능한 것은 아님

## 대안: Canva Embed

API가 제한적이면 Canva Embed를 사용:

```html
<!-- Canva 디자인을 웹페이지에 임베드 -->
<iframe
  src="https://www.canva.com/design/DESIGN_ID/view?embed"
  width="800"
  height="600"
></iframe>
```
