import pytest
import time
from pages.home_page import HomePage
from pages.tracking_page import TrackingPage


class TestTracking:

    def test_valid_tracking_number(self, driver):
        home_page = HomePage(driver)
        tracking_page = TrackingPage(driver)

        home_page.open()

        valid_number = "20450000000000"  # Бажано замінити на свій валідний номер
        home_page.search_tracking_number(valid_number)

        status_text = tracking_page.get_parcel_status()
        assert status_text != "", "Статус посилки не повинен бути порожнім!"

    def test_invalid_tracking_number(self, driver):
        home_page = HomePage(driver)
        tracking_page = TrackingPage(driver)

        home_page.open()

        invalid_number = "00000000000000"
        home_page.search_tracking_number(invalid_number)

        error_text = tracking_page.get_error_text()
        expected_error_fragment = "не знайдено"
        assert expected_error_fragment.lower() in error_text.lower(), \
            f"Очікували помилку з текстом '{expected_error_fragment}', але отримали: '{error_text}'"

    def test_empty_tracking_field(self, driver):
        home_page = HomePage(driver)
        home_page.open()

        initial_url = driver.current_url
        home_page.search_tracking_number("")

        time.sleep(1)

        current_url = driver.current_url
        assert current_url == initial_url, "Система не повинна виконувати перехід при порожньому полі пошуку!"