#!/usr/bin/env python3
"""
Apply Brand to Shopify Store

This script applies your brand configuration to a Shopify store:
- Uploads brand assets (logos, images)
- Updates theme with brand CSS variables
- Sets metafields with brand story and guidelines
- Configures theme settings with brand colors

Usage:
    python apply_brand_to_shopify.py
    python apply_brand_to_shopify.py --theme-id 123456789
    python apply_brand_to_shopify.py --dry-run  # Preview changes without applying
    python apply_brand_to_shopify.py --full     # Apply everything (assets + theme + metafields)
"""

import argparse
import json
import sys
from pathlib import Path
from shopify_client import ShopifyBrandClient, load_brand_config
from generate_css_variables import generate_css_variables


def apply_css_variables(client: ShopifyBrandClient, theme_id: int, brand_config: dict, dry_run: bool = False):
    """
    Apply brand CSS variables to theme

    Args:
        client: Shopify client
        theme_id: Theme ID to update
        brand_config: Brand configuration
        dry_run: If True, only preview changes
    """
    print("\n🎨 Applying CSS variables to theme...")

    # Generate CSS variables
    css_content = generate_css_variables(brand_config, format='css')

    asset_key = "assets/brand-variables.css"

    if dry_run:
        print(f"   [DRY RUN] Would create/update: {asset_key}")
        print(f"   Preview (first 15 lines):")
        for line in css_content.splitlines()[:15]:
            print(f"   {line}")
        return

    # Upload CSS file to theme
    result = client.update_theme_asset(theme_id, asset_key, css_content)

    print(f"   ✅ Created/updated: {asset_key}")
    print(f"   Size: {len(css_content)} bytes")


def upload_brand_assets(client: ShopifyBrandClient, theme_id: int, brand_config: dict, dry_run: bool = False):
    """
    Upload brand assets (logos, images) to theme

    Args:
        client: Shopify client
        theme_id: Theme ID
        brand_config: Brand configuration
        dry_run: If True, only preview changes
    """
    print("\n📤 Uploading brand assets...")

    script_dir = Path(__file__).parent.parent
    assets_dir = script_dir / "assets"

    assets = brand_config.get('assets', {})

    uploaded_count = 0

    # Upload logos
    if 'logo' in assets:
        for logo_type, logo_path in assets['logo'].items():
            local_path = assets_dir / logo_path
            remote_key = f"assets/brand-{logo_type}.{local_path.suffix}"

            if not local_path.exists():
                print(f"   ⚠️  File not found: {local_path}")
                continue

            if dry_run:
                print(f"   [DRY RUN] Would upload: {local_path} → {remote_key}")
                continue

            try:
                client.upload_theme_file(theme_id, remote_key, str(local_path))
                print(f"   ✅ Uploaded: {remote_key}")
                uploaded_count += 1
            except Exception as e:
                print(f"   ❌ Failed to upload {remote_key}: {e}")

    # Upload other images
    if 'images' in assets:
        for img_type, img_path in assets['images'].items():
            local_path = assets_dir / img_path
            remote_key = f"assets/brand-{img_type}.{local_path.suffix}"

            if not local_path.exists():
                print(f"   ⚠️  File not found: {local_path}")
                continue

            if dry_run:
                print(f"   [DRY RUN] Would upload: {local_path} → {remote_key}")
                continue

            try:
                client.upload_theme_file(theme_id, remote_key, str(local_path))
                print(f"   ✅ Uploaded: {remote_key}")
                uploaded_count += 1
            except Exception as e:
                print(f"   ❌ Failed to upload {remote_key}: {e}")

    if not dry_run:
        print(f"\n   📊 Total uploaded: {uploaded_count} files")


