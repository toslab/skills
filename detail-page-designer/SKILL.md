---
name: detail-page-designer
description: Professional design system toolkit for detail pages (product pages, service descriptions, portfolio pieces). Applies brand colors, typography, mood, and style systematically. Provides 5 pre-defined style systems with complete specifications, or generates custom design systems. Use this skill when designing landing pages, product showcases, service descriptions, or portfolio detail pages that require cohesive visual identity and professional execution.
license: Complete terms in LICENSE.txt
---

# Detail Page Designer Skill

This skill provides comprehensive design systems for creating professional detail pages. Each style includes curated color palettes, typography pairings, layout principles, and distinct mood that resonates with target audiences.

## Purpose

To create detail pages that achieve:
- Consistent brand identity across all elements
- Professional typography with clear hierarchy
- Emotionally resonant color systems
- Clear visual structure and information flow
- User-centered layout and experience

## Usage Instructions

Follow this workflow to design a detail page:

### Step 1: Identify Requirements

Ask the user about:
- **Page type**: Product detail, service description, portfolio piece
- **Target audience**: Demographics, preferences, technical level
- **Brand mood**: Desired emotional response (luxury, modern, energetic, classic, natural)
- **Constraints**: Existing brand colors, fonts, or guidelines

### Step 2: Recommend Style

Based on requirements, recommend the most suitable style(s) from 5 available options. Explain WHY the recommended style fits their needs.

### Step 3: Wait for Selection

**CRITICAL**: Do NOT proceed until the user explicitly confirms their choice. If user is uncertain, ask clarifying questions about their priorities.

### Step 4: Apply the Design System

Once a style is selected:

1. **Read the style file**: Load `styles/{selected-style}.md` completely
2. **Apply ALL elements consistently**:
   - Color system (Primary, Secondary, Neutral, Accent)
   - Typography (Display, Heading, Body, Caption with all specifications)
   - Layout principles (Grid, spacing, section structure)
   - UI components (Buttons, cards, icons, forms)
3. **Verify accessibility**: Ensure WCAG AA compliance (4.5:1 contrast minimum)
4. **Maintain consistency**: Every design decision MUST reference the style guide

## Available Design Styles

5 production-ready design systems are available:

### 1. Luxury Premium
**Core Colors**: Deep Charcoal `#2C2C2C`, Champagne Gold `#D4AF37`, Ivory Cream `#F8F6F0`
**Typography**: Playfair Display (Display), Montserrat (Heading), Lora (Body)
**Mood**: Sophisticated, exclusive, refined
**Best for**: High-end fashion, luxury goods, premium services, upscale hospitality

### 2. Modern Minimal
**Core Colors**: Pure Black `#000000`, Electric Blue `#0066FF`, Pure White `#FFFFFF`
**Typography**: Inter (all levels, weight-based hierarchy)
**Mood**: Clean, efficient, contemporary
**Best for**: SaaS platforms, tech startups, productivity tools, fintech services

### 3. Vibrant Energetic
**Core Colors**: Electric Purple `#6B4FEE`, Hot Pink `#FF3D88`, Sunshine Yellow `#FFD60A`
**Typography**: Poppins (Display/Heading), Inter (Body)
**Mood**: Bold, creative, playful
**Best for**: Entertainment, gaming, youth brands, creative agencies, fitness products

### 4. Elegant Classic
**Core Colors**: Navy Blue `#1E3A5F`, Antique Gold `#B8860B`, Cream `#F7F5F0`
**Typography**: Cormorant Garamond (Display), Libre Baskerville (Heading), Lora (Body)
**Mood**: Timeless, trustworthy, prestigious
**Best for**: Legal services, finance, education, healthcare, established institutions

### 5. Warm Natural
**Core Colors**: Warm Terracotta `#D97757`, Sage Green `#7C9885`, Warm Sand `#E6D5B8`
**Typography**: Fraunces (Display), Karla (Heading), Lora (Body)
**Mood**: Organic, authentic, calming
**Best for**: Organic products, wellness services, natural beauty, sustainable brands, cafes

## Style File Structure

Each style file in `styles/` directory contains a complete design system:

- **Color System**: Primary, Secondary, Neutral, Accent colors with HEX codes, usage guidelines, and accessibility ratios
- **Typography**: Display, Heading, Body, Caption fonts with sizes, weights, line-heights, letter-spacing
- **Layout Principles**: Grid system, spacing scale, section structures
- **UI Components**: Button, card, icon, form element styles with all states
- **Animation Guidelines**: Timing, easing, interaction patterns
- **Accessibility Standards**: WCAG compliance requirements

**Read the selected style file to access complete specifications.**

## Creating Custom Design Systems

If none of the 5 pre-defined styles fit requirements, create a custom system:

