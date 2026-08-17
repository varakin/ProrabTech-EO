from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ObjectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ADD_STAGES_BUTTON = (By.XPATH, '//button[@class="subtle medium button add-button"]')
    NAME_STAGE_FIELD = (By.XPATH, '//input[@autocomplete="one-time-code"]')
    CREATE_STAGE_BUTTON = (By.XPATH, '//div[@class="success input"]/following-sibling::button')
    NEW_STAGE_BUTTON = (By.XPATH, '//span[text()="New Stage"]')
    CREATE_NEW_TASK_BUTTON = (By.XPATH, '//button[@class="subtle medium button add-button level level-2"]')
    NAME_TASK_FIELD = (By.XPATH, '//input[@placeholder="Название задачи"]')
    SAVE_NEW_TASK_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    NAME_NEW_TASK = (By.XPATH, '//span[@class="title"]')
    DELETE_STAGE_BUTTON = (By.XPATH, '//span[text()="New Stage"]/../following-sibling::div[@class="cell button-wrapper"]//span[text()="Удалить"]/../..')
    CONFIRM_DELETE_STAGE = (By.XPATH, '//button[@class="primary-danger medium button"]')

    def check_add_stage_button(self):
        self.find_element(self.ADD_STAGES_BUTTON)

    def create_new_stage(self):
        self.wait_for_element_clickable(self.ADD_STAGES_BUTTON)
        self.click_button_js(self.ADD_STAGES_BUTTON)
        self.wait_for_element_clickable(self.NAME_STAGE_FIELD)
        self.click(self.NAME_STAGE_FIELD)
        self.type_text(self.NAME_STAGE_FIELD, 'New Stage')
        # sleep(5)
        # self.wait_for_element_clickable(self.CREATE_STAGE_BUTTON)
        self.click_button_js(self.CREATE_STAGE_BUTTON)

    def create_new_task(self):
        self.wait_for_element_clickable(self.NEW_STAGE_BUTTON)
        self.click_button_js(self.NEW_STAGE_BUTTON)
        self.wait_loader()
        self.wait_for_element_clickable(self.CREATE_NEW_TASK_BUTTON)
        self.click_button_js(self.CREATE_NEW_TASK_BUTTON)
        self.wait_loader()
        # self.wait_for_element_clickable(self.NAME_TASK_FIELD)
        # self.wait_for_element_clickable(self.SAVE_NEW_TASK_BUTTON)
        self.type_text(self.NAME_TASK_FIELD, 'New Task')
        self.click(self.SAVE_NEW_TASK_BUTTON)
        self.wait_loader()
        # sleep(5)
        assert 'New Task' in self.result_text(self.NAME_NEW_TASK)

    def delete_stage(self):
        self.click_button_js(self.DELETE_STAGE_BUTTON)
        self.wait_for_element_clickable(self.CONFIRM_DELETE_STAGE)
        self.click_button_js(self.CONFIRM_DELETE_STAGE)
        self.wait_loader()
        elements = self.find_elements(self.NEW_STAGE_BUTTON)
        assert len(elements) == 0


