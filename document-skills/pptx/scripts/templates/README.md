# PPTX Templates

이 디렉토리는 PowerPoint 프레젠테이션 생성 시 재사용 가능한 템플릿을 저장합니다.

## 디렉토리 구조

```
templates/
├── presentations/           # 전체 프레젠테이션 템플릿
│   ├── corporate.pptx
│   ├── minimal.pptx
│   └── creative.pptx
│
├── slides/                  # 개별 슬라이드 템플릿
│   ├── title-slides/       # 타이틀 슬라이드
│   ├── content-slides/     # 콘텐츠 슬라이드
│   └── closing-slides/     # 마무리 슬라이드
│
└── images/                  # 이미지 에셋
    ├── backgrounds/        # 배경 이미지 (canvas-design 출력 가능)
    ├── icons/              # 아이콘
    └── charts/             # 차트 이미지
```

## Canvas-Design 통합

Canvas-design에서 생성한 PNG를 슬라이드 배경으로 사용:

```bash
# Canvas-design 배경 복사
cp /workspace/slide-bg-*.png images/backgrounds/
```

## 사용 예시

```javascript
// html2pptx 사용
const pptx = new PptxGenJS();

const slide = pptx.addSlide();

// Templates 배경 이미지 사용
slide.background = { path: 'templates/images/backgrounds/abstract-bg.png' };

slide.addText('Title', { x: 1, y: 1, fontSize: 44 });

pptx.writeFile('presentation.pptx');
```
