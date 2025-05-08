import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class VKEcosystemPageLocators:
    TITLE_LABEL = (By.XPATH, '(//a[@aria-label="VK"])[1]')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    @allure.step('Проверяем элементы на главной странице')
    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.TITLE_LABEL)