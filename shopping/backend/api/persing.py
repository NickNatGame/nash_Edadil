from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .product import Products
import time


def perekrestok(driver):
    save_lst = []
    lst_url = ["https://www.perekrestok.ru/cat/search?search=хлеб",
               "https://www.perekrestok.ru/cat/search?search=рыба",
               "https://www.perekrestok.ru/cat/search?search=мясо",
               "https://www.perekrestok.ru/cat/search?search=молоко"]
    for i in range(len(lst_url)):
        driver.get(lst_url[i])
        time.sleep(5)

        nazvanie = driver.find_elements(By.CLASS_NAME, 'product-card__title')
        price = driver.find_elements(By.CLASS_NAME, 'price-new')
        image = driver.find_elements(By.CLASS_NAME, 'product-card__image')

        for i in range(len(nazvanie)):
            if(price[i].text != ''):
                prod = Products(nazvanie[i].text, price[i].text[5:-2].replace(",",".").replace(" ",""), image[i].get_attribute("src"),'перекресток')
                save_lst.append(prod.to_json())
    return save_lst
def azvuka_vkusa(driver):
    save_lst = []
    lst_url = ["https://av.ru/search/?text=%D1%85%D0%BB%D0%B5%D0%B1",
               "https://av.ru/search?text=%D1%80%D1%8B%D0%B1%D0%B0",
               "https://av.ru/search/?text=%D0%BC%D1%8F%D1%81%D0%BE",
               "https://av.ru/search?text=%D0%BC%D0%BE%D0%BB%D0%BE%D0%BA%D0%BE"]

    for i in range(len(lst_url)):
        driver.get(lst_url[i])
        '''button = driver.find_element(By.CLASS_NAME,"button_content")
        button.click()'''
        body = driver.find_element(By.TAG_NAME,'body')
        for i in range(20):
            body.send_keys(Keys.ARROW_RIGHT)
        time.sleep(8)
        nazvanie = driver.find_elements(By.CLASS_NAME, 'product-info_name')
        price = driver.find_elements(By.CLASS_NAME, 'product-price_current-price')
        #image = driver.find_elements(By.CLASS_NAME, 'product-images-slider')
        for i in range(len(nazvanie)):
            prod = Products(nazvanie[i].text, price[i].text.replace(",", ".").replace("\n","").replace("/","").replace("₽","").replace(" ","").replace("кг",""),"", 'азбука вкуса')
            save_lst.append(prod.to_json())
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
        driver.get(lst_url[i])
        #time.sleep(5)

        nazvanie = driver.find_elements(By.CLASS_NAME, "catalog-tile__name")
        price = driver.find_elements(By.CLASS_NAME, 'prices__cur')
        image = driver.find_elements(By.TAG_NAME, 'source')
        for i in range(len(nazvanie)):
            price_1 = price[i].text[:-2]
            if(price_1 != ""):
                prod = Products(nazvanie[i].text,price_1[:-2].replace(" ","")+'.'+price_1[-2:], image[i].get_attribute("srcset"),'евроспар')
                save_lst.append(prod.to_json())
    return save_lst
