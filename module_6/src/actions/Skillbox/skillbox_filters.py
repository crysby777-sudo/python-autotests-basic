from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import title, step
import logging


@title("Поиск элементов и применение фильтров на странице")
def apply_skillbox_filters_and_get_results(selenium):
    logging.info("Поиск элементов и применение фильтров на странице")

    with step("Поиск и нажатие кнопки «Профессия»"):
        selenium.find_element(By.XPATH, "//button/span[contains(., 'Профессия')]").click()

    with step("Поиск и нажатие кнопки 'Длительность'"):
        selenium.find_element(By.XPATH, "//button//span[contains(., 'Длительность')]").click()

    with step("Поиск и выбор в меню 'Длительность' значения 'От 6 до 12 мес.'"):
        selenium.find_element(By.XPATH, "//ul/li[contains(text(), 'От 6 до 12 мес.')]").click()

    with step("Поиск и нажатие кнопки 'Тематика'"):
        selenium.find_element(By.XPATH, "(//button[@aria-label= 'Открыть список'])[3]").click()

    with step("Поиск и выбор в меню 'Тематика' значения 'Тестирование'"):
        selenium.find_element(By.XPATH, "//li[contains(text(), 'Тестирование')]").click()

    with step("Поиск и нажатие кнопки 'Применить' в меню 'Тематика'"):
        selenium.find_element(By.XPATH, "//button[contains(text(), 'Применить')]").click()

    with step("Ожидание и поиск отфильтрованных профессий"):
        wait = WebDriverWait(selenium, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'programs-filtered')]")))

    with step("Поиск в отфильтрованных элементах значения 'Профессия'"):
        profession_filter = selenium.find_elements(By.XPATH, "//span[contains(@class, 'product')]"
                                                   "[normalize-space() = 'Профессия']")

    with step("Поиск в отфильтрованных элементах значения 'Продолжительность'"):
        duration_filter = selenium.find_elements(By.XPATH, "//li[contains(@class , 'product-card')"
                                                 " and contains(., 'месяцев')]")

    with step("Возвращаем значения для проверки"):
        logging.info("Возвращаем значения для проверки")
        return profession_filter, duration_filter
