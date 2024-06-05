from product import Products
import time
import json,random


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
        return 1205+summ

def analize():
    cart = []
    cart_var = []
    with open("product_list.json", "r") as file:
        l = json.load(file)


    for i in range(10):
        j = random.randint(0,len(l)-1)
        cart.append(l[j])
    cart_new = [[0 for i in range(4)]for i in range(len(cart))]
    cart_new[0][0] = random.randint(0,10)
    cart_new[1][0] = random.randint(0, 10)
    cart_new[2][0] = random.randint(0, 10)
    cart_new[3][0] = random.randint(0, 10)
    cart_new[4][0] = random.randint(0, 10)
    cart_new[5][0] = random.randint(0, 10)
    cart_new[6][0] = random.randint(0, 10)
    cart_new[7][0] = random.randint(0, 10)
    cart_new[8][0] = random.randint(0, 10)
    cart_new[9][0] = random.randint(0, 10)




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


    for a in range(len(cart)):
        for b in range(len(cart)):
            for c in range(len(cart)):
                summ = 0
                if cart_new[a][1] != 0:
                    summ += float(cart_new[a][1].get("price"))*float(cart_new[a][0])
                if cart_new[a][2] != 0:
                    summ += float(cart_new[a][2].get("price"))*float(cart_new[a][0])
                if cart_new[a][3] != 0:
                    summ += float(cart_new[a][3].get("price"))*float(cart_new[a][0])
                if(summ not in cart_var):
                    cart_var.append(summ)
    print(cart_var)



    for i in range(len(cart_new)):
        for j in range(4):
            print(cart_new[i][j], end = " ")
        print()