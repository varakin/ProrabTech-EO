from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.DASHBOARD_PAGE

    def wait_loader(self):
        self.wait_for_element_invisible(self.SPINNER)
