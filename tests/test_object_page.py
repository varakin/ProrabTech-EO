import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.regression
@pytest.mark.smoke
def test_check_add_stage_button(driver, authorization, dashboard, object_home_page, object_page):
    authorization.auth_test10()
    object_home_page.enter_object_for_tests()
    object_home_page.wait_loader()
    object_home_page.enter_object_page
    object_page.check_add_stage_button()

@pytest.mark.regression
@pytest.mark.smoke
def test_add_new_stage(driver, authorization, dashboard, object_home_page, object_page):
    authorization.auth_test10()
    object_home_page.enter_object_for_tests()
    object_home_page.wait_loader()
    object_home_page.enter_object_page
    object_page.create_new_stage()

@pytest.mark.regression
@pytest.mark.smoke
def test_add_new_task(driver, authorization, dashboard, object_home_page, object_page):
    authorization.auth_test10()
    object_home_page.enter_object_for_tests()
    object_home_page.wait_loader()
    object_home_page.enter_object_page
    object_page.create_new_task()


@pytest.mark.regression
@pytest.mark.smoke
def test_delete_stage(driver, authorization, dashboard, object_home_page, object_page):
    authorization.auth_test10()
    object_home_page.enter_object_for_tests()
    object_home_page.wait_loader()
    object_home_page.enter_object_page
    object_page.delete_stage()   
