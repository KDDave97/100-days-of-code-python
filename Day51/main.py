from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time

ACCOUNT_EMAIL = os.environ.get("MY_EMAIL")
ACCOUNT_PASSWORD = "password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net")

wait = WebDriverWait(driver, timeout=120)

wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[id^='onetrust-accept-btn-handler']"))).click()
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='flex h-[176px]']"))).click()

result_id = wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                           '//*[@id="root"]/div/div[1]/div/div[2]/div[2]'
                                                           '/div[2]/div/div/div/div[1]/p/a')))

test_finished = bool(result_id)

if test_finished:
    download_speed = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]'
                                                                '/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3'))).text
    upload_speed = wait.until(ec.presence_of_element_located((By.XPATH,
                                                              '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]'
                                                              '/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3'))).text

driver.get("https://app.100daysofpython.dev/services/y")
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[class^='y-login-link']"))).click()
y_email_login = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[id^='email']")))
y_password_login = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[id^='password']")))
y_email_login.send_keys(ACCOUNT_EMAIL)
y_password_login.send_keys(ACCOUNT_PASSWORD)
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type^='submit']"))).click()

message = f"My download speed is {download_speed} and my upload is {upload_speed}. This is unacceptable!"

tweet_body = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[id^='tweet-compose']")))
tweet_body.send_keys(message)
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[id^='post-btn']"))).click()