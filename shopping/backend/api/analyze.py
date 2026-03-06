import itertools
import json

from django.conf import settings
from .product import Products


def _perek_cost(summ):
    if summ < 700:
        return False
    return 172 + summ


def _azbuka_cost(summ):
    return 175 + summ


def _eurospar_cost(summ):
    if summ < 1205:
        return False
    return summ


def analyze(data):
    cart = []
    cart_1 = []
    cart_var = []

    l_cart = json.loads(data)
    product_list_path = getattr(
        settings,
        'PRODUCT_LIST_PATH',
        settings.BASE_DIR.parent / 'frontend' / 'src' / 'product_list.json'
    )
    with open(product_list_path, "r", encoding="utf-8") as file:
        l = json.load(file)

    for i in range(len(l_cart)):
        if l_cart[i] not in cart:
            cart.append(l_cart[i])
        cart_1.append(l_cart[i])

    cart_new = [[0 for _ in range(4)] for _ in range(len(cart))]
    for i in range(len(cart)):
        cart_new[i][0] = cart_1.count(cart[i])

    for i in range(len(cart)):
        for j in range(3):
            if cart[i].get("store") == "азбука вкуса":
                cart_new[i][1] = cart[i]
            if cart[i].get("store") == "перекресток":
                cart_new[i][2] = cart[i]
            if cart[i].get("store") == "евроспар":
                cart_new[i][3] = cart[i]
            for t in range(len(l)):
                if (cart[i].get("name")[:10] == l[t].get("name")[:10]
                        and cart[i].get("price") != l[t].get("price")):
                    if l[t].get("store") == "азбука вкуса":
                        cart_new[i][1] = l[t]
                    if l[t].get("store") == "перекресток":
                        cart_new[i][2] = l[t]
                    if l[t].get("store") == "евроспар":
                        cart_new[i][3] = l[t]

    digits = [1, 2, 3]
    cart_var = list(itertools.product(digits, repeat=len(cart)))
    lst_price = []
    lst_cart = []
    lst_price_1 = []
    lst_cart_1 = []
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
            if s[j] == '1':
                summ1 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
            if s[j] == '2':
                summ2 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
            if s[j] == '3':
                summ3 += float(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])

        if fl is False:
            if summ2 == 0 and summ3 != 0 and _eurospar_cost(summ3) and summ1 != 0:
                lst_price.append(_azbuka_cost(summ1) + _eurospar_cost(summ3))
                lst_price_1.append(summ1 + summ3)
                lst_cart.append(s)
            if summ2 != 0 and summ3 == 0 and _perek_cost(summ2) and summ1 != 0:
                lst_price.append(_azbuka_cost(summ1) + _perek_cost(summ2))
                lst_price_1.append(summ1 + summ2)
                lst_cart.append(s)
            if summ2 == 0 and summ3 == 0 and summ1 != 0:
                lst_price.append(_azbuka_cost(summ1))
                lst_price_1.append(summ1)
                lst_cart.append(s)
            if (summ2 != 0 and _perek_cost(summ2) and summ3 != 0
                    and _eurospar_cost(summ3) and summ1 != 0):
                lst_price.append(_azbuka_cost(summ1) + _perek_cost(summ2) + _eurospar_cost(summ3))
                lst_price_1.append(summ1 + summ2 + summ3)
                lst_cart.append(s)
            if summ2 == 0 and summ3 != 0 and _eurospar_cost(summ3) and summ1 == 0:
                lst_price.append(_eurospar_cost(summ3))
                lst_price_1.append(summ3)
                lst_cart.append(s)
            if summ2 != 0 and summ3 == 0 and _perek_cost(summ2) and summ1 == 0:
                lst_price.append(_perek_cost(summ2))
                lst_price_1.append(summ2)
                lst_cart.append(s)
            if (summ2 != 0 and _perek_cost(summ2) and summ3 != 0
                    and _eurospar_cost(summ3) and summ1 == 0):
                lst_price.append(_perek_cost(summ2) + _eurospar_cost(summ3))
                lst_price_1.append(summ2 + summ3)
                lst_cart.append(s)

    if len(lst_price) == 0 or lst_price[0] == 175:
        return "Не набрана минимальная цена заказа из какого-то магазина"

    l = lst_cart[lst_price.index(min(lst_price))]
    l = f"{l}"
    for i in range(len(l)):
        if cart_new[i][int(l[i])] not in lst_cart_1:
            lst_cart_1.append(cart_new[i][int(l[i])])
    return [f"{round(min(lst_price), 2)} ₽ ( Без доставки {round(min(lst_price_1), 2)} ₽ )", lst_cart_1]
