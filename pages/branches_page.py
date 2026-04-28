import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class BranchesPage(BasePage):
    CITY_INPUT = (By.CSS_SELECTOR, "input#city")
    BRANCH_INPUT = (By.CSS_SELECTOR, "input#branch")
    BRANCH_RESULTS = (By.CSS_SELECTOR, "li.office-item, div.branch-list-item")
    EMPTY_RESULT_MSG = (By.CSS_SELECTOR, "div.empty-results, div.error-message")

    def open(self):
        self.driver.get("https://novaposhta.ua/office")
        time.sleep(2)

    def select_city(self, city_name):
        city_field = self.wait_for_element(self.CITY_INPUT)
        city_field.send_keys(Keys.CONTROL + "a")
        city_field.send_keys(Keys.BACKSPACE)
        city_field.send_keys(city_name)
        time.sleep(1.5)
        city_field.send_keys(Keys.ENTER)
        time.sleep(1)

    def search_branch(self, branch_number):
        branch_field = self.wait_for_element(self.BRANCH_INPUT)
        branch_field.send_keys(Keys.CONTROL + "a")
        branch_field.send_keys(Keys.BACKSPACE)
        branch_field.send_keys(branch_number)
        branch_field.send_keys(Keys.ENTER)
        time.sleep(2)

    def get_branch_results_count(self):
        try:
            elements = self.driver.find_elements(*self.BRANCH_RESULTS)
            return len(elements)
        except:
            return 0

    def get_empty_result_text(self):
        element = self.wait_for_element(self.EMPTY_RESULT_MSG)
        return element.text.strip()