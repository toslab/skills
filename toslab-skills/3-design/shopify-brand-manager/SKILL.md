---
name: shopify-brand-manager
description: |
  Comprehensive brand management toolkit for Shopify stores. Applies brand identity
  (colors, typography, logos, brand story) to Shopify themes programmatically.

  Claude should use this skill when users want to:
  - Apply brand guidelines to Shopify store
  - Update Shopify theme with brand colors and fonts
  - Upload brand assets (logos, images) to Shopify
  - Manage brand consistency across Shopify store
  - Set up brand metafields and theme settings
  - Customize Shopify theme with brand identity

  Requires Shopify Admin API credentials.

  Trigger phrases: "Shopify에 브랜드 적용", "브랜드 색상 업데이트", "Shopify 테마 커스터마이징",
  "브랜드 자산 업로드", "Shopify 브랜드 관리"

  Keywords: Shopify, brand, branding, theme, colors, logo, typography, CSS variables,
  metafields, brand identity, store customization
allowed-tools: [Bash, Read, Write, Edit]
---

# Shopify Brand Manager

## Overview

To apply brand identity to Shopify stores systematically and consistently, use this skill.
Manages brand assets, colors, typography, and brand story across your Shopify store.

**What this skill does:**
- Converts brand configuration to Shopify-compatible formats
- Uploads brand assets (logos, images, fonts)
- Generates CSS variables for consistent styling
- Sets brand metafields for programmatic access
- Updates theme settings with brand colors
- Creates reusable Liquid snippets

## Prerequisites

### 1. Shopify API Credentials

To use this skill, obtain Shopify Admin API credentials:

1. **Go to Shopify Admin** → Apps → "Develop apps"
2. **Create new app** (or use existing)
3. **Configure Admin API scopes:**
   - `read_themes` - Read theme files
   - `write_themes` - Modify theme files
   - `read_products` - Read products
   - `write_products` - Update products
   - `read_content` - Read metafields
   - `write_content` - Write metafields

4. **Install app and get Access Token**
5. **Set environment variables:**

```bash
export SHOPIFY_STORE_URL="your-store.myshopify.com"
export SHOPIFY_ACCESS_TOKEN="shpat_xxxxx..."
```

### 2. Brand Assets

Ensure you have:
- `assets/brand/brand-config.json` - Brand configuration file
- `assets/brand/brand-story.md` - Brand story and guidelines
- `assets/images/` - Logo and image files

## Workflow

### Decision Tree

```
User wants to apply brand to Shopify?
  │
  ├─ First time setup?
  │  └─ 1. Configure brand assets
  │     2. Test connection
  │     3. Apply brand (--full)
  │
  ├─ Update colors/fonts only?
  │  └─ Apply CSS variables only
  │
  ├─ Upload new assets?
  │  └─ Upload assets only
  │
  └─ Complete update?
     └─ Apply everything
```

## Step-by-Step Guide

### Step 1: Configure Brand Assets

#### 1.1 Edit `assets/brand/brand-config.json`

**Update brand information:**

```json
{
  "brand": {
    "name": "Your Brand Name",
    "tagline": "Your tagline",
    "version": "1.0.0"
  },
  "colors": {
    "primary": {
      "name": "Brand Blue",
      "hex": "#0066CC",
      "usage": "Main CTA buttons, links"
    },
    "secondary": {
      "name": "Brand Orange",
      "hex": "#FF6B35",
      "usage": "Accents, highlights"
    }
  },
  "typography": {
    "headings": {
      "family": "Your Heading Font",
      "weights": [400, 600, 700],
      "fallback": "sans-serif"
    },
    "body": {
      "family": "Your Body Font",
      "weights": [400, 500],
      "fallback": "sans-serif"
    }
  }
}
```

