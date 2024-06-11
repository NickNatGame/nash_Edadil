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

def analize(data):
    cart = []
    cart_1 = []
    cart_var = []

    l = json.loads(data)

    for i in range(len(l)):
        if l[i] not in cart:
            cart.append(l[i])
        cart_1.append(l[i])

    cart_new = [[0 for i in range(4)] for i in range(len(cart))]
    for i in range(len(cart)):
        cart_new[i][0] = cart_1.count(cart[i])

    for i in range(len(cart)):
        for j in range(3):
            if (cart[i].get("store") == "азбука вкуса"):
                cart_new[i][1] = cart[i]
            if (cart[i].get("store") == "перекресток"):
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
            if (s[j] == '1'):
                summ1 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
            if (s[j] == '2'):
                summ2 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
            if (s[j] == '3'):
                summ3 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
        if fl == False:
            if summ2 == 0 and summ3 != 0 and eurospar(summ3) != False:
                lst.append(azbuka(summ1) + eurospar(summ3))
            if summ2 != 0 and summ3 == 0 and perek(summ2) != False:
                lst.append(azbuka(summ1) + perek(summ2))
            if summ2 == 0 and summ3 == 0:
                lst.append(azbuka(summ1))
            if summ2 != 0 and perek(summ2) != False and summ3 != 0 and eurospar(summ3) != False:
                lst.append(azbuka(summ1) + + perek(summ2) + eurospar(summ3))
    print(lst)
    for i in range(len(cart_new)):
        for j in range(4):
            print(cart_new[i][j], end = " ")
        print()
    if(len(lst) == 0):
        return "Не набрана минимальная цена заказа из какого-то магазина"
    else:
        return f"{round(min(lst),2)} ₽"

