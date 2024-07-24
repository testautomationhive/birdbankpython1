import logging

import pytest

from pages.basepage import BasePage
from pages.paybillspage import PayBillsPage
from testdata.read_data import read_data

LOGGER = logging.getLogger(__name__)


class TestPayBills:

    @pytest.fixture(scope="class")
    def navigate_to_pay_bills_page(self, driver, do_login):
        basepage = BasePage(driver)
        basepage.navigate_to_tab("PAY BILLS")
        LOGGER.info("Navigated to Pay Bills page")

    @pytest.fixture
    def navigate_to_add_new_biller_page(self, driver, navigate_to_pay_bills_page):
        self.pay_bills_page = PayBillsPage(driver)
        self.pay_bills_page.click_add_new_biller()
        LOGGER.info("Navigated to Add New Billers page")

    @pytest.mark.parametrize("name,reg_num", read_data())
    def test_add_new_payee(self, driver, navigate_to_add_new_biller_page, name, reg_num):
        self.pay_bills_page.do_add_new_payee(name, reg_num)
        assert "Payee Added Successful" == self.pay_bills_page.get_confirmation_msg()
        LOGGER.info("Added the new payee")
