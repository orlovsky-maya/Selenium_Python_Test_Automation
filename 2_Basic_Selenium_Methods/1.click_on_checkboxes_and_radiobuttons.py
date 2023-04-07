from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.chrome.options import Options


# Function for calculation
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://suninjuly.github.io/math.html'

try:
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Get x value + calculation using fun calc()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(int(x))

    # Input x value in input field
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Check checkbox
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    # Select radiobutton
    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    # Click Submit button

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()


finally:
    time.sleep(30)
    browser.quit()

