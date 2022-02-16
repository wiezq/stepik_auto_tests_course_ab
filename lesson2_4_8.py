from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()

browser.get(link)
button = browser.find_element_by_id("book")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()

WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.ID, "input_value"))
)

x = browser.find_element_by_id("input_value").text
x = str(math.log(abs(12 * math.sin(int(x)))))

browser.find_element_by_id("answer").send_keys(x)

browser.find_element_by_id("solve").click()
