from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects1.html"

try:
    browser.get(link)
    x = browser.find_element_by_css_selector(".container .nowrap:nth-child(2)").text
    y = browser.find_element_by_css_selector(".container .nowrap:nth-child(4)").text
    result = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()