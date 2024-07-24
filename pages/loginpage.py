from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LoginPage(BasePage):
    __username_field = By.NAME, "username"
    __password_field = By.NAME, "password"
    __login_button = By.ID, "signin"

    def do_login(self, username, password):
        self._enter_text(self.__username_field, username)
        self._enter_text(self.__password_field, password)
        self._click(self.__login_button)