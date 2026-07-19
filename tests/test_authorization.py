import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.regression
@pytest.mark.smoke
def test_authorization_and_logout(driver, authorization, dashboard, profile):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_email()
    authorization.enter_password()
    authorization.click_button_enter()
    dashboard.is_opened()
    dashboard.click_profile_button()
    profile.is_opened()
    profile.click_logout_button()
    authorization.is_opened()


@pytest.mark.regression
def test_wrong_email(driver, authorization):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_wrong_email()
    authorization.enter_password()
    authorization.click_button_enter()
    authorization.visible_toaster()
    assert authorization.text_toaster_authorization() == 'Пользователь не найден'


@pytest.mark.regression
def test_wrong_password(driver, authorization):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_email()
    authorization.enter_wrong_password()
    authorization.click_button_enter()
    authorization.visible_toaster()
    assert authorization.text_toaster_authorization() == 'Пароль неверный'


@pytest.mark.regression
def test_incorrect_email(driver, authorization):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_incorrect_email()
    authorization.enter_password()
    authorization.check_disabled_button_login()


@pytest.mark.regression
def test_shot_password(driver, authorization):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_email()
    authorization.enter_shot_password()
    authorization.check_disabled_button_login()

@pytest.mark.regression
def test_password_restore_cancel(driver, authorization, password_restore):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.click_password_restore()
    password_restore.is_opened()
    password_restore.click_button_cancel()
    authorization.is_opened()

@pytest.mark.regression
@pytest.mark.smoke
def test_password_restore_send_email(driver, authorization, password_restore):
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.click_password_restore()
    password_restore.is_opened()
    password_restore.enter_email()
    password_restore.click_button_send()
    password_restore.check_message_restore()
    password_restore.click_return_login_page_button()
    authorization.is_opened()


    


