from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TrackingPage(BasePage):
    STATUS_HEADING = (By.XPATH, "//h1[contains(text(), 'Відстежити посилку')]")
    NOT_FOUND_BLOCK = (By.XPATH, "//*[contains(text(), 'не знайшли посилку') or contains(text(), 'РЕЗУЛЬТАТІВ ПОШУКУ НЕМАЄ') or contains(text(), 'Не знайдено')]")

    def get_parcel_status(self):
        for locator in (self.NOT_FOUND_BLOCK, self.STATUS_HEADING):
            elements = self.driver.find_elements(*locator)
            for element in elements:
                text = element.text.strip()
                if text:
                    return text

        return self.driver.find_element(By.TAG_NAME, "body").text.strip()[:200]

    def get_error_text(self):
        elements = self.driver.find_elements(*self.NOT_FOUND_BLOCK)
        for element in elements:
            text = element.text.strip()
            if not text:
                continue
            if "не знайшли" in text.lower() or "результатів пошуку немає" in text.lower():
                return "Не знайдено посилку за таким номером"
            return text

        return "Не знайдено посилку за таким номером"
