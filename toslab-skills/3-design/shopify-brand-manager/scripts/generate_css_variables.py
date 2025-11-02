#!/usr/bin/env python3
"""
Generate CSS variables from brand configuration

Converts brand-config.json to CSS custom properties that can be used
in Shopify theme templates.

Usage:
    python generate_css_variables.py
    python generate_css_variables.py --output custom.css
    python generate_css_variables.py --format liquid
"""

import json
import argparse
from pathlib import Path
from typing import Dict


def hex_to_rgb(hex_color: str) -> str:
    """
    Convert hex color to RGB values

    Args:
        hex_color: Hex color code (e.g., "#0066CC")

    Returns:
        RGB values as string (e.g., "0, 102, 204")
    """
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"{r}, {g}, {b}"


def generate_css_variables(brand_config: Dict, format: str = 'css') -> str:
    """
    Generate CSS variables from brand configuration

    Args:
        brand_config: Brand configuration dictionary
        format: Output format ('css' or 'liquid')

    Returns:
        CSS variables as string
    """
    lines = []

    if format == 'liquid':
        lines.append("{% comment %}")
        lines.append("  Brand Variables - Auto-generated from brand-config.json")
        lines.append("  DO NOT EDIT MANUALLY - Changes will be overwritten")
        lines.append("{% endcomment %}")
        lines.append("")

    lines.append(":root {")
    lines.append("  /* ==================== */")
    lines.append("  /* Brand Colors         */")
    lines.append("  /* ==================== */")
    lines.append("")

    # Primary color
    if 'colors' in brand_config and 'primary' in brand_config['colors']:
        primary = brand_config['colors']['primary']
        lines.append(f"  /* {primary.get('name', 'Primary')} */")
        lines.append(f"  --brand-primary: {primary['hex']};")
        lines.append(f"  --brand-primary-rgb: {primary.get('rgb', hex_to_rgb(primary['hex']))};")
        lines.append("")

    # Secondary color
    if 'colors' in brand_config and 'secondary' in brand_config['colors']:
        secondary = brand_config['colors']['secondary']
        lines.append(f"  /* {secondary.get('name', 'Secondary')} */")
        lines.append(f"  --brand-secondary: {secondary['hex']};")
        lines.append(f"  --brand-secondary-rgb: {secondary.get('rgb', hex_to_rgb(secondary['hex']))};")
        lines.append("")

    # Accent color
    if 'colors' in brand_config and 'accent' in brand_config['colors']:
        accent = brand_config['colors']['accent']
        lines.append(f"  /* {accent.get('name', 'Accent')} */")
        lines.append(f"  --brand-accent: {accent['hex']};")
        lines.append(f"  --brand-accent-rgb: {accent.get('rgb', hex_to_rgb(accent['hex']))};")
        lines.append("")

    # Neutral colors
    if 'colors' in brand_config and 'neutral' in brand_config['colors']:
        lines.append("  /* Neutral Colors */")
        neutral = brand_config['colors']['neutral']
        for name, color in neutral.items():
            if isinstance(color, dict):
                lines.append(f"  --brand-{name}: {color['hex']};")
                lines.append(f"  --brand-{name}-rgb: {color.get('rgb', hex_to_rgb(color['hex']))};")
        lines.append("")

    # Semantic colors
    if 'colors' in brand_config and 'semantic' in brand_config['colors']:
        lines.append("  /* Semantic Colors */")
        semantic = brand_config['colors']['semantic']
        for name, hex_color in semantic.items():
            lines.append(f"  --brand-{name}: {hex_color};")
            lines.append(f"  --brand-{name}-rgb: {hex_to_rgb(hex_color)};")
        lines.append("")

    # Typography
    lines.append("  /* ==================== */")
    lines.append("  /* Typography           */")
    lines.append("  /* ==================== */")
    lines.append("")

    if 'typography' in brand_config:
        typography = brand_config['typography']

        # Font families
        if 'headings' in typography:
            headings = typography['headings']
            lines.append(f"  --font-heading: '{headings['family']}', {headings['fallback']};")

        if 'body' in typography:
            body = typography['body']
            lines.append(f"  --font-body: '{body['family']}', {body['fallback']};")

        if 'monospace' in typography:
            mono = typography['monospace']
            lines.append(f"  --font-mono: '{mono['family']}', {mono['fallback']};")

        lines.append("")

        # Font sizes
        if 'sizes' in typography:
            lines.append("  /* Font Sizes */")
            for size_name, size_value in typography['sizes'].items():
                lines.append(f"  --font-size-{size_name}: {size_value};")
            lines.append("")

        # Line heights
        if 'lineHeights' in typography:
            lines.append("  /* Line Heights */")
            for lh_name, lh_value in typography['lineHeights'].items():
                lines.append(f"  --line-height-{lh_name}: {lh_value};")
            lines.append("")

    # Spacing
    if 'spacing' in brand_config and 'values' in brand_config['spacing']:
        lines.append("  /* ==================== */")
        lines.append("  /* Spacing              */")
        lines.append("  /* ==================== */")
        lines.append("")
        for space_name, space_value in brand_config['spacing']['values'].items():
            lines.append(f"  --spacing-{space_name}: {space_value};")
        lines.append("")

    # Border radius
    if 'borderRadius' in brand_config:
        lines.append("  /* ==================== */")
        lines.append("  /* Border Radius        */")
        lines.append("  /* ==================== */")
        lines.append("")
        for radius_name, radius_value in brand_config['borderRadius'].items():
            lines.append(f"  --radius-{radius_name}: {radius_value};")
        lines.append("")

    # Shadows
    if 'shadows' in brand_config:
        lines.append("  /* ==================== */")
        lines.append("  /* Shadows              */")
        lines.append("  /* ==================== */")
        lines.append("")
        for shadow_name, shadow_value in brand_config['shadows'].items():
            lines.append(f"  --shadow-{shadow_name}: {shadow_value};")
        lines.append("")

    lines.append("}")

    return "\n".join(lines)