def set_brand_metafields(client: ShopifyBrandClient, brand_config: dict, dry_run: bool = False):
    """
    Set shop-level metafields with brand information

    Args:
        client: Shopify client
        brand_config: Brand configuration
        dry_run: If True, only preview changes
    """
    print("\n📝 Setting brand metafields...")

    namespace = brand_config.get('shopify', {}).get('metafield_namespace', 'toslab_brand')

    metafields = [
        {
            'key': 'brand_config',
            'value': brand_config,
            'type': 'json',
            'description': 'Full brand configuration'
        },
        {
            'key': 'brand_name',
            'value': brand_config.get('brand', {}).get('name', ''),
            'type': 'string',
            'description': 'Brand name'
        },
        {
            'key': 'brand_tagline',
            'value': brand_config.get('brand', {}).get('tagline', ''),
            'type': 'string',
            'description': 'Brand tagline'
        },
        {
            'key': 'primary_color',
            'value': brand_config.get('colors', {}).get('primary', {}).get('hex', ''),
            'type': 'color',
            'description': 'Primary brand color'
        },
        {
            'key': 'secondary_color',
            'value': brand_config.get('colors', {}).get('secondary', {}).get('hex', ''),
            'type': 'color',
            'description': 'Secondary brand color'
        }
    ]

    # Load brand story
    script_dir = Path(__file__).parent.parent
    story_path = script_dir / "assets" / "brand" / "brand-story.md"

    if story_path.exists():
        with open(story_path, 'r', encoding='utf-8') as f:
            brand_story = f.read()

        metafields.append({
            'key': 'brand_story',
            'value': brand_story,
            'type': 'multi_line_text_field',
            'description': 'Brand story and guidelines'
        })

    for metafield in metafields:
        if dry_run:
            print(f"   [DRY RUN] Would set metafield: {namespace}.{metafield['key']}")
            print(f"   Type: {metafield['type']}")
            print(f"   Description: {metafield['description']}")
            continue

        try:
            # Check if metafield exists
            existing = client.get_metafields('shop', 0)
            existing_field = next(
                (m for m in existing if m['namespace'] == namespace and m['key'] == metafield['key']),
                None
            )

            if existing_field:
                # Update existing
                client.update_metafield(existing_field['id'], metafield['value'])
                print(f"   ✅ Updated: {namespace}.{metafield['key']}")
            else:
                # Create new
                client.create_metafield(
                    'shop', 0,
                    namespace,
                    metafield['key'],
                    metafield['value'],
                    metafield['type']
                )
                print(f"   ✅ Created: {namespace}.{metafield['key']}")

        except Exception as e:
            print(f"   ❌ Failed to set {metafield['key']}: {e}")


def update_theme_settings(client: ShopifyBrandClient, theme_id: int, brand_config: dict, dry_run: bool = False):
    """
    Update theme settings with brand colors

    Args:
        client: Shopify client
        theme_id: Theme ID
        brand_config: Brand configuration
        dry_run: If True, only preview changes
    """
    print("\n⚙️  Updating theme settings...")

    # Get current theme settings
    try:
        settings_asset = client.get_theme_asset(theme_id, "config/settings_data.json")

        if not settings_asset:
            print("   ⚠️  settings_data.json not found in theme")
            return

        settings_data = json.loads(settings_asset.get('value', '{}'))

        # Update color settings
        colors = brand_config.get('colors', {})

        if 'current' not in settings_data:
            settings_data['current'] = {}

        color_updates = {}

        if 'primary' in colors:
            color_updates['brand_primary'] = colors['primary']['hex']

        if 'secondary' in colors:
            color_updates['brand_secondary'] = colors['secondary']['hex']

        if 'accent' in colors:
            color_updates['brand_accent'] = colors['accent']['hex']

        if dry_run:
            print("   [DRY RUN] Would update theme settings:")
            for key, value in color_updates.items():
                print(f"   {key}: {value}")
            return

        # Apply updates
        settings_data['current'].update(color_updates)

        # Save back to theme
        updated_value = json.dumps(settings_data, indent=2)
        client.update_theme_asset(theme_id, "config/settings_data.json", updated_value)

        print(f"   ✅ Updated {len(color_updates)} color settings")

    except Exception as e:
        print(f"   ❌ Failed to update theme settings: {e}")


