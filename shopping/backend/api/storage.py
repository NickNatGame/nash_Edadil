import json
from pathlib import Path

from django.conf import settings


def _get_product_list_path():
    return getattr(
        settings,
        'PRODUCT_LIST_PATH',
        settings.BASE_DIR.parent / 'frontend' / 'src' / 'product_list.json'
    )


def clear_file():
    with open(_get_product_list_path(), "w", encoding="utf-8") as file:
        json.dump({}, file)


def save_file(save_lst):
    with open(_get_product_list_path(), "w", encoding="utf-8") as file:
        json.dump(save_lst, file, ensure_ascii=False)
