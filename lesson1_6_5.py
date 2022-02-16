from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"
try:

    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element_by_partial_link_text('224592')
    link.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivansd")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrovasd")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolenkasd")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russiaasdas")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    time.sleep(10)
    browser.quit()

