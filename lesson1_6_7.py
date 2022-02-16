from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"
try:

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivansd")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrovasd")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolenskasd")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russiaasdas")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()
finally:
    time.sleep(5)
    browser.quit()