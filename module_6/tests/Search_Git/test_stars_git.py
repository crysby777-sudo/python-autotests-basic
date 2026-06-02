import re
from allure import feature, step, title, suite
from src.actions.Search_Git.search_repo_stars import search_repos_and_get_star_elements
import logging


@suite("Поиск и фильтрация по количеству звезд репозиториев")
@feature("Поиск и фильтрация по репозиториям")
class TestRepoStars:
    @title("Поиск и фильтрация репозиториев по количеству звезд")
    def test_repo_stars(self, selenium):
        logging.info("Запуск теста test_stars_git.py")
        with step("Выполняем переход на страницу https://github.com/search/advanced"):
            selenium.get('https://github.com/search/advanced')
        language = 'Python'
        stars_filter = '>20000'
        filename = 'environment.yml'

        with step("Вызываем функцию для заполнения формы поиска"):
            star_elem = search_repos_and_get_star_elements(selenium, language, stars_filter, filename)
        logging.info(f"Выполняем проверку по количеству звёзд '{stars_filter}'")
        with step(f"Выполняем проверку по количеству звёзд '{stars_filter}'"):
            for element in star_elem:
                aria = element.get_attribute('aria-label')
                digits = re.findall(r'\d+', aria, re.IGNORECASE)
                stars = int(digits[0])
                assert stars > 20000
        logging.info("Завершение теста test_stars_git.py")
