import re
from allure import feature, step, title, suite
from src.actions.Search_Git.search_repo_stars import search_repos_and_get_star_elements
import logging
from playwright.sync_api import Page


@suite("Поиск и фильтрация по количеству звезд репозиториев")
@feature("Поиск и фильтрация по репозиториям")
class TestRepoStars:
    @title("Поиск и фильтрация репозиториев по количеству звезд")
    def test_repo_stars(self, go_to_url, page: Page, wait_element):
        logging.info("Запуск теста test_stars_git.py")
        with step("Выполняем переход на страницу https://github.com/search/advanced"):
            go_to_url('https://github.com/search/advanced')
        language = 'Python'
        stars_filter = '>20000'
        filename = 'environment.yml'

        with step("Вызываем функцию для заполнения формы поиска"):
            star_elem = search_repos_and_get_star_elements(wait_element, page, language, stars_filter, filename)
        logging.info(f"Выполняем проверку списка репозиториев с количеством звёзд '{stars_filter}'")
        with step(f"Выполняем проверку списка репозиториев с количеством звёзд '{stars_filter}'"):
            elem = 0
            for element in star_elem:

                aria = element.get_attribute('aria-label')
                digits = re.findall(r'\d+', aria, re.IGNORECASE)
                stars = int(digits[0])
                assert stars > 20000
                elem += 1
        logging.info(f"Количество записей в списке репозиториев с количеством звёзд >20000: '{elem}'")
        logging.info("Завершение теста test_stars_git.py")
