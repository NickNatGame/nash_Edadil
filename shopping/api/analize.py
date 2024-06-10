import itertools

from .product import Products
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

    with open("../frontend/src/product_list.json", "r") as file:
        l = json.load(file)

    for i in range(15):
        j = random.randint(0,len(l)-1)
        cart.append(l[j])
    cart_new = [[0 for i in range(4)]for i in range(len(cart))]
    for i in range(len(cart)):
        cart_new[i][0] = random.randint(1, 10)



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
    fl = False
    summ1 = 0
    summ2 = 0
    summ3 = 0
    for i in range(len(cart_var)):
        s = ""
        summ1 = 0
        summ2 = 0
        summ3 = 0
        for j in range(len(cart_var[i])):
            s += f"{cart_var[i][j]}"
        for j in range(len(s)):
            if cart_new[j][int(s[j])] == 0:
                fl = True
                break
            fl = False
            if(s[j] == '1'):
                summ1 += float(cart_new[j][int(s[j])].get("price"))*float(cart_new[j][0])
            if(s[j] == '2'):
                summ2 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
            if (s[j] == '3'):
                summ3 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
        if fl == False and azbuka(summ1) != False and perek(summ2) != False and eurospar(summ3) != False:
            lst.append(azbuka(summ1)+perek(summ2)+eurospar(summ3))


    '''for i in range(len(cart_new)):
        for j in range(4):
            print(cart_new[i][j], end = " ")
        print()'''
    return lst

