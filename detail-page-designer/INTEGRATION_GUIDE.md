# Detail Page Designer + Canva MCP Integration Guide

## Overview

This guide explains how to use the detail-page-designer skill together with Canva MCP to create editable, professional designs.

## Workflow

### Step 1: Use Detail Page Designer Skill

**User request**:
```
"Create a detail page for premium furniture products"
```

**Claude using the skill**:
1. Identifies requirements (luxury product, 30-50 age group)
2. Recommends style: Luxury Premium
3. User selects: Luxury Premium
4. Loads `styles/luxury-premium.md`
5. Generates design specifications:

```markdown
**Design Specifications for Canva**

Colors:
- Background: #F8F6F0 (Ivory Cream)
- Primary Text: #2C2C2C (Deep Charcoal)
- Accent: #D4AF37 (Champagne Gold)
- Secondary: #6B2C3E (Deep Burgundy)

Typography:
- Headline: Playfair Display Bold, 64px
- Subheading: Montserrat SemiBold, 32px
- Body: Lora Regular, 18px

Layout:
- Hero section: Full width, product image + headline
- Features: 3-column grid
- CTA: Centered, gold button
```

### Step 2: Use Canva MCP to Create Design

**If Canva MCP is available**, Claude can directly:

```javascript
// Using Canva MCP tools
mcp__canva__create_design({
  title: "Premium Furniture Detail Page",
  type: "presentation", // or "social-media-post", "document"
  pages: [
    {
      elements: [
        {
          type: "text",
          content: "Timeless Elegance",
          font: "Playfair Display",
          fontSize: 64,
          fontWeight: "bold",
          color: "#2C2C2C",
          position: { x: 100, y: 100 }
        },
        {
          type: "rectangle",
          width: 300,
          height: 60,
          fill: "#D4AF37",
          position: { x: 100, y: 500 },
          text: {
            content: "SHOP NOW",
            font: "Montserrat",
            fontSize: 16,
            color: "#2C2C2C"
          }
        },
        {
          type: "image",
          url: "product-image.jpg",
          width: 500,
          height: 500,
          position: { x: 600, y: 100 }
        }
      ],
      background: "#F8F6F0"
    }
  ]
})
```

**Result**:
- ✅ Editable Canva design created
- ✅ User gets shareable link
- ✅ Can edit in Canva web interface

### Step 3: User Edits in Canva

User receives:
- Direct link to Canva design
- All elements are editable:
  - Change text content
  - Adjust colors (within palette)
  - Move elements
  - Add/remove sections
- Download in various formats (PNG, PDF, etc.)

## Benefits of This Integration

### 1. **Design System Consistency**
- Detail Page Designer ensures professional color/font choices
- Canva MCP implements them exactly

### 2. **Editable Output**
- Unlike static images, Canva designs are fully editable
- User can iterate without Claude

### 3. **Professional Templates**
- Each of 5 styles becomes a Canva template
- Reusable for future projects

### 4. **Speed**
- From concept to editable design in minutes
- No manual Canva setup needed

## Setting Up Canva MCP

### Prerequisites

1. **Canva Account**: Free or Pro
2. **Canva API Key**: Get from Canva Developer Portal
3. **MCP Configuration**: Add to Claude config

### Installation

1. **Install Canva MCP Server**:
```bash
npm install -g @modelcontextprotocol/server-canva
# or
pip install canva-mcp-server
```

2. **Configure in Claude**:

Edit `~/.config/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "canva": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-canva"],
      "env": {
        "CANVA_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

3. **Restart Claude**

### Verification

Ask Claude:
```
"Can you use Canva MCP? List available tools."
```

Expected response:
- mcp__canva__create_design
- mcp__canva__get_design
- mcp__canva__update_design
- mcp__canva__export_design

## Example Use Cases

### Use Case 1: Product Launch Page

**User**:
```
"Create a product launch page for our new smartwatch using Modern Minimal style"
```

**Claude workflow**:
1. Loads `modern-minimal.md`
2. Extracts colors: Black #000000, Blue #0066FF, White #FFFFFF
3. Extracts fonts: Inter (all levels)
4. Creates Canva design with:
   - Hero: Smartwatch image + "Innovation Simplified"
   - Features: 3-column grid with icons
   - CTA: Blue button "Pre-order Now"
5. Returns editable Canva link

**User gets**:
- Professional design in 2 minutes
- Can edit text, swap images
- Download for web/print

### Use Case 2: A/B Testing Landing Pages

**User**:
```
"Create two versions: one with Luxury Premium style, one with Vibrant Energetic"
```

**Claude creates**:
- **Version A**: Luxury Premium (gold, charcoal, elegant)
- **Version B**: Vibrant Energetic (purple, pink, bold)
- Both editable in Canva
- User can test which converts better

### Use Case 3: Brand Consistency

**User**:
```
"Create 5 product pages for our skincare line, all using Warm Natural style"
```

**Claude**:
1. Loads `warm-natural.md` once
2. Creates 5 Canva designs with same:
   - Colors: Terracotta, Sage, Sand
   - Fonts: Fraunces, Karla, Lora
   - Layout: Consistent structure
3. Each product gets its own editable design
4. Brand consistency guaranteed

## Advanced: Custom Style + Canva

**User has specific brand colors**:
```
"Create a custom style with our brand colors: #FF5733, #33FF57, #3357FF
Then make a Canva design"
```

**Claude**:
1. Uses detail-page-designer to create custom style
2. Validates color accessibility (WCAG AA)
3. Suggests font pairings
4. Creates Canva template with custom style
5. User approves and gets editable design

## Technical Implementation

### Skill Enhancement for MCP Integration

You can enhance `SKILL.md` with MCP-specific instructions:

```markdown
## Using with Canva MCP

