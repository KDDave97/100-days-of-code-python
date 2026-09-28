from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

ACCOUNT_EMAIL = os.environ.get("MY_EMAIL")
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_textbox = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_textbox.send_keys(ACCOUNT_EMAIL)
password_textbox = wait.until(ec.presence_of_element_located((By.ID, "password-input")))
password_textbox.send_keys(ACCOUNT_PASSWORD)
login_button = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
login_button.click()

tuesday = driver.find_element(By.CSS_SELECTOR, value="")
tuesday.click()




