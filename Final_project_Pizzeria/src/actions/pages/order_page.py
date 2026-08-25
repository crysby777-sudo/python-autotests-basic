import logging
import time
import allure
from allure import step
from selenium.webdriver.common.keys import Keys
from actions.locators.page_locators import OrderPageLocators, OrderConfirmationPageLocators
from src.actions.pages.base_page import BasePage
from config.configuration import Config
from datetime import datetime


"""Функции взаимодействия с элементами и проверки  на странице оформления заказа"""


class PlacingAnOrder(BasePage):

    @allure.step("Заполнение полей страницы оформления заказа")
    def filling_in_the_fields_on_the_order(self):
        with step("Заполняем поле ИМЯ"):
            self.fill_element(OrderPageLocators.FIRST_NAME, Config.FIRST_NAME)
        with step("Заполняем поле ФАМИЛИЯ"):
            self.fill_element(OrderPageLocators.FAMILY_NAME, Config.FAMILY_NAME)
        with step("Выбираем страну Belarus"):
            self.click_element(OrderPageLocators.COUNTRY)
            time.sleep(1)
            self.click_element(OrderPageLocators.COUNTRY_FIELD)
            self.fill_element(OrderPageLocators.COUNTRY_FIELD, Config.COUNTRY_BELARUS + Keys.ENTER)
        with step("Заполняем поле Адрес"):
            self.scroll_to_element_by_locator(OrderPageLocators.REGION)
            self.fill_element(OrderPageLocators.ADDRESS, Config.ADDRESS)
        with step("Заполняем поле Город"):
            self.fill_element(OrderPageLocators.CITY, Config.CITY)
        with step("Заполняем поле Область"):
            self.fill_element(OrderPageLocators.REGION, Config.REGION)
        with step("Заполняем поле Почтовый индекс"):
            self.fill_element(OrderPageLocators.INDEX_POST, Config.INDEX_POST)
        with step("Заполняем поле Телефон"):
            self.fill_element(OrderPageLocators.NUMBER_TEL, Config.NUMBER_TEL)
        with step("Заполняем поле EMAIL"):
            self.fill_element(OrderPageLocators.EMAIL_FIELD, Config.EMAIL_USER)
        with step("Делаем выбор способа доставки"):
            self.scroll_to_element_by_locator(OrderPageLocators.PAYMENT_UPON_DELIVERY)
            self.go_to_element(OrderPageLocators.PAYMENT_UPON_DELIVERY)
            self.click_element(OrderPageLocators.PAYMENT_UPON_DELIVERY)
        with step("Соглашаемся с условиями использования сайта (ставим чекбокс)"):
            self.go_to_element(OrderPageLocators.CHECKBOX_CONSENT)
            self.click_element(OrderPageLocators.CHECKBOX_CONSENT)
        with step("Выполняем ввод даты доставки (на следующий день)"):
            self.scroll_to_top()
            self.go_to_element(OrderPageLocators.INPUT_DATA)
            self.click_element(OrderPageLocators.INPUT_DATA)
            self.input_tomorrow_date(OrderPageLocators.INPUT_DATA)

    @allure.title("Фиксация информации о заказе")
    def recording_order_information(self):
        with step("Фиксируем общую сумму заказа и личные данные"):
            self.attach_screenshot(name="recording_order_information")
            total_order = self.wait_visible_element(OrderPageLocators.TOTAL_ORDER).text
            email = self.wait_visible_element(OrderPageLocators.EMAIL_FIELD)
            email_initiate = email.get_attribute("value")
            payment_method = self.wait_visible_element(OrderPageLocators.TITLE_PAYMENT).text
            order_date = datetime.now().strftime("%d.%m.%Y")

        return total_order, email_initiate, payment_method, order_date

    @allure.step("Нажатие кнопки Оформить заказ")
    def click_place_an_order(self):
        self.scroll_to_element_by_locator(OrderPageLocators.BUTTON_PLACE_ORDER)
        self.click_element(OrderPageLocators.BUTTON_PLACE_ORDER)
        time.sleep(1)

    @allure.step("Выполнение проверки подтверждение заказа, общую сумму и личные данные")
    def check_final_order(self, total, email, payment, order_date):
        self.attach_screenshot(name="final_order_page")
        exp_total = self.wait_visible_element(OrderConfirmationPageLocators.TOTAL).text
        exp_email = self.wait_visible_element(OrderConfirmationPageLocators.EMAIL).text
        exp_payment = self.wait_visible_element(OrderConfirmationPageLocators.PAYMENT_METHOD).text
        exp_order_date = datetime.now().strftime("%d.%m.%Y")

        assert self.wait_visible_element(OrderConfirmationPageLocators.POST_TITLE).text == 'ЗАКАЗ ПОЛУЧЕН'
        assert total == exp_total, f"Ожидалось {total}, получилось {exp_total}"
        assert email == exp_email, f"Ожидалось {email}, получилось {exp_email}"
        assert payment == exp_payment, f"Ожидалось {payment}, получилось {exp_payment}"
        assert order_date == exp_order_date, f"Ожидалось {order_date}, получилось {exp_order_date}"
        logging.info(f"TOTAL: {total}, EMAIL: {email}, PAYMENT: {payment}, DATE: {order_date}")

    @allure.step("Ввод и применение промокода")
    def using_the_promo_code(self, coupon_code):
        with step(f"Активация окна для ввода промокода {coupon_code} "):
            logging.info(f"Entering and using the promo code '{coupon_code}'")
            self.go_to_element(OrderPageLocators.LINK_PROMOCOD)
            self.click_element(OrderPageLocators.LINK_PROMOCOD)
        with step(f"Ввод промокода {coupon_code} "):
            self.go_to_element(OrderPageLocators.PROMOCOD_FIELD)
            self.click_element(OrderPageLocators.PROMOCOD_FIELD)
            self.fill_element(OrderPageLocators.PROMOCOD_FIELD, coupon_code)
        with step(f"Применение промокода {coupon_code}"):
            self.go_to_element(OrderPageLocators.APPLY_PROMOCOD)
            self.click_element(OrderPageLocators.APPLY_PROMOCOD)
            time.sleep(3)
            self.attach_screenshot(name="applying a promo code")

    @allure.step("Проверка уменьшения стоимости заказа на 10% после применения промокода GIVEMEHALYAVA")
    def check_order_reduction_by_10proc(self, total_old, total_new):
        self.scroll_to_element_by_locator(OrderPageLocators.TOTAL_COST)
        self.attach_screenshot(name="order_page")
        logging.info(f"Checking 10% discount: Original={total_old}, After discount={total_new}")
        total_old_clean = self.extract_price(total_old)
        total_new_clean = self.extract_price(total_new)
        total_apply_discount = total_old_clean - (total_old_clean / 10)
        assert total_new_clean == total_apply_discount, "Стоимость заказа не уменьшилась на 10%"
        logging.info(f"Test passed! Price reduced by 10%: {total_old_clean} → {total_apply_discount}")

    @allure.step("Проверка, что невалидный промокод не применяется и цена не меняется ")
    def check_order_wrong_promo_code(self, total_old, total_new):
        self.attach_screenshot(name="error_promo_code")
        self.scroll_to_element_by_locator(OrderPageLocators.TOTAL_COST)
        self.attach_screenshot(name="order_page_total_cost")
        logging.info("Verification: Invalid promo code not applied, error message displayed")
        total_old_clean = self.extract_price(total_old)
        total_new_clean = self.extract_price(total_new)
        error = self.driver.find_elements(*OrderPageLocators.ERROR_COUPON)
        error_message = error[0].text.strip() if error else ""
        assert total_new_clean == total_old_clean
        assert total_new_clean == total_old_clean, \
            f"Цена изменилась! Старая: {total_old_clean}, Новая: {total_new_clean}"
        assert error_message, "Сообщение об ошибке не отображается!"
        assert 'Неверный купон.' in error_message, \
            f"Ожидался текст 'Неверный купон.'. Получено: {error_message}"""
        logging.info(f"The test was successful, the price did not change, an error message appeared {error_message}.")

    @allure.step("Проверка изменения стоимости заказа при применении промокода"
                 " при блокировке отправки запроса на сервер")
    def check_order_reduction_blocking_request(self, total_old, total_new):
        self.attach_screenshot(name="order_page_blocking_request")
        logging.info(f"Checking 10% discount: Original={total_old}, After discount={total_new}")
        total_old_clean = self.extract_price(total_old)
        total_new_clean = self.extract_price(total_new)
        total_apply_discount = total_old_clean - (total_old_clean / 10)
        assert total_new_clean == total_old_clean, f"Стоимость заказа уменьшилась на 10% {total_apply_discount}"
        logging.info(f"Test passed! The order total did not decrease by 10%: {total_old_clean} = {total_new_clean}")

    @allure.step("Функция блокировки запроса на сервер при применении промокода")
    def blocking_request_server_coupon(self, selenium, blocked_request):
        self.blocking_request_server(selenium, blocked_request)

    @allure.step("Функция проверки повторного применения промокода GIVEMEHALYAVA для следующего заказа")
    def check_re_use_promo_code_next_order(self, total_cost, total_sum):
        with step(" Выполнение сравнения общей стоимости и суммы заказа после применения промокода"):
            self.scroll_to_element_by_locator(OrderPageLocators.TOTAL_COST)
            self.attach_screenshot(name="order_page_Re-applying a promo code")
            logging.info("Function to check for the reuse of the GIVEMEHALYAVA promo code on the next order.")
            cost_clean = self.extract_price(total_cost)
            sum_clean = self.extract_price(total_sum)
            assert cost_clean == sum_clean, \
                f"Цена изменилась! Старая: {cost_clean}, Новая: {sum_clean}"

    @allure.title("Фиксация общей стоимости заказа и суммы заказа")
    def recording_order_cost(self):
        self.scroll_to_element_by_locator(OrderPageLocators.TOTAL_COST)
        self.attach_screenshot(name="order_page_recording_cost")
        with step("Фиксируем общую стоимость заказа"):
            cost_order = self.wait_visible_element(OrderPageLocators.TOTAL_COST).text
        with step("Фиксируем сумму заказа"):
            sum_order = self.wait_visible_element(OrderPageLocators.TOTAL_ORDER).text
        logging.info(f"Total cost: {cost_order}, Sum order: {sum_order}")
        return cost_order, sum_order
