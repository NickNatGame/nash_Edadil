from product import Products
import time
import json,random


def analize():
    l = []
    dublicate = [[]]
    cart_new = [[]]
    cart = []
    with open("product_list.json", "r") as file:
        l = json.load(file)


    for i in range(10):
        j = random.randint(0,len(l)-1)
        cart.append(l[j])
    cart_new = [[0 for i in range(3)]for i in range(len(cart))]

    p = 0
    v = 0

    for i in range(len(cart)):
        for j in range(3):
            if (cart[i].get("store") == "азбука вкуса"):
                cart_new[i][0] = cart[i]
            if(cart[i].get("store") == "перекресток"):
                cart_new[i][1] = cart[i]
            if (cart[i].get("store") == "евроспар"):
                cart_new[i][2] = cart[i]
            for t in range(len(l)):
                if (cart[i].get("name")[:10] == l[t].get("name")[:10] and cart[i].get("price") != l[t].get("price")):
                    if (l[t].get("store") == "азбука вкуса"):
                        cart_new[i][0] = l[t]
                    if (l[t].get("store") == "перекресток"):
                        cart_new[i][1] = l[t]
                    if (l[t].get("store") == "евроспар"):
                        cart_new[i][2] = l[t]
    for i in range(len(cart_new)):
        for j in range(3):
            print(cart_new[i][j], end = " ")
        print()