If Canva MCP is available, apply the design system directly:

1. Read the selected style file completely
2. Extract color palette, typography, layout specs
3. Use `mcp__canva__create_design` with:
   - Colors from style guide
   - Fonts from typography section
   - Layout from section structure
4. Return editable Canva link to user
```

### Code Example

```python
# Pseudo-code for integration

def create_detail_page_with_canva(style_name):
    # Step 1: Load design system
    style = read_file(f"styles/{style_name}.md")
    colors = extract_colors(style)
    fonts = extract_fonts(style)
    layout = extract_layout(style)

    # Step 2: Create Canva design
    design = canva_mcp.create_design({
        "title": f"Detail Page - {style_name}",
        "pages": build_pages(colors, fonts, layout)
    })

    # Step 3: Return editable link
    return design.edit_url
```

## Comparison: With vs Without Canva MCP

### Without Canva MCP
```
User request
  ↓
Claude provides:
  - Color codes (#2C2C2C, #D4AF37...)
  - Font names (Playfair Display...)
  - Layout description (text)
  ↓
User manually:
  - Opens Canva
  - Inputs colors
  - Selects fonts
  - Arranges layout
  ↓
Time: 30-60 minutes
```

### With Canva MCP
```
User request
  ↓
Claude:
  - Loads design system
  - Creates Canva design automatically
  - Returns edit link
  ↓
User:
  - Opens link
  - Design already matches style
  - Makes minor tweaks
  ↓
Time: 2-5 minutes
```

## Limitations & Considerations

### Font Availability
- Not all fonts in style guides may be in Canva
- Fallback fonts should be suggested
- Example: Playfair Display → Canva's "Libre Baskerville"

### Canva API Limits
- Free accounts: Limited API calls
- Pro accounts: Higher limits
- Consider caching designs

### Complex Layouts
- Very intricate designs may need manual adjustment
- Canva MCP best for structured layouts
- Detail page designs are well-suited (grid-based)

## Best Practices

### 1. Start with Style Selection
Always use detail-page-designer first to ensure:
- Professional color choices
- Appropriate typography
- Consistent brand identity

### 2. Provide Context
Give Claude information:
- Target audience
- Product/service details
- Preferred imagery

### 3. Iterate
Use Canva's edit link to:
- Swap images
- Adjust copy
- Fine-tune spacing

### 4. Export Appropriately
- Web: PNG (optimized)
- Print: PDF (high-res)
- Social: Platform-specific sizes

## Troubleshooting

### Issue: "Canva MCP not found"
**Solution**:
1. Install MCP server
2. Configure claude_desktop_config.json
3. Restart Claude

### Issue: "Font not available in Canva"
**Solution**:
Claude will suggest closest Canva alternative:
- Playfair Display → Libre Baskerville
- Montserrat → Poppins
- Inter → Roboto

### Issue: "Colors don't match exactly"
**Solution**:
Canva uses HEX codes, should match perfectly.
If not, manually adjust in Canva editor.

## Future Enhancements

### Planned Features
1. **Template Library**: Save successful designs as templates
2. **Batch Generation**: Create multiple variations at once
3. **Brand Kit Integration**: Store custom styles in Canva Brand Kit
4. **A/B Test Exports**: Generate comparison PDFs

## Resources

- [Canva Developers](https://www.canva.com/developers/)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Detail Page Designer Skill](./SKILL.md)
- [Style Files](./styles/)

## Example Session

**Full conversation using both tools**:

```
User: "I need a landing page for our organic coffee brand"

Claude: "I recommend the Warm Natural style for organic products.
Let me create a design using:
- Colors: Terracotta #D97757, Sage #7C9885, Sand #E6D5B8
- Fonts: Fraunces (headlines), Karla (body)
- Mood: Organic, authentic, calming

Creating Canva design now..."

[Uses Canva MCP to create design]

Claude: "✅ Design created! Here's your editable link:
https://canva.com/design/abc123

The page includes:
- Hero with coffee beans image
- '100% Organic. 100% Delicious.' headline
- 3 feature cards (Sustainably sourced, Fair trade, Small batch)
- Warm earth tone color palette
- CTA button in terracotta

You can edit everything directly in Canva!"

User: "Perfect! Can I change the headline?"

Claude: "Absolutely! Just click the headline text in the Canva
editor and type your new text. The font and colors will stay
the same, maintaining the Warm Natural style."
```

---

**This integration transforms detail-page-designer from a guide into a production tool!**
