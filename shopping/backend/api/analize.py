import itertools
import json
from pathlib import Path

API_DIR = Path(__file__).resolve().parent
PRODUCTS_FILE = API_DIR / "product_list.json"


def perek(summ):
    if summ < 700:
        return False
    return 172 + summ


def azbuka(summ):
    return 175 + summ


def eurospar(summ):
    if summ < 1205:
        return False
    return summ


def _to_float_price(value):
    return float(str(value).replace(",", "."))


def _load_cart(data):
    if isinstance(data, (bytes, bytearray)):
        return json.loads(data.decode("utf-8"))
    if isinstance(data, str):
        return json.loads(data)
    return data


def analize(data):
    cart = []
    cart_1 = []

    l_cart = _load_cart(data)
    if not isinstance(l_cart, list) or len(l_cart) == 0:
        return {
            "ok": False,
            "message": "Корзина пуста",
            "total": None,
            "subtotal": None,
            "items": [],
        }

    with PRODUCTS_FILE.open(encoding="utf-8") as file:
        products = json.load(file)

    for item in l_cart:
        if item not in cart:
            cart.append(item)
        cart_1.append(item)

    cart_new = [[0 for _ in range(4)] for _ in range(len(cart))]
    for i in range(len(cart)):
        cart_new[i][0] = cart_1.count(cart[i])

    for i in range(len(cart)):
        if cart[i].get("store") == "азбука вкуса":
            cart_new[i][1] = cart[i]
        if cart[i].get("store") == "перекресток":
            cart_new[i][2] = cart[i]
        if cart[i].get("store") == "евроспар":
            cart_new[i][3] = cart[i]

        for product in products:
            same_prefix_name = cart[i].get("name", "")[:10] == product.get("name", "")[:10]
            different_price = cart[i].get("price") != product.get("price")
            if same_prefix_name and different_price:
                if product.get("store") == "азбука вкуса":
                    cart_new[i][1] = product
                if product.get("store") == "перекресток":
                    cart_new[i][2] = product
                if product.get("store") == "евроспар":
                    cart_new[i][3] = product

    digits = [1, 2, 3]
    cart_var = itertools.product(digits, repeat=len(cart))
    lst_price = []
    lst_cart = []
    lst_price_1 = []
    lst_cart_1 = []

    for variant in cart_var:
        s = "".join(str(digit) for digit in variant)
        summ1 = 0
        summ2 = 0
        summ3 = 0
        invalid_variant = False

        for j in range(len(s)):
            if cart_new[j][int(s[j])] == 0:
                invalid_variant = True
                break
            if s[j] == "1":
                summ1 += _to_float_price(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
            if s[j] == "2":
                summ2 += _to_float_price(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])
            if s[j] == "3":
                summ3 += _to_float_price(cart_new[j][int(s[j])].get("price")) * float(cart_new[j][0])

        if invalid_variant:
            continue

        if summ2 == 0 and summ3 != 0 and eurospar(summ3) is not False and summ1 != 0:
            lst_price.append(azbuka(summ1) + eurospar(summ3))
            lst_price_1.append(summ1 + summ3)
            lst_cart.append(s)
        if summ2 != 0 and summ3 == 0 and perek(summ2) is not False and summ1 != 0:
            lst_price.append(azbuka(summ1) + perek(summ2))
            lst_price_1.append(summ1 + summ2)
            lst_cart.append(s)
        if summ2 == 0 and summ3 == 0 and summ1 != 0:
            lst_price.append(azbuka(summ1))
            lst_price_1.append(summ1)
            lst_cart.append(s)
        if summ2 != 0 and perek(summ2) is not False and summ3 != 0 and eurospar(summ3) is not False and summ1 != 0:
            lst_price.append(azbuka(summ1) + perek(summ2) + eurospar(summ3))
            lst_price_1.append(summ1 + summ2 + summ3)
            lst_cart.append(s)
        if summ2 == 0 and summ3 != 0 and eurospar(summ3) is not False and summ1 == 0:
            lst_price.append(eurospar(summ3))
            lst_price_1.append(summ3)
            lst_cart.append(s)
        if summ2 != 0 and summ3 == 0 and perek(summ2) is not False and summ1 == 0:
            lst_price.append(perek(summ2))
            lst_price_1.append(summ2)
            lst_cart.append(s)
        if summ2 != 0 and perek(summ2) is not False and summ3 != 0 and eurospar(summ3) is not False and summ1 == 0:
            lst_price.append(perek(summ2) + eurospar(summ3))
            lst_price_1.append(summ2 + summ3)
            lst_cart.append(s)

    if len(lst_price) == 0 or lst_price[0] == 175:
        return {
            "ok": False,
            "message": "Не набрана минимальная цена заказа из какого-то магазина",
            "total": None,
            "subtotal": None,
            "items": [],
        }

    best_index = lst_price.index(min(lst_price))
    best_cart_signature = str(lst_cart[best_index])

    for i in range(len(best_cart_signature)):
        product = cart_new[i][int(best_cart_signature[i])]
        if product not in lst_cart_1:
            lst_cart_1.append(product)

    total = round(min(lst_price), 2)
    subtotal = round(min(lst_price_1), 2)

    return {
        "ok": True,
        "message": f"{total} ₽ (Без доставки {subtotal} ₽)",
        "total": total,
        "subtotal": subtotal,
        "items": lst_cart_1,
    }
