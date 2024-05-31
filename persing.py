from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from product import Products
import time


def perekrestok(driver):
    save_lst = []
    lst_url = ["https://www.perekrestok.ru/cat/search?search=хлеб",
               "https://www.perekrestok.ru/cat/search?search=рыба",
               "https://www.perekrestok.ru/cat/search?search=мясо",
               "https://www.perekrestok.ru/cat/search?search=молоко"]
    for i in range(len(lst_url)):
        lst_products = []
        driver.get(lst_url[i])
        #time.sleep(5)

        nazvanie = driver.find_elements(By.CLASS_NAME, 'product-card__title')
        price = driver.find_elements(By.CLASS_NAME, 'price-new')
        image = driver.find_elements(By.CLASS_NAME, 'product-card__image')

        for i in range(len(nazvanie)):
            prod = Products(nazvanie[i].text, price[i].text[5:-2].replace(",","."), image[i].get_attribute("src"),'перекресток')
            save_lst.append(prod.to_json())
            lst_products.append(prod)
    return save_lst
def azvuka_vkusa(driver):
    save_lst = []
    lst_url = ["https://av.ru/search?text=%D0%BC%D1%8F%D1%81%D0%BE"]
    for i in range(len(lst_url)):
        lst_products = []
        driver.get(lst_url[i])
        time.sleep(5)
        element = driver.find_elements(By.XPATH,'//input[@class="button button--size-XL button--kind-primary"]')
        nazvanie = driver.find_elements(By.CLASS_NAME, 'product-info_name')
        price = driver.find_elements(By.CLASS_NAME, 'price')
        image = driver.find_elements(By.CLASS_NAME, 'product-images-slider_tab')
        for i in range(len(nazvanie)):
            print(nazvanie[i].text)
    return save_lst
def spar(driver):
    save_lst = []
    lst_url = [
               "https://myspar.ru/catalog/khleb/",
               "https://myspar.ru/catalog/okhlazhdennaya-ryba-2025/",
               "https://myspar.ru/catalog/zamorozhennaya-ryba-2025/",
               "https://myspar.ru/catalog/govyadina-telyatina/",
               "https://myspar.ru/catalog/myaso/",
               "https://myspar.ru/catalog/ptitsa/",
               "https://myspar.ru/catalog/moloko/"
              ]
    for i in range(len(lst_url)):
        lst_products = []
        driver.get(lst_url[i])
        #time.sleep(5)

        nazvanie = driver.find_elements(By.CLASS_NAME, "catalog-tile__name")
        price = driver.find_elements(By.CLASS_NAME, 'prices__cur')
        image = driver.find_elements(By.TAG_NAME, 'source')
        for i in range(len(nazvanie)):
            price_1 = price[i].text[:-2]
            prod = Products(nazvanie[i].text,price_1[:-2]+'.'+price_1[-2:], image[i].get_attribute("srcset"),'евроспар')
            save_lst.append(prod.to_json())
            lst_products.append(prod)
    return save_lst

