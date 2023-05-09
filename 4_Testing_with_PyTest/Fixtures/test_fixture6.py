# Inversion:
# Command: pytest -s -v -m "not smoke" 4_Testing_with_PyTest/test_fixture6.py

# Combining tests with different marks:
# Command: pytest -s -v -m "smoke or regression" 4_Testing_with_PyTest/test_fixture6.py

# Selection of tests with multiple markings:
# Command: pytest -s -v -m "smoke and win10" 4_Testing_with_PyTest/test_fixture6.py


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
