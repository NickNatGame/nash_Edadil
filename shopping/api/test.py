import json


def test_json():
    with open("D:/nash_Edadil/shopping/frontend/src/product_list.json", "r") as json_file:
        data = json.load(json_file)
    return data


def test_class(lst_products):
    for i in range(len(lst_products)):
        print(lst_products[i].name, lst_products[i].price)
