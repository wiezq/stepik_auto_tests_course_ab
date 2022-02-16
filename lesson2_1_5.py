from selenium import webdriver
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    math_text = browser.find_element_by_css_selector(".form-group .nowrap:nth-child(2)")
    math_answer = calc(math_text.text)

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
