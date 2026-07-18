import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.authorization_page import AuthorizationPage
from pages.dashboard_page import DashboardPage
from pages.profile_page import ProfilePage


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = Options()
    # options.add_argument("--headless")
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