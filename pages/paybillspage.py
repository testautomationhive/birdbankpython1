from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class PayBillsPage(BasePage):
    __add_new_biller_button = By.ID, "add_payee"
    __biller_name_field = By.XPATH, "//input[contains(@placeholder,'Name')]"
    __registration_field = By.XPATH, "//input[contains(@placeholder,'Number')]"
    __no_radio_button = By.XPATH, "//label[text()='No']"
    __save_button = By.ID, "save"
    __confirmation_msg_text = By.ID, "confirmationMessage"

    def click_add_new_biller(self):
        self._click(self.__add_new_biller_button)

    def do_add_new_payee(self, name, number):
        # self._enter_text(self.__biller_name_field, name)
        element = self._wait_for(self.__biller_name_field)
        element.send_keys(name)
        self._enter_text(self.__registration_field, number)
        self._click(self.__no_radio_button)
        self._click(self.__save_button)

    def get_confirmation_msg(self):
        return self._get_text(self.__confirmation_msg_text)