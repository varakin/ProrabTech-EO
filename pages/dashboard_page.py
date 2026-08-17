from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import name_new_object


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.DASHBOARD_PAGE
    NEW_OBJECT_BUTTON = (By.XPATH, '//a[@class="primary medium button add-btn"]')
    NAME_NEW_OBJECT = (By.XPATH, '//div[@class="name"][1]')
    NUMBERS_OBJECTS = (By.XPATH, '//span[@class="count"]')
    LIST_OBJECTS = (By.XPATH, '//div[@class="constructions"]/a')


    def create_new_object(self):
        self.click(self.NEW_OBJECT_BUTTON)

    def check_name_new_object(self):
        assert self.result_text(self.NAME_NEW_OBJECT) == f'autotest object № "{name_new_object}"'

    def equality_numbers_and_chunks(self):
        numbers = int(self.result_text(self.NUMBERS_OBJECTS))
        count_objects = len(self.find_elements(self.LIST_OBJECTS)) - 1
        assert numbers == count_objects

    # def enter_created_object(self):

