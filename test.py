import json

def test_json():
    with open("product_list.json", "r") as json_file:
        data = json.load(json_file)
    for i in range(len(data)):
        print(data[i])
def test_class(lst_products):
    for i in range(len(lst_products)):
        print(lst_products[i].name, lst_products[i].price)