from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import *

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return log(abs(12 * sin(x)))


try:
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Wait price 100 and book
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button_book = browser.find_element(By.ID, 'book')
    button_book.click()

    # Calculate of the problem
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(int(x))

    # Input the result and submit
    field = browser.find_element(By.ID, "answer")
    field.send_keys(result)
    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_submit.click()


finally:
    time.sleep(10)
    browser.quit()


