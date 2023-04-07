from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options

link = 'http://suninjuly.github.io/selects1.html'

try:
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--remote-debugging-port=9515")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    # Find x and y and calculate the sum
    x_element = browser.find_element(By.ID, 'num1')
    y_element = browser.find_element(By.ID, 'num2')
    x = x_element.text
    y = y_element.text
    summa = int(x) + int(y)

    # Find summa in dropdown using Select library
    # select_dropdown = Select(browser.find_element(By.ID, "dropdown"))
    # select_dropdown.select_by_visible_text(str(summa))

    # Find summa in dropdown
    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f"[value = '{summa}']").click()

    # Find and click Submit
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()
