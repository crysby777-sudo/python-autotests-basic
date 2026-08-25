import logging
from typing import Tuple
import allure
from allure import step
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

Locator = Tuple[str, str]

"""Вспомогательные функции ожидания и кликабельности элементов для выполнения тестовых сценариев"""


class WaitsElements:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Запуск функции ожидания и текущего URL")
    def wait_url_to_be(self, expected_url: str):
        logging.info(f"We expect the URL to be: {expected_url}")
        url_page = self.wait.until(EC.url_to_be(expected_url))
        logging.info("Completing the URL check function")
        return url_page

    @allure.step("Запуск функции обнаружения элемента в DOM дереве")
    def wait_visible_element(self, locator: Locator):
        logging.info(f"Start wait_visible_element for: {locator}")
        with step("Ожидание того, что искомый элемент находится в DOM дереве страницы и виден"):
            visible_element = self.wait.until(EC.visibility_of_element_located(locator))
            logging.info(f"Finish wait_visible_element {locator} mode")
            return visible_element

    @allure.step("Запуск функции поиска элемента в DOM дереве")
    def find_element_page(self, locator: Locator):
        logging.info(f"Start find_element_page for: {locator}")
        element = self.driver.find_element(locator)
        logging.info(f"Finish, found {len(element)} element")
        return element

    @allure.step("Запуск функции поиска нескольких элементов в DOM дереве")
    def find_elements_page(self, locator: Locator):
        logging.info(f"Start find_elements_page for: {locator}")
        elements = self.driver.find_elements(*locator)
        logging.info(f"Finish, found {len(elements)} elements")
        return elements

    @allure.step("Запуск функции ожидание пока видимый элемент станет кликабельным")
    def wait_clickable_element(self, locator: Locator):
        logging.info(f"Wait for clickability of a visible element {locator}")
        visible_element = self.wait.until(
            lambda driver: next((el for el in driver.find_elements(locator)
                                 if el.is_displayed()), None))
        if visible_element.tag_name == "select":
            element = self.wait.until(EC.presence_of_element_located(locator))
        else:
            element = self.wait.until(EC.element_to_be_clickable(visible_element))
        return element

    logging.info("Function completion: wait until element becomes clickable.")

    @allure.step(" Запуск функции безопасного ожидания появления элемента")
    def get_element_text_if_visible(self, locator) -> str | None:
        logging.info(f"Starting a safe wait for an element to appear {locator}")
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            logging.info("Finished a safe wait for an element")
            return element.text.strip()

        except (TimeoutException, NoSuchElementException):
            logging.info("Element not found on page")
            return None