**Key sections to customize:**
- `brand.name` - Your brand name
- `brand.tagline` - Brand tagline
- `colors.primary` - Primary brand color
- `colors.secondary` - Secondary brand color
- `typography.headings.family` - Heading font name
- `typography.body.family` - Body font name

#### 1.2 Edit `assets/brand/brand-story.md`

Update with your brand story:
- Brand values
- Brand voice and tone
- Visual identity guidelines
- Customer experience principles

#### 1.3 Add Brand Assets

Place files in appropriate folders:

```
assets/
├── images/
│   ├── toslab-logo.svg         # Primary logo
│   ├── toslab-logo-white.svg   # White version
│   ├── toslab-icon.svg         # Icon/favicon
│   ├── hero-bg.jpg             # Hero background
│   └── placeholder.jpg         # Placeholder image
└── brand/
    ├── brand-config.json       # Configuration
    └── brand-story.md          # Brand story
```

**Supported formats:**
- **Logos**: SVG (recommended), PNG
- **Images**: JPG, PNG, WebP
- **Fonts**: WOFF, WOFF2, TTF

### Step 2: Test Connection

Before applying changes, test Shopify connection:

```bash
python scripts/shopify_client.py
```

**Expected output:**
```
✅ Connected to Shopify store: Your Store Name
   URL: your-store.myshopify.com
   Email: your-email@example.com
```

