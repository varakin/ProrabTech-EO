from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import name_new_object

class NewObjectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.NEW_OBJECT_PAGE
    NAME_OBJECT_FIELD = (By.XPATH, "//input[@id='name']")
    SAVE_BUTTON = (By.XPATH, "//button[@class='primary medium button']")
    HOME_NAME_NEW_OBJECT = (By.XPATH, "//div[@class='main-part-title']")
    RETURN_DASHBOARD_BUTTON = (By.XPATH, "//button[@class='subtle medium circle icon-button'][1]")

    def enter_name_object(self):
        self.clear(self.NAME_OBJECT_FIELD)
        self.type_text(self.NAME_OBJECT_FIELD, f'autotest object № "{name_new_object}"')

    def saved_new_object(self):
        self.click(self.SAVE_BUTTON)

    def check_home_page_new_object(self):
        assert f'autotest object № "{name_new_object}"' == self.result_text(self.HOME_NAME_NEW_OBJECT)

    def return_dashboard(self):
        self.click(self.RETURN_DASHBOARD_BUTTON)