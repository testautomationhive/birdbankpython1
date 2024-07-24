import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.homepage import HomePage
from pages.loginpage import LoginPage

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def driver():
    LOGGER.info("Start initializing the driver")
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument("start-maximized")
    driver_ = webdriver.Chrome(options)
    LOGGER.info("Driver session is started")
    driver_.get("https://birdbank.pythonanywhere.com/")

    yield driver_
    # driver_.quit()
    LOGGER.info("Driver session is ended")


@pytest.fixture(scope="class")
def do_login(driver):
    LOGGER.info("Do login with testuser1")
    homepage = HomePage(driver)
    homepage.click_login_button()
    login = LoginPage(driver)
    login.do_login("testuser1", "testpassword")
    LOGGER.info("Login completed")
