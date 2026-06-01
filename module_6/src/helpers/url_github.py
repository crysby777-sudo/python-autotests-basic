import allure
import pytest
import logging


class GitHubSearch:
    @pytest.fixture()
    def go_to_github_issues(self, selenium):
        logging.info("Переход на страницу https://github.com/microsoft/vscode/issues")

        with allure.step("Выполняем переход на страницу https://github.com/microsoft/vscode/issues"):
            selenium.get("https://github.com/microsoft/vscode/issues")
