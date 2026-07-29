import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.regression
@pytest.mark.smoke
def test_equality_number_chunks(driver, authorization, dashboard, profile):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_email()
    authorization.enter_password()
    authorization.click_button_enter()
    dashboard.is_opened()
    dashboard.wait_loader()
    dashboard.equality_numbers_and_chunks()
    
    

