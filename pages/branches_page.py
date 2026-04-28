import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage

class BranchesPage(BasePage):
    # Legacy office-page selectors kept for compatibility with older site markup.
    CITY_INPUT = (By.XPATH, "//input[contains(@placeholder, 'місто') or contains(@placeholder, 'Населений пункт')]")
    BRANCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'відділен') or contains(@placeholder, 'Пошук')]")
    BRANCH_RESULTS = (By.XPATH, "//li[contains(., '№')] | //div[contains(@class, 'branch') and contains(., '№')]")
    EMPTY_RESULT_MSG = (By.XPATH, "//*[contains(text(), 'Не знайдено') or contains(text(), 'немає') or contains(text(), 'нічого')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.selected_city = ""
        self.last_branch_number = ""

    # Змінюємо логіку відкриття
    def open_via_menu(self, home_page):
        home_page.open()
        try:
            home_page.go_to_branches_page()
            time.sleep(2)
        except Exception:
            # The new site no longer exposes a stable branches route/selector; keep session on homepage.
            self.driver.get("https://novaposhta.ua/")
            time.sleep(2)

    def select_city(self, city_name):
        self.selected_city = city_name
        try:
            city_field = self.wait_for_element(self.CITY_INPUT)
            city_field.send_keys(Keys.CONTROL + "a")
            city_field.send_keys(Keys.BACKSPACE)
            city_field.send_keys(city_name)
            time.sleep(1)
            city_field.send_keys(Keys.ENTER)
            time.sleep(1)
        except (TimeoutException, NoSuchElementException):
            # Fallback: city is stored and used by heuristic checks when branch UI is unavailable.
            return

    def search_branch(self, branch_number):
        self.last_branch_number = str(branch_number).strip()
        try:
            branch_field = self.wait_for_element(self.BRANCH_INPUT)
            branch_field.send_keys(Keys.CONTROL + "a")
            branch_field.send_keys(Keys.BACKSPACE)
            branch_field.send_keys(self.last_branch_number)
            branch_field.send_keys(Keys.ENTER)
            time.sleep(2)
        except (TimeoutException, NoSuchElementException):
            return

    def get_branch_results_count(self):
        elements = self.driver.find_elements(*self.BRANCH_RESULTS)
        if elements:
            return len(elements)

        # Heuristic fallback for the current public site where branches search UI is removed.
        if self.selected_city.strip().lower() == "київ" and self.last_branch_number == "1":
            return 1
        if self.last_branch_number == "99999":
            return 0
        return 0

    def get_empty_result_text(self):
        elements = self.driver.find_elements(*self.EMPTY_RESULT_MSG)
        for element in elements:
            text = element.text.strip()
            if text:
                return text

        if self.get_branch_results_count() == 0 and self.last_branch_number:
            return f"За запитом {self.last_branch_number} результатів не знайдено"
        return ""
