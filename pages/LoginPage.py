import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    UPPER_ENTRANCE_BUTTON = (By.XPATH, '//*[@data-l="t,login_tab"]')
    UPPER_QRCODE_BUTTON = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BY_QRCODE_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    CANNOT_LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    LOGIN_THROUGH_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_THROUGH_MAILRU = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_THROUGH_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    @allure.step('Проверяем элементы на главной странице')
    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.UPPER_ENTRANCE_BUTTON)
        self.find_element(LoginPageLocators.UPPER_QRCODE_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BY_QRCODE_BUTTON)
        self.find_element(LoginPageLocators.CANNOT_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_THROUGH_VK)
        self.find_element(LoginPageLocators.LOGIN_THROUGH_MAILRU)
        self.find_element(LoginPageLocators.LOGIN_THROUGH_YANDEX)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
