from playwright.sync_api import Page
from allure import title, step
import logging


@title("Поиск тултипа графика и извлечение его содержимого")
def get_commit_activity_tooltip_data(wait_element, page: Page, date_label="Sunday,  3 Aug 2025"):

    logging.info("Выполнение манипуляций на странице для активации тултипа")
    with step(f"Поиск колонки '{date_label}' на графике"):
        wait_element(f"//*[contains(@aria-label,'{date_label}')]")
        column_locator = page.locator(f"//*[contains(@aria-label,'{date_label}')]")

    with step("Наводим указатель мыши на элемент для активации тултипа"):
        column_locator.wait_for(state='visible')
        column_locator.hover()

    with step(" Ждем,пока график применит hover-класс к этой колонке"):
        wait_element("//div[contains(@class,'highcharts-tooltip')]//table/tbody")

    with step("Извлекаем данные из тултипа"):
        tooltip_text = page.locator("//div[contains(@class,'highcharts-tooltip')]//table/tbody").inner_text()

    with step("Возвращаем для проверки полученные данные"):
        logging.info(f"Данные {tooltip_text} из тултипа возвращаем для проверки")
        return tooltip_text
