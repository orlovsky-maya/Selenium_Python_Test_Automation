# Using @pytest.mark.parametrize('parameter', list of values) for parameterization of tests

# Command: pytest -s -v 4_Testing_with_PyTest/test_fixture9.py

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")