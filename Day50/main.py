from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import os

ACCOUNT_EMAIL = os.environ.get("MY_EMAIL")
ACCOUNT_PASSWORD = "password123"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://app.100daysofpython.dev/services/tindog/u/4U31cwtpoVIRvZDNju22Mnrah4wXcPG7")

wait = WebDriverWait(driver, 2)

login_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-tindog-']")))
login_button.click()

login_facebark = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-facebark']")))
login_facebark.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

fb_email = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[id^='email']")))
fb_password = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[id^='pass']")))

fb_email.send_keys(ACCOUNT_EMAIL)
fb_password.send_keys(ACCOUNT_PASSWORD, Keys.ENTER)

driver.switch_to.window(base_window)

wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-primary']"))).click()
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-secondary']"))).click()
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-primary']"))).click()

like_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-like']")))

for i in range(20):
    sleep(1)
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-like']"))).click()
    except ElementClickInterceptedException:
        try:
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[class^='match-popup-link']"))).click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        sleep(2)


