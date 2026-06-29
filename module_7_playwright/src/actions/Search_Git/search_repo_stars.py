from playwright.sync_api import Page
from allure import step, title
import logging


@title("Выполняем поиск нужных полей и заполняем форму расширенного поиска")
def search_repos_and_get_star_elements(wait_element, page: Page, language, stars, filename):
    logging.info("Переходим к заполнению формы расширенного поиска")

    with step(f" В поле 'Written in this language' выбираем '{language}' "):
        page.locator("select").first.select_option(value="Python")

    with step(f" В поле 'With this many stars' вводим  '{stars}' "):
        page.locator("//*[@id='search_stars']").fill(stars)

    with step(f" В поле 'With this file name' вводим  '{filename}' "):
        page.locator("//*[@id='search_filename']").fill(filename)

    with step(" Нажинаем кнопку поиска"):
        page.locator("//button[contains(text(), 'Search')]").nth(1).click()

    with step("Ждем появления результатов"):
        wait_element("//a[contains(@aria-label, 'stars')]")
        star_locator = page.locator("//a[contains(@aria-label, 'stars')]").all()

    with step("Возвращаем элементы с количеством звезд"):
        logging.info("Передача данных для выполнения проверки")
        return star_locator
