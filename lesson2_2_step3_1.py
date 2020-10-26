from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = int(browser.find_element_by_id("num1").text)
    number2 = int(browser.find_element_by_id("num2").text)
    summa = str(number1 + number2)
    #print(summa)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)
    browser.find_element_by_class_name("btn").click()

    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
