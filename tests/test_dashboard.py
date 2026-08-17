import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.regression
@pytest.mark.smoke
def test_equality_number_chunks(driver, authorization, dashboard, profile):
    authorization.auth_test10()
    dashboard.equality_numbers_and_chunks()
    
    

