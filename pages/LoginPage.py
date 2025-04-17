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
    REGISTER_BUTTON = (By.XPATH, '//*[@data-l="t,register"]')
    LOGIN_THROUGH_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_THROUGH_MAILRU = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_THROUGH_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')


class LoginPageHelper(BasePage)
    pass
