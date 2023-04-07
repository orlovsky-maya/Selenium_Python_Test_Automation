from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Fill mandatory field
    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name.send_keys('Maya')

    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys('Orlovskaya')

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('orlovsky-maya@mail.ru')

    # Upload a file
    file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_to_upload.txt')
    file.send_keys(file_path)

    # Click Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()