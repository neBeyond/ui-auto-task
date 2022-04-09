from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class CalculatorPage(BasePage):

    calculator_field = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div')
    memory_field = (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/span')
    result_field = (By.XPATH, '//*[@id="cwos"]')

    def __init__(self, driver):
        super().__init__(driver)

    def calculator_field_input(self, value):
        self.send_keys(self.calculator_field, value)

    def get_memory_field_value(self):
        return self.get_text(self.memory_field)

    def get_result_field_value(self):
        return self.get_text(self.result_field)