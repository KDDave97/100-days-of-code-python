from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

upcoming_events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
upcoming_events_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

upcoming_events = {}

for event in upcoming_events_time:
    print(event.text)

for event in upcoming_events_name[1:]:
    print(event.text)

for i in range(len(upcoming_events_time)):
    upcoming_events[i] = {
        "time": upcoming_events_time[i].text,
        "name": upcoming_events_name[i].text
    }



print(upcoming_events)



driver.quit()