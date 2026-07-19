from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


class AuthorizationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.LOGIN_PAGE
    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTRATION_BUTTON = (By.XPATH, "//a[@class='outlined medium button sign-up-button']")
    TOASTER = (By.XPATH, "//div[@data-content]")
    PASSWORD_RESTORE = (By.XPATH, "//a[@class='password-restore']")

    def wait_loader(self):
        self.wait_for_element(self.USERNAME_FIELD)
        self.wait_for_element_invisible(self.SPINNER)

    def enter_email(self):
        email = os.getenv("LOGIN")
        self.type_text(self.USERNAME_FIELD, email)

    def enter_password(self):
        password = os.getenv("PASSWORD")
        self.type_text(self.PASSWORD_FIELD, password)

    def enter_wrong_email(self, email='wrong@password.ru'):
        self.type_text(self.USERNAME_FIELD, email)

    def enter_wrong_password(self, password='1234567890'):
        self.type_text(self.PASSWORD_FIELD, password)

    def click_button_enter(self):
        self.click(self.LOGIN_BUTTON)

    def visible_toaster(self):
        self.wait_for_element_visible(self.TOASTER)

    def text_toaster_authorization(self):
        return self.find_element(self.TOASTER).text
    
    def enter_incorrect_email(self, email='incorrect.password.ru'):
        self.type_text(self.USERNAME_FIELD, email)

    def enter_shot_password(self, password='1234'):
        self.type_text(self.USERNAME_FIELD, password)

    def check_disabled_button_login(self):
        self.is_button_disabled(self.LOGIN_BUTTON)

    def click_password_restore(self):
        self.click(self.PASSWORD_RESTORE)

