from pages.authorization_page import AuthorizationPage
from pages.dashboard_page import DashboardPage
from pages.profile_page import ProfilePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization_and_logout(driver):
    authorization = AuthorizationPage(driver)
    dashboard = DashboardPage(driver)
    profile = ProfilePage(driver)
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


def test_wrong_email(driver):
    authorization = AuthorizationPage(driver)
    dashboard = DashboardPage(driver)
    profile = ProfilePage(driver)
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_wrong_email()
    authorization.enter_password()
    authorization.click_button_enter()
    authorization.visible_toaster()
    assert authorization.text_toaster_authorization() == 'Пользователь не найден'

def test_wrong_password(driver):
    authorization = AuthorizationPage(driver)
    dashboard = DashboardPage(driver)
    profile = ProfilePage(driver)
    authorization.open()
    authorization.is_opened()
    authorization.wait_loader()
    authorization.enter_email()
    authorization.enter_wrong_password()
    authorization.click_button_enter()
    authorization.visible_toaster()
    assert authorization.text_toaster_authorization() == 'Пароль неверный'

