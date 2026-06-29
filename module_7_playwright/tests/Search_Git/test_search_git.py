import re
from playwright.sync_api import Page
from src.actions.Search_Git.search_issues import search_issues_and_get_matches
from src.actions.Search_Git.issues_authors import get_issue_authors_by_name
from allure import suite, feature, step, title
import logging


@suite("Поиск и фильтрация на сайте GitHub")
@feature("Поиск репозиториев по ключевому слову")
class TestSearch:
    @title("Проверка поиска по ключевому слову в заголовках задач")
    def test_search_field(self, go_to_url, page: Page, wait_element):
        with step("Выполняем переход на сайт https://github.com/microsoft/vscode/issues"):
            go_to_url('https://github.com/microsoft/vscode/issues')

        with step("Вызываем функцию для взаимодействия с элементами на странице"):
            search_location = 'in:title'
            keyword = 'copilot'
            key_word = search_issues_and_get_matches(wait_element, page, search_location, keyword)

        with step("Проверяем полученный результат"):
            assert len(key_word) > 0, f"Поиск не вернул ни одного элемента для ключевого слова '{keyword}'"

            for issue in key_word:
                title_text = issue.text_content().strip()
                pattern = rf'(?<![a-zA-Z]){re.escape(keyword)}s?\b'
                assert re.search(pattern, title_text,
                                 re.IGNORECASE), f"Слово '{keyword}' не найдено в заголовке: '{title_text}'"

    @feature("Поиск репозиториев по автору")
    @title("Применение фильтра «Автор» к списку задач")
    def test_button_Author(self, go_to_url, page, wait_element):
        with step("Выполняем переход на сайт https://github.com/microsoft/vscode/issues"):
            go_to_url('https://github.com/microsoft/vscode/issues')
        author_name = 'bpasero'

        with step("Вызываем функцию для взаимодействия с элементами на странице"):
            issue_author = get_issue_authors_by_name(wait_element, page, author_name)
        logging.info("Выполняем проверку")
        with step("Проверяем полученный результат"):
            for nickname in issue_author:
                author = nickname.text_content()
                assert author_name in author
        logging.info("Завершение теста test_search_git.py")