**If connection fails:**
1. Check environment variables are set correctly
2. Verify access token has required scopes
3. Confirm store URL format (no https://)

### Step 3: Preview Changes (Dry Run)

Preview what will be applied without making changes:

```bash
python scripts/apply_brand_to_shopify.py --full --dry-run
```

**Review output:**
- CSS variables that will be created
- Assets that will be uploaded
- Metafields that will be set
- Theme settings that will be updated

### Step 4: Apply Brand to Shopify

#### 4.1 Apply CSS Variables Only (Quick Update)

To update only colors and typography:

```bash
python scripts/apply_brand_to_shopify.py --css-only
```

**What this does:**
1. Generates CSS variables from brand-config.json
2. Uploads `brand-variables.css` to theme
3. Creates Liquid snippet for easy inclusion

**Result:**
- File created: `assets/brand-variables.css`
- Snippet created: `snippets/brand-variables.liquid`

#### 4.2 Upload Brand Assets Only

To upload logos and images:

```bash
python scripts/apply_brand_to_shopify.py --assets-only
```

**What this does:**
1. Uploads all images from `assets/images/`
2. Converts to appropriate formats
3. Places in theme assets folder

**Result:**
- Logos available at: `assets/brand-primary.svg`, etc.
- Images available at: `assets/brand-hero.jpg`, etc.

#### 4.3 Full Brand Application (Recommended)

To apply everything:

```bash
python scripts/apply_brand_to_shopify.py --full
```

**What this does:**
1. ✅ Generates and uploads CSS variables
2. ✅ Uploads all brand assets
3. ✅ Sets shop-level metafields with brand info
4. ✅ Updates theme settings with brand colors
5. ✅ Creates Liquid snippet for easy access

**Result:**
Complete brand integration across Shopify store.

#### 4.4 Target Specific Theme

To apply to a specific theme (not main):

```bash
python scripts/apply_brand_to_shopify.py --theme-id 123456789 --full
```

### Step 5: Integrate into Theme

#### 5.1 Add to theme.liquid

Edit your theme's `theme.liquid` file and add:

```liquid
<!-- Add in <head> section -->
{% render 'brand-variables' %}
```

This loads:
- CSS variables stylesheet
- Brand constants for use in Liquid

#### 5.2 Use CSS Variables in Theme

**In CSS/SCSS files:**

```css
/* Use brand colors */
.button-primary {
  background-color: var(--brand-primary);
  color: white;
}

.button-secondary {
  background-color: var(--brand-secondary);
  color: white;
}

/* Use brand typography */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
}

body {
  font-family: var(--font-body);
  font-size: var(--font-size-body);
  line-height: var(--line-height-normal);
}

/* Use brand spacing */
.section {
  padding: var(--spacing-xl) var(--spacing-md);
}

/* Use brand border radius */
.card {
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
}
```

**In Liquid templates:**

```liquid
<!-- Use brand variables -->
<div style="background-color: {{ settings.brand_primary }}">
  <h1>{{ brand_name }}</h1>
  <p>{{ brand_tagline }}</p>
</div>

<!-- Access brand metafields -->
{% assign brand_story = shop.metafields.toslab_brand.brand_story %}
<div class="brand-story">
  {{ brand_story }}
</div>
```

## Available CSS Variables

After applying brand, these variables are available:

### Colors
```css
--brand-primary          /* Primary brand color */
--brand-primary-rgb      /* Primary color as RGB */
--brand-secondary        /* Secondary brand color */
--brand-secondary-rgb    /* Secondary color as RGB */
--brand-accent           /* Accent color */
--brand-dark            /* Dark neutral */
--brand-medium          /* Medium neutral */
--brand-light           /* Light neutral */
--brand-white           /* White */
--brand-success         /* Success state */
--brand-warning         /* Warning state */
--brand-error           /* Error state */
```

### Typography
```css
--font-heading          /* Heading font family */
--font-body             /* Body font family */
--font-mono             /* Monospace font */
--font-size-h1          /* H1 size */
--font-size-h2          /* H2 size */
--font-size-body        /* Body size */
--line-height-tight     /* Tight line height */
--line-height-normal    /* Normal line height */
```

### Spacing
```css
--spacing-xs    /* 4px */
--spacing-sm    /* 8px */
--spacing-md    /* 16px */
--spacing-lg    /* 24px */
--spacing-xl    /* 32px */
--spacing-2xl   /* 48px */
```

### Other
```css
--radius-sm     /* Small border radius */
--radius-md     /* Medium border radius */
--shadow-sm     /* Small shadow */
--shadow-md     /* Medium shadow */
```

## Common Use Cases

### Use Case 1: Seasonal Color Update

**Scenario:** Update brand colors for seasonal campaign

```bash
# 1. Edit brand-config.json
# Update colors.primary.hex to seasonal color

# 2. Apply CSS update
python scripts/apply_brand_to_shopify.py --css-only

# 3. Changes are live immediately
```

### Use Case 2: New Logo Upload

**Scenario:** Company rebranded with new logo

```bash
# 1. Replace logo files in assets/images/
cp new-logo.svg assets/images/toslab-logo.svg

# 2. Upload new assets
python scripts/apply_brand_to_shopify.py --assets-only

# 3. Logo available at {{ 'brand-primary.svg' | asset_url }}
```

### Use Case 3: Complete Brand Refresh

**Scenario:** Full rebrand - colors, fonts, assets, everything

```bash
# 1. Update brand-config.json with all new values
# 2. Replace all assets in assets/images/
# 3. Update brand-story.md

# 4. Apply everything
python scripts/apply_brand_to_shopify.py --full

# 5. Verify in theme editor
```

### Use Case 4: Multi-Store Brand Deployment

**Scenario:** Apply same brand to multiple Shopify stores

```bash
# For each store:

# Store 1
export SHOPIFY_STORE_URL="store1.myshopify.com"
export SHOPIFY_ACCESS_TOKEN="token1"
python scripts/apply_brand_to_shopify.py --full

# Store 2
export SHOPIFY_STORE_URL="store2.myshopify.com"
export SHOPIFY_ACCESS_TOKEN="token2"
python scripts/apply_brand_to_shopify.py --full
```

## Advanced Features

### Generate CSS Variables Standalone

Generate CSS file without uploading:

```bash
python scripts/generate_css_variables.py \
  --config ../assets/brand/brand-config.json \
  --output brand-variables.css
```

**Use cases:**
- Preview CSS before uploading
- Use in non-Shopify projects
- Version control for CSS

### Generate Shopify Settings Schema

Create settings schema for theme customizer:

```bash
python scripts/generate_css_variables.py \
  --settings-schema \
  --output settings_schema.json
```

**Result:**
Shopify theme settings that appear in theme editor for easy color customization.

### Access Brand Data Programmatically

**In Python scripts:**

```python
from shopify_client import load_brand_config

# Load brand config
config = load_brand_config()

# Access brand data
primary_color = config['colors']['primary']['hex']
brand_name = config['brand']['name']
```

**In Liquid:**

```liquid
{% assign brand_config = shop.metafields.toslab_brand.brand_config %}
{% assign primary = brand_config.colors.primary.hex %}
```

## Troubleshooting

### "Authentication failed"

**Problem:** Cannot connect to Shopify API

**Solutions:**
1. Check environment variables:
   ```bash
   echo $SHOPIFY_STORE_URL
   echo $SHOPIFY_ACCESS_TOKEN
   ```
2. Verify access token has not expired
3. Confirm API scopes include `read_themes` and `write_themes`

### "Theme not found"

**Problem:** Specified theme ID doesn't exist

**Solutions:**
1. List all themes:
   ```python
   from shopify_client import ShopifyBrandClient
   client = ShopifyBrandClient()
   themes = client.get_themes()
   for theme in themes:
       print(f"{theme['name']}: {theme['id']}")
   ```
2. Use correct theme ID or omit to use main theme

### "Asset upload failed"

**Problem:** Cannot upload brand assets

**Solutions:**
1. Check file exists and path is correct
2. Verify file format is supported
3. Ensure file size is under Shopify limit (5MB)
4. Try uploading manually first to test

### "CSS variables not applied"

**Problem:** CSS variables not showing in store

**Solutions:**
1. Verify `{% render 'brand-variables' %}` is in theme.liquid
2. Clear browser cache and Shopify cache
3. Check CSS file was uploaded:
   ```bash
   # Verify in theme editor → Assets → brand-variables.css
   ```
4. Inspect element to see if CSS is loaded

## Best Practices

### 1. Version Control for Brand Config

Keep brand-config.json in version control:

```bash
git add assets/brand/brand-config.json
git commit -m "Update brand colors for summer campaign"
```

### 2. Test on Development Theme First

```bash
# Get development theme ID
python scripts/shopify_client.py

# Apply to dev theme first
python scripts/apply_brand_to_shopify.py \
  --theme-id DEV_THEME_ID \
  --full

# Test thoroughly, then apply to main theme
```

### 3. Use Dry Run for Major Changes

Always preview before applying:

```bash
python scripts/apply_brand_to_shopify.py --full --dry-run
```

### 4. Document Custom Colors

In brand-config.json, always include `usage` field:

```json
{
  "primary": {
    "hex": "#0066CC",
    "usage": "CTA buttons, primary links, main navigation"
  }
}
```

### 5. Keep Brand Story Updated

Regularly update brand-story.md:
- Reflect current brand values
- Update messaging guidelines
- Add new use cases

## References

### Scripts
- `scripts/shopify_client.py` - Shopify API client
- `scripts/apply_brand_to_shopify.py` - Main application script
- `scripts/generate_css_variables.py` - CSS variable generator

### Assets
- `assets/brand/brand-config.json` - Brand configuration
- `assets/brand/brand-story.md` - Brand story and guidelines
- `assets/images/` - Brand image assets

### Documentation
- [Shopify Admin API](https://shopify.dev/docs/api/admin)
- [Shopify Themes](https://shopify.dev/docs/themes)
- [Liquid](https://shopify.dev/docs/themes/liquid)

## Support

For issues or questions:
1. Check this SKILL.md first
2. Review error messages carefully
3. Test connection with `shopify_client.py`
4. Try dry run mode to debug
5. Check Shopify API status
