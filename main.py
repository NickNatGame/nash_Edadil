from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from product import Products
from work_with_json import clear_file,save_file
from persing import perekrestok,azvuka_vkusa,spar
from test import test_json,test_class
from analize import analize
import time
import json


options = webdriver.ChromeOptions()
#options.add_argument("--headless")
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

#clear_file()
#save_file(azvuka_vkusa(driver))
#save_file(spar(driver)+perekrestok(driver))
#save_file(perekrestok(driver))
#test_json()
analize()
driver.quit()