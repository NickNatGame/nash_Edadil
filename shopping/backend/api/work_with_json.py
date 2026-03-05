import json
from pathlib import Path

API_DIR = Path(__file__).resolve().parent
PRODUCTS_FILE = API_DIR / "product_list.json"


def clear_file():
    with PRODUCTS_FILE.open("w", encoding="utf-8") as file:
        json.dump([], file, ensure_ascii=False)


def save_file(save_lst):
    with PRODUCTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(save_lst, file, ensure_ascii=False)
