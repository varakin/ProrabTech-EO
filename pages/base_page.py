from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver



class BasePage:

    HOST = "https://prorabtech.ru"
    LOGIN_PAGE = f"{HOST}/login"
    DASHBOARD_PAGE = f"{HOST}/constructions"
    PROFILE_PAGE = f"{HOST}/profile"
    PASSWORD_RESTORE_PAGE = f"{HOST}/password-restore-email"

    PROFILE_BUTTON = (By.XPATH, "//div[@class='avatar-block']")
    SPINNER = (By.XPATH, "//dialog[@class='loading-dialog']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        self.find_element(locator).click()
    
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
