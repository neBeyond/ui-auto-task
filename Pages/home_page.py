from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    search_field = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_button = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')

    def __init__(self, driver):
        super().__init__(driver)

    def search_field_input(self, value):
        self.send_keys(self.search_field, value)

    def click_search_button(self):
        self.click(self.search_button)