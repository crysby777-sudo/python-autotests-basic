from allure import title, step
import logging
from playwright.sync_api import Page


@title("Поиск элементов и применение фильтров на странице")
def apply_skillbox_filters_and_get_results(wait_element, page: Page):
    logging.info("Поиск элементов и применение фильтров на странице")

    with step("Поиск и нажатие кнопки «Профессия»"):
        page.locator("//button/span[contains(., 'Профессия')]").click()

    with step("Поиск и нажатие кнопки 'Длительность'"):
        page.locator("//button//span[contains(., 'Длительность')]").click()

    with step("Поиск и выбор в меню 'Длительность' значения 'От 6 до 12 мес.'"):
        page.locator("//ul/li[contains(text(), 'От 6 до 12 мес.')]").click()

    with step("Поиск и нажатие кнопки 'Тематика'"):
        page.locator("(//button[@aria-label='Открыть список'])[3]").click()

    with step("Поиск и выбор в меню 'Тематика' значения 'Тестирование'"):
        page.locator("//li[contains(text(), 'Тестирование')]").click()

    with step("Поиск и нажатие кнопки 'Применить' в меню 'Тематика'"):
        page.locator("//button[contains(text(), 'Применить')]").click()
    page.wait_for_timeout(500)
    with step("Ожидание и поиск отфильтрованных профессий"):
        wait_element("//span[contains(@class, 'programs-filtered')]")

    with step("Поиск в отфильтрованных элементах значения 'Профессия'"):
        profession_filter = page.locator("//span[contains(@class, 'product')][normalize-space() = 'Профессия']").all()

    with step("Поиск в отфильтрованных элементах значения 'Продолжительность'"):
        duration_filter = page.locator("//li[contains(@class , 'product-card') and contains(., 'месяцев')]").all()
        logging.info(f"Найдено: профессий={len(profession_filter)}, длительностей={len(duration_filter)}")

    with step("Возвращаем значения для проверки"):
        logging.info("Возвращаем значения для проверки")
        return profession_filter, duration_filter
