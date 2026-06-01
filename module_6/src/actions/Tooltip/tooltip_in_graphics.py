from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from allure import title, step
import logging


@title("Поиск тултипа графика и извлечение его содержимого")
def get_commit_activity_tooltip_data(selenium, date_label="Sunday,  3 Aug 2025"):
    logging.info("Выполнение манипуляций на странице для активации тултипа")
    with step("Установка явного ожидания загрузки DOM (15 секунд)"):
        wait = WebDriverWait(selenium, 15)

    with step(f"Поиск колонки'{date_label}' на графике"):
        column_locator = (By.XPATH, f"//*[contains(@aria-label,'{date_label}')]")
    with step(" Установка явного ожидания (15 секунд) появления колонки"):
        column = wait.until(EC.presence_of_element_located(column_locator))

    with step(" Наводим указатель мыши на элемент для активации тултипа'"):
        ActionChains(selenium).move_to_element(column).perform()

    with step(" Ждем,пока график применит hover-класс к этой колонке"):
        wait.until(lambda d: 'highcharts-point-hover' in column.get_attribute("class"))

    with step("Извлекаем данные из тултипа"):
        column_data = column.get_attribute("aria-label")
        tooltip_text = selenium.find_element(By.XPATH, "//div[contains(@class,'highcharts-tooltip')]//table/tbody").text

    with step("Возвращаем для проверки полученные данные"):
        logging.info(f"Данные {tooltip_text} из тултипа возвращаем для проверки")
        return column_data, tooltip_text
