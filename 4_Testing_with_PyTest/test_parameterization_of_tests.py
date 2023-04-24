# Task: parameterization of tests

# Command: pytest -v 4_Testing_with_PyTest/test_parameterization_of_tests.py


import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")


# Function for calculation

def calc():
    return math.log(int(time.time()))


# Fixture to open and close browser

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


# Fixture to open link, login and calculate

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    # Open browser
    def test_open_link(self, browser, link):
        browser.get(link)

    # Find Login button on page
    def test_find_and_click_login_button_on_page(self, browser, link):
        login_button_on_page = browser.find_element(By.ID, 'ember33')
        login_button_on_page.click()

    # Find and fill in email and password fields
    def test_find_and_fill_email_and_password_fields(self, browser, link):
        email_field = browser.find_element(By.ID, 'id_login_email')
        email_field.send_keys('')
        password_field = browser.find_element(By.ID, 'id_login_password')
        password_field.send_keys('')

    # Find login button on popup
    def test_find_login_button_on_popup_and_clik(self, browser, link):
        login_button_on_popup = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
        login_button_on_popup.click()

    # Find input field and fill in answer
    def test_find_input_field_and_fill_answer(self, browser, link):
        answer_field = browser.find_element(By.ID, 'ember86')
        answer_field.send_keys(calc())

    # Find submit button and click
    def test_find_submit_button_and_click(self, browser, link):
        submit_button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        submit_button.click()

    # Find message filed and check result message
    def test_find_message_filed_and_check_result_message(self, browser, link):
        message_field = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
        message = message_field.text
        correct_message = 'Correct!'
        assert message == correct_message, "Answer is not correct! Try again"
