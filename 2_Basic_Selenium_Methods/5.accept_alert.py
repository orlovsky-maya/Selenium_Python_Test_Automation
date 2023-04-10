from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from math import *

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return log(abs(12 * sin(x)))


try:
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Find the button and click
    button_first = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button_first.click()

    # Switch to the alert and confirm
    alert = browser.switch_to.alert
    alert.accept()

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
    time.sleep(30)
    browser.quit()

