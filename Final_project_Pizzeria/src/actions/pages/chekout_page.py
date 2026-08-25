import logging
import allure
from actions.pages.base_page import BasePage
from src.actions.locators.page_locators import CheckoutLocators


"""Функция проверки перехода на страницу авторизации для неавторизованного пользователя"""


class CheckoutPage(BasePage):

    @allure.step("Проверка наличия ссылки авторизации и ссылки ввода купона")
    def checking_link_authorized_and_coupon(self):
        self.attach_screenshot("checkout_page")
        link_authorization = self.wait_visible_element(CheckoutLocators.LINK_AUTHORIZATION).text
        link_coupon = self.wait_visible_element(CheckoutLocators.LINK_COUPON).text
        assert (link_authorization == "Авторизуйтесь"
                and link_coupon == "Нажмите для ввода купона")
        logging.info(f"There are links on the page '{link_authorization}' and '{link_coupon}'")
