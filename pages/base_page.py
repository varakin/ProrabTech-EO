from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import os


name_new_object = str(datetime.now().time())

class BasePage:

    HOST = 'https://prorabtech.ru'
    LOGIN_PAGE = f'{HOST}/login'
    DASHBOARD_PAGE = f'{HOST}/constructions'
    PROFILE_PAGE = f'{HOST}/profile'
    PASSWORD_RESTORE_PAGE = f'{HOST}/password-restore-email'
    NEW_OBJECT_PAGE = f'{HOST}/constructions/add'
    OBJECT_HOME_PAGE = f'{HOST}/constructions/96/home'

    PROFILE_BUTTON = (By.XPATH, '//div[@class="avatar-block"]')
    SPINNER = (By.XPATH, '//dialog[@class="loading-dialog"][not(@open)]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        self.find_element(locator).click()

    def click_button_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        self.find_element(locator).send_keys(text)
    
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def is_button_disabled(self, locator):
        return self.find_element(locator).is_enabled()
    
    def result_text(self, locator):
        return self.find_element(locator).text

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def click_profile_button(self):
        self.click(self.PROFILE_BUTTON)

    def enter_email(self):
        email = os.getenv("LOGIN")
        self.type_text(self.USERNAME_FIELD, email)

    def enter_password(self):
        password = os.getenv("PASSWORD")
        self.type_text(self.PASSWORD_FIELD, password)

    def wait_loader(self):
        self.wait_for_element(self.SPINNER)

    def clear(self, locator):
        self.find_element(locator).clear()

    def auth_test10(self):
        self.open()
        self.wait_loader()
        self.enter_email()
        self.enter_password()
        self.click(self.LOGIN_BUTTON)
        self.wait.until(EC.url_to_be(self.DASHBOARD_PAGE))
        self.wait_loader()


