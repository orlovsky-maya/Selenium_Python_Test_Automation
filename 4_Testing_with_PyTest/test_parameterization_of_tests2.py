# Task: parameterization of tests
import datetime
# Command: pytest -v 4_Testing_with_PyTest/test_parameterization_of_tests2.py


import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")
from selenium.webdriver import ActionChains, Keys


# Function for calculation

def calc():
    return math.log(int(time.time()))


# Fixture to open and close browser

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()


# Fixture to open link, login and calculate

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1"])
def test_login_calculate_input_answer_get_massage(browser, link):
    # Open browser
    browser.implicitly_wait(6)
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

    # Find input field and fill in answer
    answer_field = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
    answer_field.send_keys(str(calc()))

    # Find submit button and click
    submit_button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    submit_button.click()
    # Find message filed and check result message
    message_field = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
    message = message_field.text
    correct_message = 'Correct!'
    assert message == correct_message, message
    print(message)
