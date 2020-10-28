import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver

import time
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element_by_id('input_value').text
    x = calc(x_element)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(x)
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True

finally:
    time.sleep(10)
    browser.quit()
