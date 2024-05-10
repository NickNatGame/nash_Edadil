from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from product import Products
import time
import json

save_lst = []

def perekrestok(driver):
    lst_url = ["https://www.perekrestok.ru/cat/search?search=хлеб",
               "https://www.perekrestok.ru/cat/search?search=рыба",
               "https://www.perekrestok.ru/cat/search?search=мясо",
               "https://www.perekrestok.ru/cat/search?search=молоко"]
    for i in range(len(lst_url)):
        lst_products = []
        driver.get(lst_url[i])
        time.sleep(5)

        nazvanie = driver.find_elements(By.CLASS_NAME, 'product-card__title')
        price = driver.find_elements(By.CLASS_NAME, 'price-new')
        image = driver.find_elements(By.CLASS_NAME, 'product-card__image')

        for i in range(len(nazvanie)):
            prod = Products(nazvanie[i].text, price[i].text[5:], image[i].get_attribute("src"))
            save_lst.append(prod.to_json())
            lst_products.append(prod)
    return save_lst
def pyaterochka(driver):
    return 0
