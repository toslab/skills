# Detail Page Designer Skill - 완벽 사용 가이드

## 📚 목차

1. [Skill이란 무엇인가?](#skill이란-무엇인가)
2. [이 Skill의 구조](#이-skill의-구조)
3. [설치 및 사용 방법](#설치-및-사용-방법)
4. [5가지 디자인 스타일 소개](#5가지-디자인-스타일-소개)
5. [상세 사용 예시](#상세-사용-예시)
6. [커스터마이징 방법](#커스터마이징-방법)
7. [실전 팁](#실전-팁)

---

## Skill이란 무엇인가?

**Skill**은 Claude가 특정 작업을 전문적으로 수행할 수 있도록 하는 **지침과 리소스 모음**입니다.

### Skill의 핵심 개념

```
일반 Claude:
"상세페이지를 만들어줘"
→ 매번 다른 스타일, 일관성 없음

Skill이 있는 Claude:
"상세페이지를 만들어줘"
→ 5가지 전문 스타일 제시
→ 선택하면 일관되게 적용
→ 모든 디자인 요소가 체계적
```

### Skill의 장점

✅ **일관성**: 매번 같은 품질의 결과물
✅ **전문성**: 사전 정의된 디자인 시스템 활용
✅ **효율성**: 긴 설명 없이 빠른 작업
✅ **재사용성**: 한 번 만들면 계속 활용
✅ **커스터마이징**: 자신만의 스타일 추가 가능

---

## 이 Skill의 구조

### 📁 파일 구조 설명

```
detail-page-designer/
│
├── SKILL.md                    # 메인 Skill 파일 (필수)
│   └── YAML frontmatter + 사용 지침
│
├── LICENSE.txt                 # 라이센스 파일
│
├── README_KR.md               # 이 파일 (한국어 가이드)
│
└── styles/                     # 디자인 스타일 정의 폴더
    ├── luxury-premium.md       # 럭셔리 프리미엄 스타일
    ├── modern-minimal.md       # 모던 미니멀 스타일
    ├── vibrant-energetic.md    # 활기찬 에너제틱 스타일
    ├── elegant-classic.md      # 우아한 클래식 스타일
    └── warm-natural.md         # 따뜻한 내츄럴 스타일
```

### 각 파일의 역할

#### 1. **SKILL.md** (핵심 파일)

```yaml
---
name: detail-page-designer
description: 상세페이지 디자인을 위한 전문 도구...
---

# 이 부분이 Claude에게 전달되는 지침입니다
- 어떻게 동작할지
- 어떤 스타일이 있는지
- 어떻게 적용할지
```

**역할**:
- Claude에게 이 Skill의 목적과 사용법 알려주기
- 5가지 스타일 소개
- 워크플로우 정의
- 커스텀 디자인 생성 방법 안내

#### 2. **styles/*.md** (스타일 정의 파일)

각 스타일 파일은 **완전한 디자인 시스템**을 포함합니다:

```markdown
# Luxury Premium Style

## 브랜드 무드 & 분위기
- 핵심 키워드
- 감성적 목표
- 피해야 할 요소

## 컬러 시스템
- Primary Colors (주요 색상)
- Secondary Colors (보조 색상)
- Neutral Colors (중립 색상)
- Accent Colors (강조 색상)

## 타이포그래피
- Display Font (디스플레이 폰트)
- Heading Font (제목 폰트)
- Body Font (본문 폰트)
- Small Text (작은 텍스트)

## 레이아웃 원칙
- 그리드 시스템
- 여백 규칙
- 섹션 구조

## UI 요소 스타일
- 버튼
- 카드 컴포넌트
- 아이콘
- 이미지 처리
- 폼 요소

## 애니메이션 & 인터랙션
## 반응형 디자인
## 실전 예시 코드
## 체크리스트
```

**각 스타일 파일은**:
- 📝 **2000-3000줄** 이상의 상세한 가이드
- 🎨 **모든 디자인 요소** 정의 (컬러, 폰트, 레이아웃, UI)
- 💻 **실제 코드 예시** 포함 (CSS, HTML)
- ✅ **체크리스트**로 품질 확인

---

## 설치 및 사용 방법

### 방법 1: Claude.ai에서 사용 (가장 쉬움)

1. **Skill 업로드**
   - Claude.ai 접속
   - 프로젝트 생성 또는 기존 프로젝트 선택
   - "Add content" → "Upload files"
   - `detail-page-designer` 폴더 전체 업로드

2. **Skill 활성화 확인**
   - Claude가 자동으로 SKILL.md 파일 인식
   - "I've loaded the detail-page-designer skill" 메시지 확인

3. **바로 사용**
   ```
   사용자: "프리미엄 가구 제품의 상세페이지를 만들어줘"

   Claude: "상세페이지를 디자인하기 위해 5가지 스타일을 추천드립니다:

   1. Luxury Premium - 고급스럽고 세련된 (추천!)
   2. Modern Minimal - 깔끔하고 현대적
   3. Vibrant Energetic - 밝고 역동적
   4. Elegant Classic - 우아하고 전통적
   5. Warm Natural - 따뜻하고 친근한

   어떤 스타일을 선호하시나요?"
   ```

### 방법 2: Claude Code에서 사용

1. **이 저장소를 마켓플레이스에 추가**
   ```bash
   /plugin marketplace add [your-username]/skills
   ```

2. **Skill 설치**
   ```bash
   /plugin install detail-page-designer
   ```

3. **사용**
   - 프로젝트에서 자동으로 로드됨
   - 상세페이지 디자인 요청시 자동 활성화

### 방법 3: API 사용 (개발자용)

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Skill 파일 읽기
with open("detail-page-designer/SKILL.md", "r") as f:
    skill_content = f.read()

# 메시지에 Skill 포함
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    system=skill_content,  # Skill을 system prompt로
    messages=[
        {
            "role": "user",
            "content": "럭셔리 시계 제품의 상세페이지 디자인해줘"
        }
    ]
)
```

---

## 5가지 디자인 스타일 소개

### 1. 🏆 Luxury Premium (럭셔리 프리미엄)

**핵심 컬러**: Deep Charcoal, Champagne Gold, Ivory Cream
**폰트**: Playfair Display (Display), Montserrat (Heading), Lora (Body)
**분위기**: 세련됨, 고급스러움, 독점적

**적합한 제품/서비스**:
- ✨ 고급 패션 & 액세서리
- 🚗 프리미엄 자동차
- 🏨 럭셔리 호텔 & 리조트
- 💎 주얼리 & 시계
- 🏡 고가 가구 & 인테리어

**주요 특징**:
- 절제된 컬러 팔레트 (블랙, 골드, 크림)
- 넉넉한 여백으로 고급스러움 표현
- 세리프 + 산세리프 조화
- 우아한 애니메이션 (느리고 부드럽게)

**사용 예시**:
```
사용자: "1000만원짜리 명품 가방 상세페이지를 만들어줘"
→ Luxury Premium 스타일 추천
→ 골드 액센트, 큰 제품 사진, 우아한 타이포그래피
```

---

### 2. ✨ Modern Minimal (모던 미니멀)

**핵심 컬러**: Pure Black, Electric Blue, Pure White
**폰트**: Inter (모든 용도)
**분위기**: 깔끔함, 효율적, 현대적

**적합한 제품/서비스**:
- 💻 SaaS 플랫폼
- 🚀 테크 스타트업
- 🎨 디자인 도구
- 📱 생산성 앱
- 💰 핀테크 서비스

**주요 특징**:
- 미니멀한 컬러 (블랙, 화이트, 블루만)
- 4px 기반 여백 시스템
- 산세리프 폰트만 사용
- Flat 디자인 (그림자 최소)
- 빠른 애니메이션 (0.2s)

**사용 예시**:
```
사용자: "새로운 프로젝트 관리 SaaS 서비스 소개 페이지"
→ Modern Minimal 스타일 추천
→ 깔끔한 그리드, 블루 CTA, 명확한 위계
```

---

### 3. 🎉 Vibrant Energetic (활기찬 에너제틱)

**핵심 컬러**: Electric Purple, Hot Pink, Sunshine Yellow
**폰트**: Poppins (Display/Heading), Inter (Body)
**분위기**: 대담함, 창의적, 즐거움

**적합한 제품/서비스**:
- 🎵 음악/엔터테인먼트 앱
- 🎮 게이밍 제품
- 👕 패션/뷰티 (젊은 브랜드)
- 🏃 스포츠/피트니스
- 🎨 크리에이티브 에이전시

**주요 특징**:
- 다채로운 컬러 (2-3가지 이상 동시 사용)
- 그라디언트 적극 활용
- 비대칭 레이아웃
- 재미있는 애니메이션 (bounce, wiggle)
- 큰 타이포그래피

**사용 예시**:
```
사용자: "10대 타겟 음악 스트리밍 앱 소개"
→ Vibrant Energetic 스타일 추천
→ 컬러풀한 그라디언트, 큰 제목, 역동적 레이아웃
```

---

### 4. 🎩 Elegant Classic (우아한 클래식)

**핵심 컬러**: Navy Blue, Antique Gold, Cream
**폰트**: Cormorant Garamond (Display), Libre Baskerville (Heading), Lora (Body)
**분위기**: 전통적, 신뢰감, 시간을 초월한

**적합한 제품/서비스**:
- ⚖️ 법률 서비스
- 🏦 금융/은행
- 🎓 교육 기관
- 🏛️ 박물관/문화 기관
- 🏥 의료/헬스케어

**주요 특징**:
- 클래식한 컬러 (네이비, 골드, 크림)
- 세리프 폰트 위주
- 대칭적 레이아웃
- 장식적 요소 (구분선, 프레임)
- 느리고 우아한 애니메이션

**사용 예시**:
```
사용자: "100년 역사의 법률 회사 소개 페이지"
→ Elegant Classic 스타일 추천
→ 세리프 폰트, 대칭 레이아웃, 골드 액센트
```

---

### 5. 🌿 Warm Natural (따뜻한 내츄럴)

**핵심 컬러**: Warm Terracotta, Sage Green, Warm Sand
**폰트**: Fraunces (Display), Karla (Heading), Lora (Body)
**분위기**: 편안함, 자연스러움, 진정성

**적합한 제품/서비스**:
- 🥗 오가닉 식품/음료
- 🧴 내츄럴 뷰티/스킨케어
- 🧘 웰니스/요가
- 🌱 친환경 제품
- ☕ 카페/베이커리

**주요 특징**:
- 자연에서 영감받은 컬러 (대지톤)
- 모든 요소 둥글게 (20-32px radius)
- 유기적 도형과 장식
- 부드러운 질감과 레이어
- 느리고 자연스러운 애니메이션

**사용 예시**:
```
사용자: "유기농 스킨케어 제품 상세페이지"
→ Warm Natural 스타일 추천
→ 베이지/그린 톤, 둥근 카드, 자연 사진
```

---

## 상세 사용 예시

### 예시 1: 럭셔리 시계 제품 페이지

**대화 흐름**:

```
👤 사용자:
"100만원대 스위스 시계 브랜드의 신제품 상세페이지를 만들어줘.
타겟은 30-50대 남성이고, 프리미엄 느낌이 중요해."

🤖 Claude (Skill 활용):
"프리미엄 시계 제품을 위한 상세페이지를 디자인하겠습니다.

타겟과 제품 특성을 고려했을 때, 다음 스타일을 추천드립니다:

**1순위: Luxury Premium** ⭐ (가장 적합)
- 고급스럽고 세련된 분위기
- Deep Charcoal + Champagne Gold 조합
- 큰 제품 사진과 우아한 타이포그래피
- 30-50대 남성에게 어필

**2순위: Elegant Classic**
- 전통과 신뢰를 강조
- Navy + Gold 조합
- 100만원대 가격대에 적합

**3순위: Modern Minimal**
- 현대적이고 세련됨
- 단, 다소 차가울 수 있음

어떤 스타일을 선택하시겠습니까?"

👤 사용자:
"Luxury Premium으로 해줘"

🤖 Claude:
"Luxury Premium 스타일을 적용하여 디자인하겠습니다.
styles/luxury-premium.md 파일의 디자인 시스템을 기반으로
다음과 같이 페이지를 구성합니다:

---

## 컬러 시스템
- **주요**: Deep Charcoal (#2C2C2C)
- **액센트**: Champagne Gold (#D4AF37)
- **배경**: Ivory Cream (#F8F6F0)

## 타이포그래피
- **메인 제목**: Playfair Display Bold, 64px
  "Swiss Precision, Timeless Elegance"
- **섹션 제목**: Montserrat SemiBold, 36px
- **본문**: Lora Regular, 18px

## 레이아웃 구조

### Hero Section
- 전체 화면 높이
- 좌측: 제품 사진 (고해상도, 블랙 배경)
- 우측:
  - 브랜드 로고 (골드)
  - 제품명 (Playfair Display)
  - 가격 (Montserrat, 골드)
  - CTA 버튼 (골드 배경, "VIEW DETAILS")

### Features Section
- 3컬럼 그리드
- 각 Feature:
  - 골드 아이콘 (64x64px)
  - 제목: "Swiss Movement", "Sapphire Crystal", etc.
  - 설명 (2-3줄)

[... 상세한 HTML/CSS 코드 ...]

제공된 모든 디자인 요소를 luxury-premium.md 가이드라인에
따라 정확히 적용했습니다."
```

**결과물**:
- ✅ 일관된 프리미엄 디자인
- ✅ 모든 컬러, 폰트, 레이아웃이 스타일 가이드 준수
- ✅ 타겟에 최적화된 UI/UX
- ✅ 즉시 구현 가능한 코드

---

### 예시 2: SaaS 플랫폼 랜딩 페이지

```
👤 사용자:
"AI 기반 마케팅 자동화 SaaS의 랜딩 페이지를 만들어줘.
스타트업이고, B2B 타겟이야."

🤖 Claude:
"B2B SaaS 플랫폼을 위한 랜딩 페이지를 디자인하겠습니다.

**추천 스타일: Modern Minimal** ⭐
- SaaS에 가장 적합한 스타일
- 신뢰감 있고 전문적
- 빠른 정보 전달

적용할까요?"

👤 사용자:
"응, 그리고 주요 색상을 파란색 대신 보라색으로 바꿀 수 있어?"

🤖 Claude:
"물론입니다! Modern Minimal 스타일을 기반으로
커스텀 컬러 팔레트를 적용하겠습니다.

## 커스터마이즈된 컬러 시스템
- **Primary**: Deep Purple (#6B4FEE) ← 변경
- **Secondary**: Black (#000000)
- **Neutral**: White, Gray 계열 유지
- **Accent**: Purple 기반 그라디언트

나머지 타이포그래피, 레이아웃, UI 요소는
Modern Minimal 가이드를 따릅니다.

[... HTML/CSS 코드 ...]"
```

**핵심**:
- Skill의 가이드라인을 기반으로 하되
- 사용자 요구에 맞게 커스터마이징 가능
- 일관성은 유지하면서 유연성 제공

---

## 커스터마이징 방법

### 방법 1: 기존 스타일 수정

**시나리오**: Luxury Premium 스타일이 좋은데, 골드 대신 실버를 쓰고 싶음

1. **styles/luxury-premium.md 복사**
   ```bash
   cp luxury-premium.md luxury-premium-silver.md
   ```

2. **파일 열어서 수정**
   ```markdown
   # Luxury Premium Silver Style

   ## 컬러 시스템

   ### Primary Colors

   **Deep Charcoal** `#2C2C2C` (유지)

   **Platinum Silver** `#C0C0C0` ← 변경
   - 사용처: 액센트, CTA 버튼, 아이콘, 구분선
   - 느낌: 현대적 럭셔리, 기술적 세련됨

   ... (나머지 골드 → 실버로 전체 변경)
   ```

3. **SKILL.md에 추가**
   ```markdown
   ## 제공되는 디자인 스타일

   총 6가지의 완성도 높은 디자인 스타일을 제공합니다:

   1. **Luxury Premium** (럭셔리 프리미엄 - 골드)
   2. **Luxury Premium Silver** (럭셔리 프리미엄 - 실버) ← 추가
   3. **Modern Minimal** (모던 미니멀)
   ...
   ```

4. **사용**
   ```
   사용자: "Luxury Premium Silver 스타일로 페이지 만들어줘"
   → Claude가 새 스타일 적용
   ```

---

### 방법 2: 완전히 새로운 스타일 만들기

**시나리오**: 레트로/빈티지 느낌의 디자인 시스템이 필요함

1. **템플릿 복사**
   ```bash
   cp styles/luxury-premium.md styles/retro-vintage.md
   ```

2. **새로운 스타일 정의**

```markdown
# Retro Vintage Style

70-80년대 레트로 감성과 빈티지 디자인의 조화

## 브랜드 무드 & 분위기

### 핵심 키워드
- **Nostalgic** (향수를 불러일으키는)
- **Funky** (펑키한)
- **Groovy** (그루비한)
- **Retro** (복고풍)
- **Playful** (재미있는)

### 감성적 목표
- "옛날이 생각난다"
- "재미있고 독특하다"
- "트렌디하면서 익숙하다"

## 컬러 시스템

### Primary Colors
**Burnt Orange** `#FF6B35`
- 70년대 대표 컬러
- 따뜻하고 활기찬

**Mustard Yellow** `#F7B801`
- 빈티지 느낌
- 레트로 포인트

**Avocado Green** `#6A994E`
- 70년대 인테리어 컬러
- 자연스러운 복고

### Typography
**Font Family**: Bebas Neue (Display), Archivo (Heading), IBM Plex Mono (Body)
- Bebas Neue: 70년대 포스터 느낌
- IBM Plex Mono: 타자기 느낌

### 레이아웃 원칙
- 그루비한 물결 모양
- 비대칭적이지만 균형
- 큰 타이포그래피
- 반복되는 패턴

### UI 요소
- 버튼: 둥근 모서리, 두꺼운 테두리
- 카드: 종이 질감, 그림자
- 아이콘: 두툼하고 단순한
- 패턴: 체크무늬, 꽃무늬, 기하학

### 애니메이션
- Groovy wave
- Bounce 효과
- Rotate 활용

... (상세하게 계속 작성)
```

3. **SKILL.md 업데이트**
4. **Claude에게 테스트**

---

### 방법 3: 브랜드 가이드라인 통합

**시나리오**: 회사 고유의 브랜드 컬러와 폰트가 있음

**예시**: 회사 브랜드
- 주요 색상: `#2E5090` (코발트 블루)
- 보조 색상: `#E67E22` (오렌지)
- 폰트: Proxima Nova

**스타일 파일 생성**: `styles/company-brand.md`

```markdown
# Company Brand Style

우리 회사의 공식 브랜드 가이드라인을 따르는 디자인 시스템

## 컬러 시스템

### Primary Colors (공식 브랜드 컬러)

**Cobalt Blue** `#2E5090`
- 회사 공식 주요 색상
- 사용처: 로고, 주요 CTA, 헤더

**Energetic Orange** `#E67E22`
- 회사 공식 보조 색상
- 사용처: 강조, 링크, 아이콘

### Typography (공식 브랜드 폰트)

**Font Family**: Proxima Nova
- Display: Proxima Nova Bold
- Heading: Proxima Nova Semibold
- Body: Proxima Nova Regular

### 브랜드 규정
- 로고 사용 규정 준수
- 최소 여백: 로고 높이의 1.5배
- 컬러 변형 금지
- 폰트 대체 불가

... (회사 브랜드 가이드라인 모두 포함)
```

**사용**:
```
사용자: "Company Brand 스타일로 신제품 페이지 만들어줘"
→ 모든 요소가 회사 브랜드 준수
```

---

## 실전 팁

### 💡 Tip 1: 스타일 선택이 어려울 때

```
사용자: "어떤 스타일을 선택해야 할지 모르겠어.
우리 제품은 친환경 대나무 칫솔이야."

Claude 응답 (Skill 기반):
"친환경 대나무 칫솔을 위한 최적의 스타일을 추천드립니다:

**1순위: Warm Natural** ⭐⭐⭐
- 자연, 유기농, 친환경에 완벽
- 따뜻한 대지 톤 (테라코타, 세이지 그린)
- 둥근 요소로 부드러움 표현
- 타겟(환경 의식 소비자)에게 가장 공감

**2순위: Modern Minimal**
- 깔끔하고 현대적
- 지속가능성 + 미니멀리즘 연결 가능
- 단, Warm Natural보다 차가울 수 있음

**3순위: Elegant Classic**
- 품질과 신뢰 강조
- 다소 형식적일 수 있어 친환경 느낌이 덜함

추천: Warm Natural로 시작하시는 것이 좋겠습니다!"
```

**팁**: Claude에게 제품/서비스 특성을 자세히 알려주면, Skill 기반으로 최적 스타일 추천

---

### 💡 Tip 2: 여러 스타일 혼합

```
사용자: "Modern Minimal의 깔끔함 + Warm Natural의 컬러를 섞을 수 있어?"

Claude:
"물론입니다! 두 스타일의 장점을 결합한 커스텀 스타일을 만들겠습니다:

## Modern Natural Style (커스텀)

### 컬러 시스템 (Warm Natural에서)
- Primary: Sage Green (#7C9885)
- Secondary: Terracotta (#D97757)
- Neutral: Warm Sand (#E6D5B8)

### 타이포그래피 (Modern Minimal에서)
- Font: Inter (산세리프, 하나만)
- 크기와 무게로 위계 구분

### 레이아웃 (Modern Minimal에서)
- 12 Column Grid
- 4px 기반 여백
- 깔끔한 정렬

### UI 요소
- 버튼: 미니멀하지만 컬러풀 (Terracotta 배경)
- 카드: Flat 디자인 + 자연 컬러
- 라운드: 12px (Modern보다 약간 둥글게)

이렇게 두 스타일의 best practices를 결합했습니다!"
```

**팁**: Skill 파일들을 "재료"처럼 활용하여 자유롭게 믹스 가능

---

### 💡 Tip 3: 섹션별로 다른 스타일

```
사용자: "히어로는 Vibrant Energetic,
제품 설명은 Modern Minimal로 할 수 있어?"

Claude:
"가능하지만 주의가 필요합니다.
두 스타일의 차이가 커서 일관성이 떨어질 수 있습니다.

대신 이렇게 제안드립니다:

**통합 스타일: Vibrant Modern**

1. Hero Section
- Vibrant 컬러 사용 (Purple, Pink)
- 큰 타이포그래피
- 역동적 레이아웃

2. Product Section (전환 구간)
- 컬러 점차 줄임
- 레이아웃 정돈
- 타이포그래피 크기 축소

3. Details Section
- Minimal 스타일 적용
- 같은 컬러 팔레트 유지 (일관성)
- 깔끔한 그리드

이렇게 **점진적 전환**으로 일관성을 유지하면서
두 스타일의 장점을 모두 살릴 수 있습니다."
```

**팁**: 급격한 스타일 변화보다 점진적 전환 추천

---

### 💡 Tip 4: 접근성 체크

모든 스타일 파일에는 접근성 가이드가 포함되어 있습니다:

```markdown
## 컬러 사용 가이드라인

### 접근성 고려
- Navy Blue on Cream: ✅ 8.4:1 (AAA)
- Forest Green on Cream: ✅ 7.2:1 (AAA)
- Gold on Navy: ✅ 4.5:1 (AA)
```

**WCAG 기준**:
- **AA**: 4.5:1 이상 (일반 텍스트)
- **AAA**: 7:1 이상 (가장 엄격)

**Claude에게 요청**:
```
사용자: "모든 텍스트가 AAA 기준을 충족하는지 확인해줘"

Claude:
"접근성 검사 결과:

✅ 주요 텍스트 (Charcoal on Cream): 10.1:1 (AAA)
✅ 제목 (Navy on Cream): 8.4:1 (AAA)
⚠️ CTA 버튼 (Gold on White): 3.8:1 (AA 미만)

CTA 버튼을 수정하겠습니다:
- 변경 전: Gold (#B8860B) on White
- 변경 후: Darker Gold (#8B6508) on White → 4.6:1 (AA)

또는 배경을 Navy로 변경:
- Gold (#B8860B) on Navy (#1E3A5F) → 4.5:1 (AA)"
```

---

### 💡 Tip 5: 실제 코드로 빠르게 변환

```
사용자: "이 디자인을 React + Tailwind CSS로 구현해줘"

Claude:
"Luxury Premium 스타일을 Tailwind CSS로 구현하겠습니다.

// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        charcoal: '#2C2C2C',
        'champagne-gold': '#D4AF37',
        'ivory-cream': '#F8F6F0',
        'warm-gray': '#8B8680',
        burgundy: '#6B2C3E',
      },
      fontFamily: {
        display: ['Playfair Display', 'serif'],
        heading: ['Montserrat', 'sans-serif'],
        body: ['Lora', 'serif'],
      },
      spacing: {
        'xs': '8px',
        's': '16px',
        'm': '24px',
        'l': '40px',
        'xl': '64px',
        'xxl': '120px',
      }
    }
  }
}

// Hero.jsx
export function Hero() {
  return (
    <section className="h-screen bg-ivory-cream flex items-center">
      <div className="container mx-auto px-l">
        <h1 className="font-display text-6xl font-bold text-charcoal mb-m">
          Timeless Excellence
        </h1>
        <p className="font-body text-lg text-charcoal mb-xl max-w-2xl">
          Experience the pinnacle of luxury and craftsmanship
        </p>
        <button className="bg-champagne-gold text-charcoal font-heading
                          px-10 py-4 rounded hover:shadow-lg transition">
          Explore Collection
        </button>
      </div>
    </section>
  )
}

[... 전체 컴포넌트 코드 ...]"
```

**팁**: 각 스타일의 CSS 변수가 미리 정의되어 있어
어떤 프레임워크로든 빠르게 변환 가능

---

## FAQ (자주 묻는 질문)

### Q1: 한 프로젝트에 여러 Skill을 동시에 사용할 수 있나요?

**A**: 네! 예를 들어:
- `detail-page-designer` (상세페이지용)
- `brand-guidelines` (브랜드 일관성용)
- `pptx` (발표 자료용)

모두 동시에 로드 가능합니다. Claude가 상황에 맞게 적절한 Skill을 선택합니다.

---

### Q2: 기존 디자인 시스템(Figma 등)을 Skill로 만들 수 있나요?

**A**: 물론입니다!

1. Figma의 Design Tokens 추출
2. `styles/my-figma-design.md` 파일 생성
3. 컬러, 폰트, 컴포넌트 스타일 옮기기
4. Claude가 Figma 디자인을 코드로 자동 변환 가능

---

### Q3: Skill을 팀원들과 공유하려면?

**A**:
1. **GitHub**: 저장소로 관리 (가장 추천)
2. **Claude.ai 프로젝트**: 팀 멤버 초대
3. **파일 공유**: Dropbox, Google Drive 등

팀 전체가 일관된 디자인을 사용할 수 있습니다.

---

### Q4: 다국어 지원이 가능한가요?

**A**: 가능합니다!

```
사용자: "Luxury Premium 스타일로 일본어 페이지 만들어줘"

Claude:
"일본어 페이지에 최적화된 디자인을 적용하겠습니다:

## 폰트 수정
- Display: Noto Serif JP (일본어 세리프)
- Heading: Noto Sans JP
- Body: Noto Sans JP Regular

## 레이아웃 조정
- 세로쓰기 지원 (writing-mode: vertical-rl)
- 줄간격 조정 (일본어 최적화)

나머지 컬러, UI 요소는 Luxury Premium 유지"
```

---

### Q5: Skill을 계속 업데이트하려면?

**A**:

1. **버전 관리**
```markdown
---
name: detail-page-designer
version: 2.0.0
description: ...
---
```

2. **변경 로그 유지**
```markdown
## Changelog

### v2.0.0 (2024-03-15)
- 새로운 스타일 추가: Retro Vintage
- Luxury Premium 컬러 팔레트 개선
- 접근성 가이드 강화

### v1.0.0 (2024-01-01)
- 초기 릴리스
```

3. **Git으로 관리**
```bash
git tag v2.0.0
git push --tags
```

---

## 마무리

### 이 Skill의 가치

✅ **시간 절약**: 디자인 결정에 시간 낭비 없음
✅ **일관성**: 프로젝트 전체에 일관된 디자인
✅ **전문성**: 검증된 디자인 시스템 활용
✅ **확장성**: 커스터마이징으로 무한 확장
✅ **협업**: 팀 전체가 같은 기준 공유

### 다음 단계

1. ✅ Skill 설치 완료
2. 📖 5가지 스타일 모두 읽어보기
3. 🎨 간단한 프로젝트로 테스트
4. 🔧 필요시 커스터마이징
5. 👥 팀과 공유

### 추가 리소스

- [Claude Skills 공식 문서](https://docs.anthropic.com/claude/docs/skills)
- [디자인 시스템 Best Practices](https://www.designsystems.com)
- [Figma Community](https://www.figma.com/community)

---

**궁금한 점이나 개선 제안이 있다면 언제든 이슈를 열어주세요!**

Happy Designing! 🎨✨