def create_liquid_snippet(client: ShopifyBrandClient, theme_id: int, brand_config: dict, dry_run: bool = False):
    """
    Create a Liquid snippet for easy brand access

    Args:
        client: Shopify client
        theme_id: Theme ID
        brand_config: Brand configuration
        dry_run: If True, only preview changes
    """
    print("\n💧 Creating Liquid snippet...")

    snippet_content = """{% comment %}
  Brand Variables Snippet
  Usage: {% render 'brand-variables' %}

  This snippet loads brand variables and makes them available in your theme.
{% endcomment %}

<style>
  {{ 'brand-variables.css' | asset_url | stylesheet_tag }}
</style>

{% comment %} Brand Constants {% endcomment %}
{% assign brand_name = "{{ brand_name }}" %}
{% assign brand_tagline = "{{ brand_tagline }}" %}
{% assign brand_primary = "{{ primary_color }}" %}
{% assign brand_secondary = "{{ secondary_color }}" %}
{% assign brand_accent = "{{ accent_color }}" %}
""".replace("{{ brand_name }}", brand_config.get('brand', {}).get('name', 'toslab'))
    snippet_content = snippet_content.replace("{{ brand_tagline }}", brand_config.get('brand', {}).get('tagline', ''))
    snippet_content = snippet_content.replace("{{ primary_color }}", brand_config.get('colors', {}).get('primary', {}).get('hex', ''))
    snippet_content = snippet_content.replace("{{ secondary_color }}", brand_config.get('colors', {}).get('secondary', {}).get('hex', ''))
    snippet_content = snippet_content.replace("{{ accent_color }}", brand_config.get('colors', {}).get('accent', {}).get('hex', ''))

    asset_key = "snippets/brand-variables.liquid"

    if dry_run:
        print(f"   [DRY RUN] Would create: {asset_key}")
        return

    client.update_theme_asset(theme_id, asset_key, snippet_content)
    print(f"   ✅ Created: {asset_key}")
    print("   💡 Add to theme.liquid: {% render 'brand-variables' %}")


def main():
    parser = argparse.ArgumentParser(
        description='Apply brand configuration to Shopify store'
    )
    parser.add_argument(
        '--theme-id',
        type=int,
        help='Theme ID to update (default: main theme)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without applying them'
    )
    parser.add_argument(
        '--full',
        action='store_true',
        help='Apply everything (CSS + assets + metafields + settings)'
    )
    parser.add_argument(
        '--css-only',
        action='store_true',
        help='Only update CSS variables'
    )
    parser.add_argument(
        '--assets-only',
        action='store_true',
        help='Only upload brand assets'
    )

    args = parser.parse_args()

    print("🏪 Shopify Brand Manager")
    print("=" * 60)

    if args.dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
        print("=" * 60)

    try:
        # Initialize client
        print("\n🔌 Connecting to Shopify...")
        client = ShopifyBrandClient()

        shop = client.get_shop_info()
        print(f"   ✅ Connected to: {shop.get('name')}")

        # Load brand configuration
        brand_config = load_brand_config()
        print(f"\n📖 Loaded brand config: {brand_config.get('brand', {}).get('name')}")

        # Determine theme ID
        if args.theme_id:
            theme_id = args.theme_id
            print(f"\n🎨 Using specified theme ID: {theme_id}")
        else:
            main_theme = client.get_main_theme()
            if not main_theme:
                print("❌ No main theme found. Please specify --theme-id")
                sys.exit(1)

            theme_id = main_theme['id']
            print(f"\n🎨 Using main theme: {main_theme.get('name')} (ID: {theme_id})")

        # Apply changes based on flags
        if args.css_only:
            apply_css_variables(client, theme_id, brand_config, args.dry_run)

        elif args.assets_only:
            upload_brand_assets(client, theme_id, brand_config, args.dry_run)

        elif args.full:
            # Apply everything
            apply_css_variables(client, theme_id, brand_config, args.dry_run)
            upload_brand_assets(client, theme_id, brand_config, args.dry_run)
            set_brand_metafields(client, brand_config, args.dry_run)
            update_theme_settings(client, theme_id, brand_config, args.dry_run)
            create_liquid_snippet(client, theme_id, brand_config, args.dry_run)

        else:
            # Default: CSS + Liquid snippet
            apply_css_variables(client, theme_id, brand_config, args.dry_run)
            create_liquid_snippet(client, theme_id, brand_config, args.dry_run)

        print("\n" + "=" * 60)
        if args.dry_run:
            print("✅ Dry run completed. Use without --dry-run to apply changes.")
        else:
            print("✅ Brand successfully applied to Shopify store!")
            print("\n📚 Next steps:")
            print("   1. Add {% render 'brand-variables' %} to theme.liquid")
            print("   2. Use CSS variables in your theme (e.g., var(--brand-primary))")
            print("   3. Test your changes in the theme editor")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
