from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

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

# Найдем элемент с классом 'product-card__title-wrapper'
nazvanie = driver.find_elements(By.CLASS_NAME, 'product-card__title-wrapper')
price = driver.find_elements(By.CLASS_NAME, 'product-card__price')

print(nazvanie)
for name in nazvanie:
        print(name.text)
for cena in price:
        print(cena.text)
driver.quit()