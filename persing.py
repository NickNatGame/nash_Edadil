from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from product import Products
import time


product_list = open('product_list.txt','w')

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

lst_products = []
# options.add_argument("--headless")

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

url = "https://www.perekrestok.ru/cat/search?search=%D1%85%D0%BB%D0%B5%D0%B1"
driver.get(url)
time.sleep(5)


# Найдем элемент с классом 'product-card__title-wrapper'
nazvanie = driver.find_elements(By.CLASS_NAME, 'product-card__title')
price = driver.find_elements(By.CLASS_NAME, 'product-card__price')

print(nazvanie)
for i in range(len(nazvanie)):
    #print(nazvanie[i].text)
    #print(price[i].text)
    #lst_name.append(f"{name.text}")
    product_1 = Products(nazvanie[i].text,price[i].text)
    lst_products.append(product_1)
    #product_list.write(f"{name.text}\n")
#for i in range(len(price)):
 #   lst_products[i] = Products("price.text")
    #lst_price.append(f"{cena.text}")
    #product_list.write(f"{cena.text}\n")

for i in range(len(lst_products)):
    print(lst_products[i].name,lst_products[i].price)
driver.quit()
product_list.close()
