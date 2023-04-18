import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")
browser = webdriver.Chrome(options=chrome_options)


class TestRegistration(unittest.TestCase):
    def test_part1(self):
        link = "http://suninjuly.github.io/registration1.html"
        try:
            browser.get(link)

            input_first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input_first_name.send_keys('Maya')
            input_last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input_last_name.send_keys('Orlovskaya')
            input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input_email.send_keys('orlovsky-maya@mail.ru')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assertEquals проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            result_text = "Congratulations! You have successfully registered!"
            self.assertEqual(result_text, welcome_text, "incorrect registration text")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            # browser.quit()

    def test_part2(self):
        link = "http://suninjuly.github.io/registration2.html"
        try:
            browser.get(link)

            input_first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input_first_name.send_keys('Maya')
            input_last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input_last_name.send_keys('Orlovskaya')
            input_email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input_email.send_keys('orlovsky-maya@mail.ru')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assertEquals проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            result_text = "Congratulations! You have successfully registered!"
            self.assertEqual(result_text, welcome_text, "incorrect registration text")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
