import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.regression
@pytest.mark.smoke
def test_new_object(driver, authorization, dashboard, object_home_page):
    authorization.auth_test10()
    object_home_page.enter_object_for_tests()
    object_home_page.wait_loader()
    object_home_page.checking_description()

@pytest.mark.regression
@pytest.mark.smoke
def test_element_of_page(driver, authorization, dashboard, object_home_page):
    authorization.auth_test10()
    object_home_page.enter_object_for_tests()
    object_home_page.wait_loader()
    object_home_page.check_name_menu()

@pytest.mark.regression
@pytest.mark.smoke
def test_return_dashboard(driver, authorization, dashboard, object_home_page):
    authorization.auth_test10()
    object_home_page.enter_object_for_tests()
    object_home_page.wait_loader()
    object_home_page.return_to_dashboard()
    dashboard.is_opened()
    dashboard.wait_loader()
   

    