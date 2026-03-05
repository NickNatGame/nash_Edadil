import json
from pathlib import Path

API_DIR = Path(__file__).resolve().parent
PRODUCTS_FILE = API_DIR / "product_list.json"

def test_json():
    with PRODUCTS_FILE.open(encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def test_class(lst_products):
    for i in range(len(lst_products)):
        print(lst_products[i].name, lst_products[i].price)
