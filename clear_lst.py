import json
def clear_file():
    with open("product_list.json", "r") as file:
        data = json.load(file)
    data = {}
    with open("product_list.json", "w") as file:
        json.dump(data, file)