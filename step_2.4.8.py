from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(15)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button1 = browser.find_element_by_id("book")
    button1.click()

    # ждем загрузки страницы
    time.sleep(0.5)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    button = browser.find_element_by_id("solve")
    button.click()
    #time.sleep(30)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла