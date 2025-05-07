import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    with allure.step("Запускаем браузер Chrome"):
        driver = webdriver.Chrome()
        yield driver
        with allure.step("Закрываем браузер"):
            driver.quit()
