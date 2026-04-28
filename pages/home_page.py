from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class HomePage(BasePage):
    TRACKING_INPUT = (By.ID, "cargo_number")
    TRACKING_INPUT_FALLBACK = (By.XPATH, "//input[@name='query' and contains(@placeholder, 'Введіть номер посилки')]")

    # Додаємо "розумний" локатор для пошуку посилання "Відділення" в шапці
    BRANCHES_MENU_LINK = (By.XPATH, "//a[contains(text(), 'Відділення') or contains(text(), 'Мережа')]")

    def open(self):
        self.driver.get("https://novaposhta.ua/")

    def _get_tracking_input(self):
        # Prefer the old locator first, then fallback to the currently visible field.
        for locator in (self.TRACKING_INPUT, self.TRACKING_INPUT_FALLBACK):
            elements = self.driver.find_elements(*locator)
            for element in elements:
                if element.is_displayed():
                    return element

        return self.wait_for_element(self.TRACKING_INPUT_FALLBACK)

    def search_tracking_number(self, tracking_number):
        input_element = self._get_tracking_input()
        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.BACKSPACE)

        tracking_value = (tracking_number or "").strip()
        if not tracking_value:
            return

        input_element.send_keys(tracking_value)
        input_element.send_keys(Keys.ENTER)

    # Додаємо метод переходу
    def go_to_branches_page(self):
        self.click_element(self.BRANCHES_MENU_LINK)