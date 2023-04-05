from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

try:
    # Первая версия страницы регистрации - тест проходит
    link = "http://suninjuly.github.io/registration1.html"

    # Вторая версия страницы регистрации - тест падает с ошибкой NoSuchElementException
    # link = "http://suninjuly.github.io/registration2.html"

    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".second[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".third[placeholder='Input your email']")
    input3.send_keys("petrov@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, ".first[placeholder='Input your phone:']")
    input4.send_keys("+74951234567")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second[placeholder='Input your address:']")
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()