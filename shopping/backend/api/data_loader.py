import json

from django.conf import settings


def load_products():
    product_list_path = getattr(
        settings,
        'PRODUCT_LIST_PATH',
        settings.BASE_DIR.parent / 'frontend' / 'src' / 'product_list.json'
    )
    with open(product_list_path, "r", encoding="utf-8") as file:
        return json.load(file)
