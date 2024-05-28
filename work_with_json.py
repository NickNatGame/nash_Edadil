import json
def clear_file():
    data = {}
    with open("product_list.json", "w") as file:
        json.dump(data, file)
def save_file(save_lst):
    with open("product_list.json", "w") as file:
        json.dump(save_lst, file)