# Bird bank Automation Project

## Dependencies
### requirement.txt
It's a dependency management file where we provide all our dependencies of the project. Here we install these as our dependencies,
```
selenium~=4.22.0
pytest~=8.2.2
xlrd~=2.0.1
pytest-html-reporter~=0.2.9
```
To install dependencies try below command, 
```commandline
pip intall -r requirements.txt
```

## Framework/Folder/Project Structure

```
bridbankautomation2
|- pages
    |-- basepage.py
    |-- homepage.py
    |-- ..
|- testdata
    |-- *.xlsx
    |-- read_data.py
|- reports
    |-- *.html
    |-- *.logs
|- tests
    |- *.py
|- conftest.py
|- pytest.ini
|- requirments.txt
|- README.md
```
* pages - POM (Page Object Model) - Design Pattern
  * BasePage clas, 
    * have all the selenium interactions like click(locator), enter_text(locator, text)
    * common methods in the pages
  * Page class like HomePage, LoginPage, AccountsPage, etc.,
    * Page objects -> By locators like By.ID, "signin_button"
    * Page actions -> def click_login_button():
    * Each page classes inherit BasePage
```python
class BasePage:

    def __init__(self, driver):
        self.__driver = driver

    def _click(self, locator):
        self.__driver.find_element(*locator).click()
        
class HomePage(BasePage):
  
    __LOGIN_BUTTON = By.ID, "signin_button"

    def click_login_button(self):
        self._click(self.__LOGIN_BUTTON)
```

* testdata
  * Excel file - have the testdata
  * read.data.py - reponsible to read the data from the Excel (xlrd). 
  It has to return the data in the format in list of list 
```python
import xlrd

def read_data():
    wb = xlrd.open_workbook("testdata/TestData.xls")
    sheet = wb.sheet_by_name("NewBiller")
    data = []
    for row in range(1, sheet.nrows):
        temp = []
        for col in range(sheet.ncols):
            temp.append(sheet.cell_value(row, col))
        data.append(temp)

    return data
```
* reports
  * *.html reports (pytest-html-reporter)
  * *.logs (pytest logs)
* tests
  * pytest test files
```python
import pytest
from pages.accountspage import AccountsPage
from pages.paybillspage import PayBillsPage
from testdata.read_data import read_data


class TestAddNewBiller:

    @pytest.fixture(autouse=True)
    def navigate_to_paybills_page(self, driver, do_login):
        accounts = AccountsPage(driver)
        accounts.click_pay_bills_link()

    @pytest.mark.parametrize("name,number", read_data())
    def test_add_new_biller_no_autopay(self, driver, name, number):
        paybills = PayBillsPage(driver)
        paybills.click_addnewbiller_button()
        paybills.do_add_new_biller(name, number, "no")
        assert "Payee Added Successful" == paybills.get_confirmation_text()

```
* conftest.py
  * In your tests, if you have some fixtures are needs to be used for multiple test files then you can keep those fixtures in conftest.py file. You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. The discovery of fixture functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins.
* pytest.ini
  * It's configuration file, which helps to create test suites and all our configuration options are provided here
```
[pytest]
python_files =
    test_*.py
addopts = 
-s
-v
log_file = reports/logs.log
log_file_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
log_file_date_format = %Y-%m-%d %H:%M:%S
```
* requirement.txt
  * discussed in the Dependencies section

## Important command line options
```commandline
pytest
```

## Key aspects
* conftest and pytest files should not have any selenium interaction
* all selenium interaction should be handled in the Page classes
* test data should not be hardcoded in the page classes