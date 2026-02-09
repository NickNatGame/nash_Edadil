import json
import os
dir = os.path.abspath(os.curdir)

def load_sample_data():
    with open(dir + "\\api\\product_list.json") as json_file:
        data = json.load(json_file)
    return data


def test_class(lst_products):
    for i in range(len(lst_products)):
        print(lst_products[i].name, lst_products[i].price)
