# Task: parameterization of tests by using login page
# Command: pytest -v 4_Testing_with_PyTest/test_parameterization_of_tests2.py

import math
import time
import pytest
from selenium import webdriver
from login_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test data
user = ''
password = ''


# Fixture to open and close browser
@pytest.fixture(scope="function")
def browser():
    print('Start')
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
    print('Finish')


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1"])
def test_open_link_login_calculate_check_result(browser, link):
    browser.get(link)
    print(f'{link} link opened')

    # Find Login button on page
    login_button_on_page = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'ember33')))
    login_button_on_page.click()
    print(f'{link} login button click')

    # Login to the site
    login = Login_page(browser)
    login.authorization(user, password)
    print('User is logged in')

    # Find input field and fill in by answer
    # time.sleep(7)
    answer_field = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                     '.ember-text-area')))
    answer = math.log(int(time.time()))
    answer_field.send_keys(answer)
    print(answer)
    print('Answer is calculated')
    time.sleep(2)

    # Find submit button and click
    submit_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                '.submit-submission')))
    submit_button.click()
    print('Answer is submitted')

    # Find message filed and check result message
    message_field = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                      '.smart-hints__hint')))
    message = message_field.text
    print(f'{link} shows {message}')
    correct_message = 'Correct!'
    assert message == correct_message, message
