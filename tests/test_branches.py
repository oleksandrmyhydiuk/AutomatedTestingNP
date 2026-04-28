import pytest
from pages.branches_page import BranchesPage


class TestBranches:

    def test_existing_branch_search(self, driver):
        branches_page = BranchesPage(driver)
        branches_page.open()

        branches_page.select_city("Київ")
        branches_page.search_branch("1")

        results_count = branches_page.get_branch_results_count()
        assert results_count > 0, "БАГ! Очікували знайти відділення №1 у місті Київ, але список порожній."

    def test_nonexistent_branch_search(self, driver):
        branches_page = BranchesPage(driver)
        branches_page.open()

        branches_page.select_city("Київ")

        invalid_branch_number = "99999"
        branches_page.search_branch(invalid_branch_number)

        results_count = branches_page.get_branch_results_count()
        assert results_count == 0, f"БАГ! Система знайшла {results_count} результатів для відділення {invalid_branch_number}."

        empty_message = branches_page.get_empty_result_text()
        assert empty_message != "", "Повідомлення про відсутність результатів не відобразилося!"