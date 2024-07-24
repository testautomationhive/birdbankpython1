from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class HomePage(BasePage):
    __login_button = By.ID, "signin_button"

    def click_login_button(self):
        self._click(self.__login_button)