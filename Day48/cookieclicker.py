from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ozh.github.io/cookieclicker/")

    time.sleep(5)
    language_select = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
    language_select.click()


    last_click = time.monotonic()
    last_bought_product = time.monotonic()
    last_bought_upgrade = time.monotonic()
    while True:
        current_time = time.monotonic()

        if current_time - last_click >= 0.1:
            clicking_cookie(driver)
            last_click = current_time

        if current_time - last_bought_product >= 3:
            buy_products(driver)
            last_bought_product = current_time

        if current_time - last_bought_upgrade >= 30:
            buy_upgrades(driver)
            last_bought_upgrade = current_time



def clicking_cookie(driver):
    cookie_click = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")
    cookie_click.click()

def buy_products(driver):
    try:
        products = driver.find_elements(By.CSS_SELECTOR, value="#products .enabled")
        products[-1].click()
    except IndexError:
        print("No buyable products")

def buy_upgrades(driver):
    try:
        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#upgrades .enabled")
        upgrades[-1].click()
    except IndexError:
        print("No buyable upgrades")

main()



