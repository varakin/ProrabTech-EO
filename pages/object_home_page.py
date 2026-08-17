from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ObjectHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PAGE_URL = BasePage.OBJECT_HOME_PAGE
    OBJECT_FOR_TESTS = (By.XPATH, '//div[@class="constructions"]//div[text()="Object with moсk data (autotest)"]')
    DISCRIPTION_OBJECT = (By.XPATH, '//div[@class="main-part-description"]')
    TASKS_AND_STAGES_BUTTON = (By.XPATH, '//div[@class="container"]/a[1]/span')
    USERS_BUTTON = (By.XPATH, '//div[@class="container"]/a[2]/span')
    ROLES_BUTTON = (By.XPATH, '//div[@class="container"]/a[3]/span')
    PASSPORT_OBJECT_BUTTON = (By.XPATH, '//div[@class="container"]/a[4]/span')
    NOTIFICATIONS_BUTTON = (By.XPATH, '//div[@class="container"]/a[5]/span')
    SETTINGS_BUTTON = (By.XPATH, '//div[@class="container"]/a[6]/span')
    
    RETURN_BUTTON = (By.XPATH, '//div[@class="navbar"]/button')

    def enter_object_for_tests(self):
        self.click(self.OBJECT_FOR_TESTS)

    def checking_description(self):
        assert self.result_text(self.DISCRIPTION_OBJECT) == 'Object for autotests with mock data'

    def check_name_menu(self):
        assert self.result_text(self.TASKS_AND_STAGES_BUTTON) == 'Задачи и этапы'
        assert self.result_text(self.USERS_BUTTON) == 'Люди'  
        assert self.result_text(self.ROLES_BUTTON) == 'Роли' 
        assert self.result_text(self.PASSPORT_OBJECT_BUTTON) == 'Паспорт объекта' 
        assert self.result_text(self.NOTIFICATIONS_BUTTON) == 'Уведомления'
        assert self.result_text(self.SETTINGS_BUTTON) == 'Настройки'

    def return_to_dashboard(self):
        self.click(self.RETURN_BUTTON)

    @property
    def enter_object_page(self):
        self.click(self.TASKS_AND_STAGES_BUTTON)