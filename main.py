from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from product import Products
from clear_lst import clear_file
from persing import perekrestok
from test import test_json,test_class
import time
import json


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

clear_file()
save_lst = perekrestok(driver)
with open("product_list.json", "w") as json_file:
    json.dump(save_lst, json_file)
#print(test_json)
driver.quit()