from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def _click(self, locator):
        self.__driver.find_element(*locator).click()

    def _enter_text(self, locator, text):
        self.__driver.find_element(*locator).send_keys(text)

    def _get_text(self, locator):
        return self.__driver.find_element(*locator).text

    def _wait_for(self, locator, condition="visibility", timeout=30):
        wait = WebDriverWait(self.__driver, timeout)
        if condition == "visibility":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "clickable":
            return wait.until(EC.element_to_be_clickable(locator))
        elif condition == "invisibility":
            return wait.until(EC.invisibility_of_element_located(locator))

    def navigate_to_tab(self, text):
        self.__driver.find_element(By.LINK_TEXT, text).click()
