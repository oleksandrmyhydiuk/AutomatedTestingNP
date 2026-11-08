import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    BASE_URL = "https://novaposhta.ua/"
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def open_url(self, url=None):
        self.driver.get(url or self.BASE_URL)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def clear_and_type(self, element, text=""):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        if text:
            element.send_keys(text)

    def click_element(self, locator, retries=3):
        for i in range(retries):
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(0.5)
                fresh_element = self.driver.find_element(*locator)
                fresh_element.click()
                return
            except StaleElementReferenceException:
                if i == retries - 1:
                    raise
                time.sleep(1)
            except Exception:
                fresh_element = self.wait_for_element(locator)
                self.driver.execute_script("arguments[0].click();", fresh_element)
                return
