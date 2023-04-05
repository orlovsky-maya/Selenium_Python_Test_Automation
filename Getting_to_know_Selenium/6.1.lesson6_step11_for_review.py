from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

try:
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    link = "http://suninjuly.github.io/registration2.html"
    # link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
    input3.send_keys("abc@gmail.com")
    input4 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control first']")
    input4.send_keys("89998886655")
    input5 = browser.find_element(By.XPATH, "//div[@class='second_block']//input[@class='form-control second']")
    input5.send_keys("Улица Пушкина, дом Колотушкина")

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//div//button")
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