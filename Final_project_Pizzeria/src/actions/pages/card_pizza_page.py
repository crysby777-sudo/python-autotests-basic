import logging
import time
import allure
from src.actions.pages.base_page import BasePage
from actions.locators import CardProductLocators


"""Функции взаимодействия с элементами и проверки  на странице карточки товара"""


class PizzaCard(BasePage):

    @allure.step("Наведение и клик по изображению пиццы в слайдере для перехода в карточку товара")
    def hover_and_click_pizza_image(self, image_slider):
        self.go_to_element(image_slider)
        self.attach_screenshot(name="Выбранная пицца")
        self.click_element(image_slider)

    @allure.step("Проверка того что открылась страница карточки товара Пицца")
    def verifying_product_pizza_page_opened(self):
        text_url = "product"
        self.attach_screenshot(name="Пицца нв странице карточки товара")
        current_url = self.extraction_url_contains(text_url)
        assert text_url in current_url, f"Ожидалось {text_url} в URL, но получили: {current_url}"
        logging.info(f"Page opened successfully. Current URL: {current_url}")

    @allure.step("Проверка открытия карточки товара с выбранной пиццей")
    def assert_product_card_opened(self, title_pizza_in_slider):
        self.attach_screenshot("Карточка товара")
        title_pizza_in_card = (self.wait_visible_element
                               (CardProductLocators.TITLE_CARD_PRODUCT).text.lower())
        logging.info(f"Pizza name in the slider /{title_pizza_in_slider}/")
        logging.info(f"Pizza name in the card /{title_pizza_in_card}/")
        assert title_pizza_in_card == title_pizza_in_slider

    @allure.step("Наведение указателя на селектор с выбором борта пиццы")
    def hover_selector_bort(self):
        self.go_to_element(CardProductLocators.SELECT_BORT)

    @allure.step("Клик по селектору с выбором доп опции борта пиццы")
    def select_option_bort(self, locator, bort):
        self.select_options(locator, bort)

    @allure.step("Наведение указателя и клик по кнопке 'В корзину'")
    def hover_and_click_add_to_cart(self):
        self.go_to_element(CardProductLocators.BUTTON_ADD_TO_CART)
        self.click_element(CardProductLocators.BUTTON_ADD_TO_CART)
        time.sleep(2)

    @allure.step("Получение текущей стоимости пиццы")
    def get_pizza_cost(self) -> str:
        self.attach_screenshot(name="Стоимость пиццы до применения доп опции")
        return self.wait_visible_element(CardProductLocators.PRICE_PIZZA).text

    @allure.step("Сравнение стоимости пиццы без и с доп опцией 'сырный борт'")
    def assert_pizza_cost(self, old_price):
        self.attach_screenshot(name="Стоимость пиццы после применения доп опции")
        new_price = self.wait_visible_element(CardProductLocators.PRICE_PIZZA).text
        logging.info(f" Initial pizza amount = {old_price}")
        logging.info(f" Final pizza total = {new_price}")
        assert old_price != new_price
