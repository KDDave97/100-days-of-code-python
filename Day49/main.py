from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

ACCOUNT_EMAIL = os.environ.get("MY_EMAIL")
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"
BOOKED_CLASSES = 0
ALREADY_BOOKED = 0
WAITLISTED = 0
ALREADY_WAITLISTED = 0

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

days = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='day-group-']")))
for day in days:
    day_text = day.find_element(By.CSS_SELECTOR, value="h2[id^='day-title-']").text
    if "Tue" in day_text or "Thu" in day_text:
        cards = day.find_elements(By.CSS_SELECTOR, value="div[id^='class-card-']")
        for card in cards:
            time_text = card.find_element(By.CSS_SELECTOR, value="p[id^='class-time-']").text
            if "6:00 PM" in time_text:
                book_class_button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                if book_class_button.text == "Book Class":
                    book_class_button.click()
                    BOOKED_CLASSES += 1
                    print(f"Booked class: {card.find_element(By.TAG_NAME, value="h3").text}, at {time_text.split()[1]} {day_text}")
                elif book_class_button.text == "Join Waitlist":
                    book_class_button.click()
                    WAITLISTED += 1
                    print(f"Joined waitlist: {card.find_element(By.TAG_NAME, value="h3").text}, at {time_text.split()[1]} {day_text}")
                elif book_class_button.text == "Booked":
                    ALREADY_BOOKED += 1
                    print(f"Already booked: {card.find_element(By.TAG_NAME, value="h3").text}, at {time_text.split()[1]} {day_text}")
                elif book_class_button.text == "Waitlisted":
                    ALREADY_WAITLISTED += 1
                    print(f"Already on waitlist: {card.find_element(By.TAG_NAME, value="h3").text} at {time_text.split()[1]} {day_text}")

print(f"""
---Booking Summary---
Classes booked: {BOOKED_CLASSES}
Waitlist joined: {WAITLISTED}
Already booked: {ALREADY_BOOKED}
Already on waitlist: {ALREADY_WAITLISTED}
""")




