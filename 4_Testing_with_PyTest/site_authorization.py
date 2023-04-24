from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


link = 'https://stepik.org/lesson/236895/step/1'

try:
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5)
    browser.get(link)

    # Find Login button on page
    login_button_on_page = browser.find_element(By.ID, 'ember33')
    login_button_on_page.click()

    # Find and fill in email and password fields
    email_field = browser.find_element(By.ID, 'id_login_email')
    email_field.send_keys('')
    password_field = browser.find_element(By.ID, 'id_login_password')
    password_field.send_keys('')

    # Find login button on popup
    login_button_on_popup = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
    login_button_on_popup.click()


finally:
    time.sleep(5)
    browser.quit()
