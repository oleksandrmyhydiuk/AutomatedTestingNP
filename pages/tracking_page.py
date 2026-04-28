from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TrackingPage(BasePage):
    STATUS_HEADING = (By.CSS_SELECTOR, "div.header__status-text")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-msg, div.tracking-error")

    def get_parcel_status(self):
        element = self.wait_for_element(self.STATUS_HEADING)
        return element.text.strip()

    def get_error_text(self):
        element = self.wait_for_element(self.ERROR_MESSAGE)
        return element.text.strip()