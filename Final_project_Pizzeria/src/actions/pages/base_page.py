from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import logging
import allure
from allure import step
import re
import time
from datetime import datetime, timedelta
from src.actions.waits.waits_elements import WaitsElements

"""Вспомогательные функции взаимодействия с элементами на страницах для выполнения тестовых сценариев"""

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver: WebDriver = driver
        self.timeout = timeout
        self.wait: WebDriverWait = WebDriverWait(driver, timeout)
        self.action = ActionChains(self.driver)
        self.waits_elements = WaitsElements(driver, timeout)

    def wait_url_to_be(self, expected_url: str):
        return self.waits_elements.wait_url_to_be(expected_url)

    def wait_visible_element(self, locator: Locator):
        return self.waits_elements.wait_visible_element(locator)

    def find_elements_page(self, locator: Locator):
        return self.waits_elements.find_elements_page(locator)

    def wait_clickable_element(self, locator: Locator):
        return self.waits_elements.wait_clickable_element(locator)

    def get_element_text_if_visible(self, locator) -> str | None:
        return self.waits_elements.get_element_text_if_visible(locator)

    @allure.step("Запуск функции наведение указателя на элемент")
    def go_to_element(self, locator: Locator):
        logging.info(f"Start hovering to element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.action.move_to_element(element).perform()
        logging.info(f"Finish hovering to {locator} element mode")

    @allure.step("Запуск функции нажатия на элемент")
    def click_element(self, locator: Locator):
        logging.info(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        with step("Клик по элементу"):
            element.click()
            logging.info("Clicked successfully")

    @allure.step("Функция извлечения искомого текста из URL")
    def extraction_url_contains(self, expected_text: str):
        logging.info(f"Function for extracting the target text from a URL: {expected_text}")
        self.wait.until(EC.url_contains(expected_text))
        current_url = self.driver.current_url
        return current_url

    @allure.step("Выбор опции '{option_text}' в выпадающем списке")
    def select_options(self, locator: Locator, option_text: str):
        logging.info(f"Select option '{option_text}' for locator: {locator}")
        options = self.wait.until(EC.presence_of_element_located(locator))
        from selenium.webdriver.support.select import Select
        select_element = Select(options)
        select_element.select_by_visible_text(option_text)
        self.driver.execute_script("document.activeElement.blur()")
        logging.info("Additional option selected")

    @allure.step("Создание скриншота текущего экрана браузера и прикрепления его к отчету Allure")
    def attach_screenshot(self, name: str):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )

    @allure.step("Добавление количество товаров на странице корзины")
    def click_change_quantity_up(self, locator: Locator):
        logging.info(f"Increasing quantity for input: {locator}")
        input_quantity = self.wait.until(EC.visibility_of_element_located(locator))
        input_quantity.click()
        from selenium.webdriver import Keys
        input_quantity.send_keys(Keys.ARROW_UP)

    @allure.step("Установка максимальной цены фильтра товаров")
    def price_filter_actions(self, path_price, target_price, slider_locator=None):
        with allure.step(
                         f"Установить правый ползунок фильтра по цене товара,"
                         f" в диапазон до {target_price} рублей, включительно"
        ):
            logging.info("Open the price setting function in the filter")

            price_element = self.wait_visible_element(path_price)

            current_price_text = price_element.text
            price_filter = int(re.sub(r'\D', '', current_price_text))

            while price_filter >= target_price:
                if slider_locator:
                    slider = self.wait_visible_element(slider_locator)
                    self.action.click_and_hold(slider).move_by_offset(xoffset=-50, yoffset=0).release().perform()

                current_price_text = self.wait_visible_element(path_price).text
                price_filter = int(re.sub(r'\D', '', current_price_text))

            logging.info(f"Price no more than {target_price} руб. installed")

    @allure.step("Запуск функции проверки и выхода из аккаунта")
    def logout(self, logout_button_locator: Locator):
        logging.info("Start checking authorization status and logout")
        auth_button = self.wait_visible_element(logout_button_locator)
        button_text = auth_button.text.strip()

        if button_text == "Выйти":
            with step("Пользователь авторизован. Выполняем выход из аккаунта"):
                self.go_to_element(logout_button_locator)
                self.click_element(logout_button_locator)
                logging.info("Successfully logged out")
        else:
            logging.info(
                f"User is not logged in (button text is '{button_text}')"
            )
        logging.info("Finish checking authorization status and logout")

    @allure.step("Запуск функции приведения текста к единому формату")
    def normalize_text(self, text: str) -> str:
        logging.info(f"Start normalizing text '{text}'")
        if not text:
            return ""

        for q in ['«', '»', '"', '"', '“', '”', '„', "'", '`', ' ']:
            text = text.replace(q, '')

        return ' '.join(text.lower().split())

    logging.info("Finish normalizing text")

    @allure.step("Запуск функции получения цены товара из текста")
    def extract_price(self, price: str) -> int:
        logging.info(f"Starting the function for obtaining the product price <{price}> from text")
        if not price:
            return 0

        clean = price.replace(" ", "").replace(",", ".")
        match = re.search(r"(\d+\.?\d*)", clean)
        if match:
            extracted = int(round(float(match.group(1))))
            logging.info(f"Finish the function for obtaining the product price {price} from text {clean}")
            return extracted
        return 0

    @allure.step("Запуск функции ввода значения в поле")
    def fill_element(self, input_field: Locator, initial_data: str):
        with step(f"Вводим значение {initial_data} в поле {input_field}"):
            logging.info(f"Run the function to enter {initial_data} a value into {input_field} a field")
            value_input = self.wait_visible_element(input_field)
            value_input.clear()
            value_input.send_keys(initial_data)
            logging.info("Completing the function of entering a value into a field")

    @allure.step("Запуск функции прокрутки к элементу по локатору")
    def scroll_to_element_by_locator(self, locator):
        logging.info("Launching the scroll function to an element by locator")
        element = self.wait_visible_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        time.sleep(0.5)
        logging.info("Completing the function of scroll to an element by locator")

    @allure.step("Прокрутка страницы в самое начало (наверх)")
    def scroll_to_top(self):
        logging.info("Scroll to the very top of the page")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.3)
        logging.info("Scrolling to top completed")

    @allure.step("Ввод в поле даты следующего дня")
    def input_tomorrow_date(self, locator: Locator):
        logging.info("Enter the date of the next day")
        tomorrow = datetime.now() + timedelta(days=1)
        date_str = tomorrow.strftime("%d.%m.%Y")
        self.fill_element(locator, date_str)
        logging.info(f"Input data: {date_str}")

    @allure.step("Функция блокировки запроса на сервер")
    def blocking_request_server(self, selenium, blocked_request):
        logging.info(f"Launch of the {blocked_request} request blocking feature")
        selenium.execute_cdp_cmd("Network.enable", {})
        selenium.execute_cdp_cmd("Network.setBlockedURLs", {
            "urls": [blocked_request]
        })

    @allure.step("Функция инициирует скрипт, для программного закрытия модального окна алерта")
    def suppress_alerts(self):
        logging.info("Run the function to suppress alerts in this page")
        self.driver.execute_script("window.alert = function() {};")
