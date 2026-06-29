from allure import step, title
import logging
from playwright.sync_api import Page


@title("Выполняем поиск нужных элементов на странице и вносим искомые данные")
def search_issues_and_get_matches(wait_element, page: Page,
                                  search_location,
                                  keyword):
    logging.info("Выполнение сценария на странице: поиск элементов и ввод данных")

    with step("Активируем строку поиска кликом"):
        search_bar = page.locator('//input[@id="repository-input"]')
        search_bar.click()

    with step("Очищаем строку поиска"):
        search_bar.clear()

    with step(f"Вводим в строку поиска '{keyword}'"):
        search_bar.fill(f'{search_location} {keyword}')
        page.locator('button[class*="SubmitButton-module__IconButton"]').click()

    with step(f"Ищем элементы с ключевым словом '{keyword}'"):
        wait_element('//a[@data-testid="issue-pr-title-link"]')
        key_word = page.locator('//a[@data-testid="issue-pr-title-link"]').filter(has_text=keyword).all()

        logging.info(f"Найдено: названия заголовков с ключевым словом '{keyword}'={len(key_word)}")

    with step("Отправляем найденные названия задач для проверки"):
        logging.info("Передача элементов для выполнения проверки")
        return key_word
