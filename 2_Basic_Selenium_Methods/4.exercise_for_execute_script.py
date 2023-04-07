from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from math import *

link = 'http://suninjuly.github.io/execute_script.html'


# Function for calculation
def calc(x):
    return log(abs(12 * sin(x)))


try:
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Find x value and calculate
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    result = calc(int(x))

    # Scroll the page
    field = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(result)

    # Check checkbox
    check_box = browser.find_element(By.ID, 'robotCheckbox')
    check_box.click()

    # Select redio button
    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()

    # Click Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()



