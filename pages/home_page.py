from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class HomePage(BasePage):
    TRACKING_INPUT = (By.ID, "cargo_number")

    def open(self):
        self.driver.get("https://novaposhta.ua/")

    def search_tracking_number(self, tracking_number):
        input_element = self.wait_for_element(self.TRACKING_INPUT)
        input_element.clear()
        input_element.send_keys(tracking_number)
        input_element.send_keys(Keys.ENTER)