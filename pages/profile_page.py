from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class ProfilePage(BasePage):
        
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.PROFILE_PAGE
    LOGOUT_BUTTON = (By.XPATH, "//button[@class='subtle medium button']")

    def click_logout_button(self):
        self.wait_for_element_clickable(self.LOGOUT_BUTTON)
        self.find_element(self.LOGOUT_BUTTON)
        self.click(self.LOGOUT_BUTTON)
