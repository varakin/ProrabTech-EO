from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class PasswordRestorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.PASSWORD_RESTORE_PAGE
    CANCEL_BUTTON = (By.XPATH, "//a[@class='subtle-black medium button']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    SEND_BUTTON = (By.XPATH, "//button[@class='primary-outlined medium button']")
    TEXT_SEND_EMAIL_RESTORE = (By.XPATH, "//form[@class='auth-page']/p")
    RETURN_LOGIN_PAGE_BUTTON = (By.XPATH, "//button[@class='primary medium button']")

    def click_button_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def enter_email(self, email='test10@lamantin.spb.ru'):
        self.type_text(self.EMAIL_FIELD, email)

    def click_button_send(self):
        self.click(self.SEND_BUTTON)

    def check_message_restore(self):
        assert self.result_text(self.TEXT_SEND_EMAIL_RESTORE) == 'Письмо со ссылкой для восстановления пароля отправлено на вашу почту'

    def click_return_login_page_button(self):
        self.click(self.RETURN_LOGIN_PAGE_BUTTON)