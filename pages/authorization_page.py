from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class AuthorizationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.LOGIN_PAGE
    USERNAME_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTRATION_BUTTON = (By.XPATH, "//a[@class='outlined medium button sign-up-button']")
    TOASTER = (By.XPATH, "//div[@data-content]")

    def wait_loader(self):
        self.wait_for_element(self.USERNAME_FIELD)
        self.wait_for_element_invisible(self.SPINNER)

    def enter_email(self, email='test10@lamantin.spb.ru'):
        self.type_text(self.USERNAME_FIELD, email)

    def enter_password(self, password='lamantin2026'):
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
