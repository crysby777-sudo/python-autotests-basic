import re
from src.actions.Search_Git.search_issues import search_issues_and_get_matches
from src.actions.Search_Git.issues_authors import get_issue_authors_by_name
from src.helpers.url_github import GitHubSearch
from allure import suite, feature, step, title
import logging


@suite("Поиск и фильтрация на сайте GitHub")
@feature("Поиск репозиториев по ключевому слову")
class TestSearch(GitHubSearch):

    @title("Проверка поиска по ключевому слову в заголовках задач")
    def test_search_field(self, selenium, go_to_github_issues):

        keyword = 'copilot'
        search_query = f"in:title {keyword}"

        with step("Вызываем функцию для взаимодействия с элементами на странице"):
            key_word = search_issues_and_get_matches(selenium, keyword, search_query)

        with step("Проверяем полученный результат"):
            for issue in key_word:
                title = issue.get_attribute("textContent").strip()
                pattern = rf'(?<![a-zA-Z]){re.escape(keyword)}s?\b'
                assert re.search(pattern, title, re.IGNORECASE)

    @feature("Поиск репозиториев по автору")
    @title("Применение фильтра «Автор» к списку задач")
    def test_button_Author(self, selenium, go_to_github_issues):
        with step("Выполняем переход на страницу https://github.com/microsoft/vscode/issues"):
            selenium.get('https://github.com/microsoft/vscode/issues')
        author_name = 'bpasero'

        with step("Вызываем функцию для взаимодействия с элементами на странице"):
            issue_author = get_issue_authors_by_name(selenium, author_name)
        logging.info("Выполняем проверку")
        with step("Проверяем полученный результат"):
            for nickname in issue_author:
                author = nickname.text
                assert author_name in author
        logging.info("Завершение теста test_search_git.py")
