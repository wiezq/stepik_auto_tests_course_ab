from selenium import webdriver
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    math_text = browser.find_element_by_id("treasure")
    math_text = math_text.get_attribute("valuex")
    math_answer = calc(math_text)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(math_answer)

    input_checkbox = browser.find_element_by_id("robotCheckbox")
    input_checkbox.click()

    input_radiobox = browser.find_element_by_css_selector("input[value='robots']")
    input_radiobox.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    time.sleep(5)
    browser.quit()
