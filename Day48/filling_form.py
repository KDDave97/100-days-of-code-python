from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

textbox_list = driver.find_elements(By.CSS_SELECTOR, value="input")

first_name = textbox_list[0]
last_name = textbox_list[1]
email = textbox_list[2]

first_name.send_keys("David")
last_name.send_keys("Kurucz")
email.send_keys("kuruczdavid997@gmail.com")