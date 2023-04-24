# Using @pytest.mark.parametrize('parameter', list of values) for
# parameterization of tests class

# Command: pytest -s -v 4_Testing_with_PyTest/test_fixture10.py


import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        # этот тест тоже запустится дважды
        pass
