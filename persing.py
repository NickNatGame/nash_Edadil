from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from product import Products
from clear_lst import clear_file
import time
import json

save_lst = []
clear_file()
lst_url = ["https://www.perekrestok.ru/cat/search?search=хлеб","https://www.perekrestok.ru/cat/search?search=рыба","https://www.perekrestok.ru/cat/search?search=мясо", "https://www.perekrestok.ru/cat/search?search=молоко"]

# options.add_argument("--headless")
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
for i in range(len(lst_url)):
    lst_products = []
    driver.get(lst_url[i])
    time.sleep(5)

    nazvanie = driver.find_elements(By.CLASS_NAME, 'product-card__title')
    price = driver.find_elements(By.CLASS_NAME, 'price-new')

    for i in range(len(nazvanie)):
        prod = Products(nazvanie[i].text, price[i].text[5:])
        save_lst.append(prod.to_json())
        lst_products.append(prod)
with open("product_list.json", "w") as json_file:
    json.dump(save_lst, json_file)
driver.quit()
