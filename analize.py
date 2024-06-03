from product import Products
import time
import json,random


def analize():
    l = []
    dublicate = [[]]
    cart = []
    with open("product_list.json", "r") as file:
        l = json.load(file)


    for i in range(10):
        j = random.randint(0,len(l)-1)
        cart.append(l[j])
    p = 0
    v = 0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if((l[i].get("name")[:5] != "Стейк" or l[i].get("name")[:5] != "cтейк") or (l[i].get("name")[:7] != "Медальон" or l[i].get("name")[:7] != "медальон")):
                if(l[i].get("name")[:10] == l[j].get("name")[:10] and l[i].get("store") != l[j].get("store")):
                    dublicate.append([])
                    dublicate[p].append(l[i])
                    dublicate[v].append(l[j])
                    p += 1
                    v += 1
            else:
                if (l[i].get("name")[:15] == l[j].get("name")[:15] and l[i].get("store") != l[j].get("store")):
                    dublicate.append([])
                    dublicate[p].append(l[i])
                    dublicate[v].append(l[j])
                    p += 1
                    v += 1
    p_1 = random.randint(0,len(dublicate)-1)
    v_1 = random.randint(0,1)
    cart.append(dublicate[0][1])
    summ = 0
    for i in range(len(cart)):
        var_1 = 0
        var_2 = 0
        fl = False
        for j in range(len(dublicate)-1):
            if(dublicate[j][0] == cart[i] or dublicate[j][1] == cart[i]):
                var_1 = dublicate[j][0]
                var_2 = dublicate[j][1]
                fl = True
                break
        if(fl):
            if(float(var_1.get("price")) + summ < float(var_2.get("price")) + summ):
                summ += float(var_1.get("price"))
            else:
                summ += float(var_2.get("price"))
        else:
            summ += float(cart[i].get("price"))
    print(cart)
    print(l)
    print(summ)