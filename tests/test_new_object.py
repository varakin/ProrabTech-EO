import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.regression
@pytest.mark.smoke
def test_new_object(driver, authorization, dashboard, new_object):
    authorization.auth_test10()
    dashboard.create_new_object()
    new_object.is_opened()
    new_object.wait_loader()
    new_object.enter_name_object()
    new_object.saved_new_object()
    new_object.wait_loader()
    new_object.check_home_page_new_object()
    new_object.return_dashboard()
    dashboard.wait_loader()
    dashboard.check_name_new_object()

@pytest.mark.regression
@pytest.mark.smoke
def test_delete_new_object(driver, authorization, dashboard, new_object):
    authorization.auth_test10()
    new_object.delete_created_object()

