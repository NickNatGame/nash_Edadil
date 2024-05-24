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
        time.sleep(5)

        nazvanie = driver.find_elements(By.CLASS_NAME, 'product-card__title')
        price = driver.find_elements(By.CLASS_NAME, 'price-new')
        image = driver.find_elements(By.CLASS_NAME, 'product-card__image')

        for i in range(len(nazvanie)):
            prod = Products(nazvanie[i].text, price[i].text[5:], image[i].get_attribute("src"))
            save_lst.append(prod.to_json())
            lst_products.append(prod)
    return save_lst
def azvuka_vkusa(driver):
    save_lst = []
    lst_url = ["https://av.ru/search?text=%D0%BC%D1%8F%D1%81%D0%BE  "]
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
def pyaterochka(driver):
    save_lst = []
    lst_url = ["https://5ka.ru/special_offers"]
    for i in range(len(lst_url)):
        lst_products = []
        driver.get(lst_url[i])
        time.sleep(5)

        search_box = driver.find_element(By.TAG_NAME,"input")
        search_box.send_keys("молоко")
        search_box.send_keys(Keys.RETURN)

        # Пример ожидания загрузки результатов поиска
        driver.implicitly_wait(10)

        nazvanie = driver.find_elements(By.CLASS_NAME, 'item-name')
        price = driver.find_elements(By.CLASS_NAME, 'price')
        image = driver.find_elements(By.CLASS_NAME, 'product-images-slider_tab')

        for i in range(len(nazvanie)):
            print(nazvanie[i].text)
    return save_lst
def lenta(driver):
    save_lst = []
    lst_url = ["https://lenta.com/search/?searchText=%D0%BC%D1%8F%D1%81%D0%BE&searchSource=Sku"]
    for i in range(len(lst_url)):
        lst_products = []
        driver.get(lst_url[i])
        time.sleep(5)

        nazvanie = driver.find_elements(By.CLASS_NAME, 'lui-sku-product-card-text lui-sku-product-card-text--view-primary')
        price = driver.find_elements(By.CLASS_NAME, 'lui-priceText lui-priceText--view_regular')
        image = driver.find_elements(By.CLASS_NAME, 'lui-sku-product-card-image')

        for i in range(len(nazvanie)):
            print(nazvanie[i].text)
    return save_lst
