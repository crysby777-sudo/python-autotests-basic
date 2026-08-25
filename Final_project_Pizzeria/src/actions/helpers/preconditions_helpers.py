import allure
import logging
import time
from actions.pages.base_page import BasePage
from src.actions.locators.page_locators import AuthorizedPageLocators, HomePageLocators
from config.configuration import Config
from src.actions.pages.home_page import HomePage


"""Класс для функций-предусловий, которые подготавливают состояние системы перед тестом"""


class Preconditions(BasePage):

    @allure.step("Предусловие: Авторизация пользователя")
    def authorize_user(self):
        """Выполняет авторизацию пользователя на сайте."""
        logging.info("Start of user authorization")

        username = Config.TEST_USERNAME
        password = Config.TEST_PASSWORD

        self.fill_element(AuthorizedPageLocators.FIELD_USERNAME, username)
        self.fill_element(AuthorizedPageLocators.FIELD_PASSWORD, password)
        self.click_element(AuthorizedPageLocators.BUTTON_AUTHORIZED)
        time.sleep(2)
        welcome_user = self.wait_visible_element(HomePageLocators.BUTTON_AUTHORIZED)
        if welcome_user:
            self.click_element(HomePageLocators.BUTTON_LOGO)
            logging.info("The user has been successfully authorized.")
            return
        else:
            logging.info("The user has not been successfully authorized.")
            assert False, "Пользователь не авторизован! Тест остановлен."

    @allure.step("Добавление товаров из разных категорий в корзину")
    def add_products_from_different_slider_to_cart(self):
        """Добавляет в корзину по одному товару из слайдеров 'Десерты' 'Пицца' 'Напитки'."""
        logging.info("Start adding items to cart")

        home_page = HomePage(self.driver)
        # Добавляем первую Пиццу в слайдере
        home_page.hover_pizza_image_1()
        self.wait_visible_element(HomePageLocators.BUTTON_ADD_TO_PIZZA_1)
        self.click_element(HomePageLocators.BUTTON_ADD_TO_PIZZA_1)

        # Прокручиваем страницу вниз
        self.scroll_to_element_by_locator(HomePageLocators.SLIDER_DESERTS)

        # Добавляем первый десерт в слайдере в корзину
        home_page.hover_desert_image_1()
        self.wait_visible_element(HomePageLocators.BUTTON_ADD_TO_CART_DESERT)
        self.click_element(HomePageLocators.BUTTON_ADD_TO_CART_DESERT)

        # Прокручиваем страницу вниз
        self.scroll_to_element_by_locator(HomePageLocators.SLIDER_DRINKS)

        # Добавляем первый напиток в слайдере в корзину
        home_page.hover_drink_image_1()
        self.wait_visible_element(HomePageLocators.BUTTON_ADD_TO_CART_DRINK)
        self.click_element(HomePageLocators.BUTTON_ADD_TO_CART_DRINK)

        # Переходим в корзину
        self.scroll_to_top()
        home_page.hover_trash_can_icon()
        home_page.click_trash_can_icon()
        return