1. **Gather requirements**: Brand identity, target audience, competitive landscape, color/font preferences
2. **Generate system**: Follow the same structure as existing style files - define colors, typography, layouts, components
3. **Present for review**: Show the custom system, gather feedback, iterate
4. **Apply after approval**: Use the finalized custom system consistently

## Critical Guidelines

### ✅ MUST DO
- Apply ALL elements from the selected style consistently
- Verify color contrast ratios meet WCAG AA standards (4.5:1 minimum for text)
- Maintain clear typographic hierarchy at all levels
- Design for mobile responsiveness from the start
- Follow spacing rules precisely (use the defined spacing scale)
- Ensure all interactive elements have appropriate states

### ❌ NEVER DO
- Mix elements from different styles on the same page
- Use colors outside the defined palette
- Ignore accessibility requirements
- Add arbitrary decorative elements that conflict with the style
- Use inconsistent spacing (no arbitrary values)
- Compromise the established visual hierarchy

### ⚠️ IMPORTANT PRINCIPLES

**Consistency is paramount**: The design system exists to ensure every element works harmoniously. Trust the system and apply it faithfully.

**Accessibility is non-negotiable**: WCAG AA compliance is the minimum standard. All text must meet contrast requirements.

**Hierarchy must be clear**: Users should instantly understand the relative importance of every element on the page.

## Application Process

### Phase 1: Color System
Apply colors according to the style guide:
- Background: Neutral background color
- Primary headings: Primary color + Display font
- Body text: Neutral text color + Body font
- CTA buttons: Accent color + specified border-radius
- Dividers/cards: Neutral border color

### Phase 2: Typography
Apply typography hierarchy exactly as specified:
- H1: Display font, 48-64px, Bold weight
- H2: Heading font, 32-40px, Semi-Bold weight
- H3: Heading font, 24-28px, Medium weight
- Body: Body font, 16-18px, Regular weight, line-height 1.6
- Caption: Caption font, 12-14px, Regular weight

### Phase 3: Layout Structure
Build sections in this order:
- Hero: Full-width visual + concise headline + CTA
- Description: Alternating image-text blocks
- Features: Icon grid or card layout
- CTA: Clear call-to-action section
- Footer: Secondary information

### Phase 4: Component Details
Style components according to the guide:
- Buttons: Follow exact specifications for size, color, states
- Cards: Apply consistent shadow, padding, border-radius
- Images: Use uniform border-radius, filters
- Icons: Maintain unified style and sizing

## File Resources

```
styles/
├── luxury-premium.md        # Sophisticated high-end design system
├── modern-minimal.md        # Clean contemporary design system
├── vibrant-energetic.md     # Bold dynamic design system
├── elegant-classic.md       # Timeless traditional design system
└── warm-natural.md          # Organic comfortable design system
```

Each file contains a complete, production-ready design system.

## Technical Implementation

### Web Development
- Define all colors as CSS variables
- Optimize web font loading (preload, font-display: swap)
- Use responsive typography scales
- Build component-based design system

### Design Tools (Figma/Sketch)
- Create color styles for entire palette
- Define text styles for all typography levels
- Build component library with variants
- Create reusable layout templates

## Example Scenarios

### Scenario 1: Premium Headphones
**Product**: High-end noise-cancelling headphones, 30-50 age group
**Recommendation**: Luxury Premium (best fit) or Modern Minimal
**User selects**: Luxury Premium
**Application**: Deep Charcoal + Gold accents + Cream background, Playfair Display + Montserrat + Lora, large product imagery with generous spacing, sophisticated and refined mood

### Scenario 2: Meditation App
**Product**: Wellness app for stress reduction, broad audience
**Recommendation**: Warm Natural (best fit) or Elegant Classic
**User selects**: Warm Natural
**Application**: Sage Green + Terracotta + Sand, Fraunces + Karla + Lora, organic shapes with rounded corners, calm and healing mood

## Quality Checklist

Before finalizing, verify:

- [ ] Clear visual hierarchy (primary, secondary, tertiary elements distinct)
- [ ] Consistent color application (palette followed throughout)
- [ ] Readable typography (appropriate sizes, weights, spacing)
- [ ] Adequate spacing (no cramped sections)
- [ ] Brand identity reflected (mood appropriate)
- [ ] Mobile optimization (responsive breakpoints working)
- [ ] Fast performance (optimized assets)
- [ ] Clear CTAs (prominent and obvious)
- [ ] Accessibility compliance (WCAG AA minimum)
- [ ] Consistent mood and tone (style guide followed faithfully)

---

**Note**: This skill provides design systems and guidelines. Implementation requires HTML/CSS, Figma, Sketch, or other design/development tools.
