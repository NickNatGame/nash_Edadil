import itertools

from product import Products
import time
import json,random
from itertools import permutations

def perek(summ):
    if(summ < 700):
        return False
    else:
        return 172+summ
def azbuka(summ):
    return 175+summ
def eurospar(summ):
    if summ < 1205:
        return False
    else:
        return summ

def analize():
    cart = []
    cart_var = []
    with open("product_list.json", "r") as file:
        l = json.load(file)


    for i in range(5):
        j = random.randint(0,len(l)-1)
        cart.append(l[j])
    cart_new = [[0 for i in range(4)]for i in range(len(cart))]
    cart_new[0][0] = random.randint(0,10)
    cart_new[1][0] = random.randint(0, 10)
    cart_new[2][0] = random.randint(0, 10)
    cart_new[3][0] = random.randint(0, 10)
    cart_new[4][0] = random.randint(0, 10)




    for i in range(len(cart)):
        for j in range(3):
            if (cart[i].get("store") == "азбука вкуса"):
                cart_new[i][1] = cart[i]
            if(cart[i].get("store") == "перекресток"):
                cart_new[i][2] = cart[i]
            if (cart[i].get("store") == "евроспар"):
                cart_new[i][3] = cart[i]
            for t in range(len(l)):
                if (cart[i].get("name")[:10] == l[t].get("name")[:10] and cart[i].get("price") != l[t].get("price")):
                    if (l[t].get("store") == "азбука вкуса"):
                        cart_new[i][1] = l[t]
                    if (l[t].get("store") == "перекресток"):
                        cart_new[i][2] = l[t]
                    if (l[t].get("store") == "евроспар"):
                        cart_new[i][3] = l[t]
    digits = [1, 2, 3]
    cart_var = list(itertools.product(digits, repeat=len(cart)))
    lst = []
    for i in range(len(cart_var)):
        s = ""
        for j in range(len(cart_var[i])):
            s += f"{cart_var[i][j]}"
        for j in range(len(s)):
            if cart_new[j][int(s[j])] == 0:
                continue
            if perek(float(cart_new[j][int(s[j])].get("price"))) + eurospar(float(cart_new[j][int(s[j])].get("price"))) + azbuka(float(cart_new[j][int(s[j])].get("price"))) not in lst:
                lst.append(perek(float(cart_new[j][int(s[j])].get("price"))*cart_new[j][0]) + eurospar(float(cart_new[j][int(s[j])].get("price"))*cart_new[j][0]) + azbuka(float(cart_new[j][int(s[j])].get("price"))*cart_new[j][0]))

    print(lst)


    for i in range(len(cart_new)):
        for j in range(4):
            print(cart_new[i][j], end = " ")
        print()