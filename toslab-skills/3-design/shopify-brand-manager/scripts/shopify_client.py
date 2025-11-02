#!/usr/bin/env python3
"""
Shopify API Client for Brand Management

Handles authentication and API requests to Shopify store.
Supports theme customization, metafield management, and asset uploads.

Requirements:
    - shopify_python_api (pip install ShopifyAPI)
    - requests

Environment Variables:
    SHOPIFY_STORE_URL - Your Shopify store URL (e.g., your-store.myshopify.com)
    SHOPIFY_ACCESS_TOKEN - Your Shopify Admin API access token
"""

import os
import json
import requests
from typing import Dict, List, Optional, Any
from pathlib import Path


class ShopifyBrandClient:
    """
    Shopify API client for brand management operations
    """

    def __init__(self, store_url: str = None, access_token: str = None):
        """
        Initialize Shopify client

        Args:
            store_url: Shopify store URL (e.g., your-store.myshopify.com)
            access_token: Shopify Admin API access token
        """
        self.store_url = store_url or os.getenv('SHOPIFY_STORE_URL')
        self.access_token = access_token or os.getenv('SHOPIFY_ACCESS_TOKEN')

        if not self.store_url or not self.access_token:
            raise ValueError(
                "Shopify credentials required. Set SHOPIFY_STORE_URL and "
                "SHOPIFY_ACCESS_TOKEN environment variables or pass them as arguments."
            )

        # Remove https:// if present
        self.store_url = self.store_url.replace('https://', '').replace('http://', '')

        self.base_url = f"https://{self.store_url}/admin/api/2024-01"
        self.headers = {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        """
        Make API request to Shopify

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            data: Request payload

        Returns:
            Response JSON

        Raises:
            requests.HTTPError: If request fails
        """
        url = f"{self.base_url}/{endpoint}"

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            json=data
        )

        response.raise_for_status()

        return response.json() if response.content else {}

    # ========== Theme Management ==========

    def get_themes(self) -> List[Dict]:
        """
        Get all themes from the store

        Returns:
            List of theme objects
        """
        response = self._request('GET', 'themes.json')
        return response.get('themes', [])

    def get_main_theme(self) -> Optional[Dict]:
        """
        Get the currently published main theme

        Returns:
            Main theme object or None
        """
        themes = self.get_themes()
        for theme in themes:
            if theme.get('role') == 'main':
                return theme
        return None

    def get_theme_asset(self, theme_id: int, asset_key: str) -> Optional[Dict]:
        """
        Get a specific asset from a theme

        Args:
            theme_id: Theme ID
            asset_key: Asset key (e.g., "assets/theme.css.liquid")

        Returns:
            Asset object or None
        """
        endpoint = f"themes/{theme_id}/assets.json?asset[key]={asset_key}"
        try:
            response = self._request('GET', endpoint)
            return response.get('asset')
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                return None
            raise

    def update_theme_asset(self, theme_id: int, asset_key: str, value: str) -> Dict:
        """
        Update or create a theme asset

        Args:
            theme_id: Theme ID
            asset_key: Asset key (e.g., "assets/brand-colors.css")
            value: Asset content

        Returns:
            Updated asset object
        """
        endpoint = f"themes/{theme_id}/assets.json"
        data = {
            "asset": {
                "key": asset_key,
                "value": value
            }
        }
        response = self._request('PUT', endpoint, data)
        return response.get('asset', {})

    def upload_theme_file(self, theme_id: int, asset_key: str, file_path: str) -> Dict:
        """
        Upload a file to theme assets

        Args:
            theme_id: Theme ID
            asset_key: Asset key (e.g., "assets/logo.svg")
            file_path: Local file path

        Returns:
            Asset object
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # For binary files (images, fonts), use attachment
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.woff', '.woff2', '.ttf']:
            import base64
            with open(file_path, 'rb') as f:
                attachment = base64.b64encode(f.read()).decode('utf-8')

            endpoint = f"themes/{theme_id}/assets.json"
            data = {
                "asset": {
                    "key": asset_key,
                    "attachment": attachment
                }
            }
        else:
            # For text files, use value
            with open(file_path, 'r', encoding='utf-8') as f:
                value = f.read()

            endpoint = f"themes/{theme_id}/assets.json"
            data = {
                "asset": {
                    "key": asset_key,
                    "value": value
                }
            }

        response = self._request('PUT', endpoint, data)
        return response.get('asset', {})

    # ========== Metafield Management ==========

    def get_metafields(self, resource: str, resource_id: int) -> List[Dict]:
        """
        Get metafields for a resource

        Args:
            resource: Resource type (e.g., "products", "collections", "shop")
            resource_id: Resource ID (use 0 for shop-level metafields)

        Returns:
            List of metafield objects
        """
        if resource == "shop":
            endpoint = "metafields.json"
        else:
            endpoint = f"{resource}/{resource_id}/metafields.json"

        response = self._request('GET', endpoint)
        return response.get('metafields', [])

    def create_metafield(
        self,
        resource: str,
        resource_id: int,
        namespace: str,
        key: str,
        value: Any,
        value_type: str = "string"
    ) -> Dict:
        """
        Create a metafield

        Args:
            resource: Resource type (e.g., "products", "collections", "shop")
            resource_id: Resource ID
            namespace: Metafield namespace
            key: Metafield key
            value: Metafield value
            value_type: Value type (string, integer, json, etc.)

        Returns:
            Created metafield object
        """
        if resource == "shop":
            endpoint = "metafields.json"
        else:
            endpoint = f"{resource}/{resource_id}/metafields.json"

        # Convert value to appropriate format
        if value_type == "json":
            value = json.dumps(value)

        data = {
            "metafield": {
                "namespace": namespace,
                "key": key,
                "value": value,
                "type": value_type
            }
        }

        response = self._request('POST', endpoint, data)
        return response.get('metafield', {})

    def update_metafield(self, metafield_id: int, value: Any) -> Dict:
        """
        Update an existing metafield

        Args:
            metafield_id: Metafield ID
            value: New value

        Returns:
            Updated metafield object
        """
        endpoint = f"metafields/{metafield_id}.json"
        data = {
            "metafield": {
                "value": value
            }
        }
        response = self._request('PUT', endpoint, data)
        return response.get('metafield', {})

    # ========== Shop Settings ==========

    def get_shop_info(self) -> Dict:
        """
        Get shop information

        Returns:
            Shop object
        """
        response = self._request('GET', 'shop.json')
        return response.get('shop', {})

    # ========== Product Management ==========

    def get_products(self, limit: int = 50) -> List[Dict]:
        """
        Get products from store

        Args:
            limit: Number of products to retrieve (max 250)

        Returns:
            List of product objects
        """
        endpoint = f"products.json?limit={limit}"
        response = self._request('GET', endpoint)
        return response.get('products', [])

    def update_product(self, product_id: int, data: Dict) -> Dict:
        """
        Update a product

        Args:
            product_id: Product ID
            data: Product data to update

        Returns:
            Updated product object
        """
        endpoint = f"products/{product_id}.json"
        payload = {"product": data}
        response = self._request('PUT', endpoint, payload)
        return response.get('product', {})

    # ========== Collection Management ==========

    def get_collections(self) -> List[Dict]:
        """
        Get custom collections

        Returns:
            List of collection objects
        """
        response = self._request('GET', 'custom_collections.json')
        return response.get('custom_collections', [])

    def update_collection(self, collection_id: int, data: Dict) -> Dict:
        """
        Update a collection

        Args:
            collection_id: Collection ID
            data: Collection data to update

        Returns:
            Updated collection object
        """
        endpoint = f"custom_collections/{collection_id}.json"
        payload = {"custom_collection": data}
        response = self._request('PUT', endpoint, payload)
        return response.get('custom_collection', {})


# ========== Helper Functions ==========

def load_brand_config(config_path: str = None) -> Dict:
    """
    Load brand configuration from JSON file

    Args:
        config_path: Path to brand-config.json

    Returns:
        Brand configuration dictionary
    """
    if config_path is None:
        # Default path relative to this script
        script_dir = Path(__file__).parent.parent
        config_path = script_dir / "assets" / "brand" / "brand-config.json"

    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def test_connection():
    """Test Shopify API connection"""
    try:
        client = ShopifyBrandClient()
        shop = client.get_shop_info()
        print(f"✅ Connected to Shopify store: {shop.get('name')}")
        print(f"   URL: {shop.get('domain')}")
        print(f"   Email: {shop.get('email')}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False


if __name__ == "__main__":
    # Test connection
    print("Testing Shopify API connection...")
    test_connection()
