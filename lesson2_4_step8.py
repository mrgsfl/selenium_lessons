from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #Ждем, когда цена станет $100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    #Находим и нажимаем на кнопку "Book"
    book_btn = browser.find_element_by_id("book")
    book_btn.click()

    #Решаем математическую задачу:
    x_element = browser.find_element_by_id('input_value').text
    x = calc(x_element)
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(x)
    
    submit_btn = browser.find_element_by_id("solve")
    submit_btn.click()
    

finally:
    time.sleep(10)
    browser.quit()
