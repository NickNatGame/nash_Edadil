from selenium import webdriver
from selenium_stealth import stealth
from .json_utils import save_file
from .parsing import perekrestok, azvuka_vkusa, spar
from .analyze import analyze

def parsing():
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
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
        save_file(perekrestok(driver) + spar(driver) + azvuka_vkusa(driver))
        driver.quit()
def cart():
        analyze()
#clear_file()
#save_file(azvuka_vkusa(driver))
#save_file(azvuka_vkusa(driver)+perekrestok(driver)+spar(driver))
#save_file(perekrestok(driver))
#load_sample_data()
