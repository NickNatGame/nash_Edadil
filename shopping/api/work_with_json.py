import json
import os
def clear_file():
    data = {}
    with open('D:/nash_Edadil/shopping/frontend/src/product_list.json', "w") as file:
        json.dump(data, file)
def save_file(save_lst):
    with open('D:/nash_Edadil/shopping/frontend/src/product_list.json', "w") as file:
        json.dump(save_lst, file)