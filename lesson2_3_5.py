from selenium import webdriver
from time import sleep
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()

    browser.get(link)

    browser.find_element_by_tag_name("button").click()

    old_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    x = str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element_by_id("answer").send_keys(x)

    browser.find_element_by_class_name("btn").click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    sleep(4)
    browser.quit()
