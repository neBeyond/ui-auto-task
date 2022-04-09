import pytest
from Pages.home_page import HomePage
from Pages.calculator_page import CalculatorPage
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures('init_driver')
class TestCalculator:

    def test_calculate(self):
        home_page = HomePage(self.driver)
        calculator_page = CalculatorPage(self.driver)
        """открыть google.com"""
        self.driver.get('http://google.com')
        """ввести в строку поиска Калькулятор"""
        home_page.search_field_input('Калькулятор')
        """нажать на кнопку поиска"""
        home_page.click_search_button()
        """на страничке калькулятора сделать подсчет"""
        calculator_page.calculator_field_input('1 * 2 - 3 + 1')
        calculator_page.calculator_field_input(Keys.RETURN)
        """проверить значение в строке памяти"""
        assert calculator_page.get_memory_field_value() == '1 × 2 - 3 + 1 ='
        """проверить значение результата"""
        assert calculator_page.get_result_field_value() == '0'
