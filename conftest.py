import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.authorization_page import AuthorizationPage
from pages.dashboard_page import DashboardPage
from pages.profile_page import ProfilePage
from pages.password_restore import PasswordRestorePage
from pages.new_object_page import NewObjectPage
from pages.object_home_page import ObjectHomePage
from pages.object_page import ObjectPage
import os
from dotenv import load_dotenv


load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless") # включить для ci/cd
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    return AuthorizationPage(driver)

@pytest.fixture
def dashboard(driver):
    return DashboardPage(driver)

@pytest.fixture
def profile(driver):
    return ProfilePage(driver)

@pytest.fixture
def password_restore(driver):
    return PasswordRestorePage(driver)

@pytest.fixture
def new_object(driver):
    return NewObjectPage(driver)

@pytest.fixture
def object_home_page(driver):
    return ObjectHomePage(driver)

@pytest.fixture
def object_page(driver):
    return ObjectPage(driver)

# @pytest.fixture
# def auth_data():
#     return {
#         'LOGIN': os.getenv("LOGIN"),
#         'PASSWORD': os.getenv("PASSWORD")
#     }
