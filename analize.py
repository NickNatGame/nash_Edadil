from product import Products
import time
import json,random


def analize():
    l = []
    l_1 = []
    with open("product_list.json", "r") as file:
        l = json.load(file)
    for i in range(5):
        l_1.append(l[random.randint(0,len(l)-1)])
    print(l_1)
