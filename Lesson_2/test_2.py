from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import yaml
from time import sleep
import time
from selenium.webdriver.common.keys import Keys


# Загрузка данных для теста
with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def test_invalid_login(site, selector_login, selector_passwd, selector_button, selector_error):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys("test")
    
    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys("test")
    
    btn = site.find_element("css", selector_button)
    btn.click()

    err_text3 = site.find_element("xpath", selector_error)
    assert err_text3.text == "401"

def test_login_and_add_post(site, selector_login, selector_passwd, selector_button, selector_home, selector_create_post_button, selector_title_input, selector_description_input, selector_submit_post_button):
    # Шаг 2: авторизация с допустимыми данными
    input1 = site.find_element("xpath", selector_login)
    input1.clear()
    input1.send_keys(testdata.get("username"))

    input2 = site.find_element("xpath", selector_passwd)
    input2.clear()
    input2.send_keys(testdata.get("password"))

    btn = site.find_element("css", selector_button)
    btn.click()

    home_path = site.find_element("xpath", selector_home)
    assert home_path.text == "Home", "test FAIL"

    # Шаг 3: создание поста
    create_post_button = WebDriverWait(site, 10).until(
        EC.element_to_be_clickable((By.XPATH, selector_create_post_button))
    )
    create_post_button.click()

    title_input = WebDriverWait(site, 10).until(
        EC.element_to_be_clickable((By.XPATH, selector_title_input))
    )
    title_input.clear()  # Очищаем поле, если там уже что-то есть
    title_input.click()  # Кликаем на поле, чтобы активировать его
    title_input.send_keys(Keys.CONTROL + 'a')  # Выделить всё (для Windows)
    title_input.send_keys(Keys.DELETE)  # Удалить выделенное
    title_input.send_keys("Это тестовый заголовок")  # Вводим текст

    description_input = WebDriverWait(site, 10).until(
        EC.element_to_be_clickable((By.XPATH, selector_description_input))
    )
    description_input.send_keys("Это тестовое описание")

    submit_button = site.find_element("xpath", selector_submit_post_button)
    submit_button.click()

    # Здесь можно добавить задержку для надежности
    time.sleep(3)

    post_title = WebDriverWait(site, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/main/div/div[1]/h1"))
    )

    assert post_title.text == "Это тестовый заголовок", "Post creation failed or title doesn't match"

if __name__ == "__main__":
    pytest.main(["-vv"])