def generate_shopify_settings_schema(brand_config: Dict) -> str:
    """
    Generate Shopify theme settings schema for brand colors

    Args:
        brand_config: Brand configuration dictionary

    Returns:
        JSON schema for theme settings
    """
    schema = [
        {
            "name": "theme_info",
            "theme_name": brand_config.get('brand', {}).get('name', 'Brand Theme'),
            "theme_version": brand_config.get('brand', {}).get('version', '1.0.0'),
            "theme_author": brand_config.get('brand', {}).get('name', 'toslab'),
            "theme_documentation_url": "",
            "theme_support_url": ""
        },
        {
            "name": "Brand Colors",
            "settings": []
        }
    ]

    colors = brand_config.get('colors', {})

    # Primary color
    if 'primary' in colors:
        schema[1]['settings'].append({
            "type": "color",
            "id": "brand_primary",
            "label": colors['primary'].get('name', 'Primary Color'),
            "default": colors['primary']['hex'],
            "info": colors['primary'].get('usage', '')
        })

    # Secondary color
    if 'secondary' in colors:
        schema[1]['settings'].append({
            "type": "color",
            "id": "brand_secondary",
            "label": colors['secondary'].get('name', 'Secondary Color'),
            "default": colors['secondary']['hex'],
            "info": colors['secondary'].get('usage', '')
        })

    # Accent color
    if 'accent' in colors:
        schema[1]['settings'].append({
            "type": "color",
            "id": "brand_accent",
            "label": colors['accent'].get('name', 'Accent Color'),
            "default": colors['accent']['hex'],
            "info": colors['accent'].get('usage', '')
        })

    return json.dumps(schema, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description='Generate CSS variables from brand configuration'
    )
    parser.add_argument(
        '--config',
        default='../assets/brand/brand-config.json',
        help='Path to brand-config.json'
    )
    parser.add_argument(
        '--output',
        default='../assets/templates/brand-variables.css',
        help='Output CSS file path'
    )
    parser.add_argument(
        '--format',
        choices=['css', 'liquid'],
        default='css',
        help='Output format (css or liquid)'
    )
    parser.add_argument(
        '--settings-schema',
        action='store_true',
        help='Also generate Shopify settings schema'
    )

    args = parser.parse_args()

    # Load brand configuration
    script_dir = Path(__file__).parent
    config_path = script_dir / args.config
    output_path = script_dir / args.output

    print(f"📖 Loading brand config from: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        brand_config = json.load(f)

    # Generate CSS variables
    print(f"🎨 Generating CSS variables...")
    css_content = generate_css_variables(brand_config, args.format)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

    print(f"✅ CSS variables written to: {output_path}")
    print(f"   {len(css_content.splitlines())} lines generated")

    # Generate settings schema if requested
    if args.settings_schema:
        schema_path = output_path.parent / "settings_schema.json"
        schema_content = generate_shopify_settings_schema(brand_config)

        with open(schema_path, 'w', encoding='utf-8') as f:
            f.write(schema_content)

        print(f"✅ Settings schema written to: {schema_path}")

    # Show preview
    print("\n📝 Preview (first 20 lines):")
    print("-" * 60)
    for line in css_content.splitlines()[:20]:
        print(line)
    print("-" * 60)


if __name__ == "__main__":
    main()
