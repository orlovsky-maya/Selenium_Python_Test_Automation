# Login page is used by test_parameterization_of_tests2.py

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")


class Login_page:
    def __init__(self, browser):
        self.browser = browser

    def authorization(self, login_name, login_password):
        # Find and fill in email and password fields
        email_field = self.browser.find_element(By.ID, 'id_login_email')
        email_field.send_keys(login_name)

        password_field = self.browser.find_element(By.ID, 'id_login_password')
        password_field.send_keys(login_password)

        # Find login button on popup
        login_button_on_popup = self.browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
        login_button_on_popup.click()

