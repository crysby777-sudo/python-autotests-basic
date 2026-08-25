import logging
import time
import allure
from actions.pages.base_page import BasePage
from src.actions.locators.page_locators import HomePageLocators


"""Функции взаимодействия с элементами и проверки на главной странице сайта"""


class HomePage(BasePage):

    @allure.step("Проверка, что открылась нужная страница")
    def is_page_opened(self):
        text_url = "https://pizzeria.skillbox.cc/"
        self.attach_screenshot(name="page_opened")
        current_url = self.extraction_url_contains(text_url)
        assert text_url in current_url, f"Ожидалось {text_url} в URL, но получили: {current_url}"
        logging.info(f"Page opened successfully. Current URL: {current_url}")

    @allure.step("Выйти из аккаунта (если авторизован)")
    def logout_else_authorized(self):
        self.logout(HomePageLocators.BUTTON_AUTHORIZED)

    @allure.step("Проверка наличия слайдера 'Пицца'")
    def is_pizza_slider_visible(self):
        self.attach_screenshot(name="pizza_slider")
        assert self.wait_visible_element(HomePageLocators.SLIDER_PIZZA)

    @allure.step("Наведение курсора на первую пиццу в слайдере")
    def hover_pizza_image_1(self):
        self.go_to_element(HomePageLocators.IMAGE_PIZZA_1)

    @allure.step("Наведение курсора на первый десерт в слайдере")
    def hover_desert_image_1(self):
        self.go_to_element(HomePageLocators.IMAGE_DESERT_1)

    @allure.step("Наведение курсора на первый напиток в слайдере")
    def hover_drink_image_1(self):
        self.go_to_element(HomePageLocators.IMAGE_DRINK_1)

    @allure.step("Наведение курсора на третью пиццу в слайдере")
    def hover_pizza_image_3(self):
        self.go_to_element(HomePageLocators.IMAGE_PIZZA_3)

    @allure.step("Наведение курсора на четвертую пиццу в слайдере")
    def hover_pizza_image_4(self):
        self.go_to_element(HomePageLocators.IMAGE_PIZZA_4)

    @allure.step("Проверка отображение кнопки 'В корзину'")
    def is_add_to_cart_button_visible(self):
        self.attach_screenshot(name="add_to_cart_button")
        assert self.wait_visible_element(HomePageLocators.BUTTON_ADD_TO_PIZZA_1)

    @allure.step("Нажатие на кнопку прокрутки слайдера влево")
    def click_slider_left(self):
        self.go_to_element(HomePageLocators.BUTTON_LEFT)
        self.click_element(HomePageLocators.BUTTON_LEFT)
        time.sleep(1)

    @allure.step("Нажатие на кнопку прокрутки слайдера вправо")
    def click_slider_right(self):
        self.go_to_element(HomePageLocators.BUTTON_RIGHT)
        self.click_element(HomePageLocators.BUTTON_RIGHT)
        time.sleep(1)

    @allure.step("Получение названия первой пиццы в слайдере")
    def get_first_pizza_name(self) -> str:
        return self.wait_visible_element(HomePageLocators.TITLE_PIZZA_IN_SLIDER_1).text

    @allure.step("Получения названия второй пиццы в слайдере")
    def get_second_pizza_name(self) -> str:
        return self.wait_visible_element(HomePageLocators.TITLE_PIZZA_IN_SLIDER_2).text

    @allure.step("Получения названия последней пиццы в слайдере")
    def get_last_pizza_name(self) -> str:
        return self.wait_visible_element(HomePageLocators.TITLE_PIZZA_IN_SLIDER_4).text

    @allure.step("Получения названия предпоследней пиццы в слайдере")
    def get_penultimate_pizza_name(self) -> str:
        return self.wait_visible_element(HomePageLocators.TITLE_PIZZA_IN_SLIDER_3).text

    @allure.step("Нажатие кнопки 'В корзину' для первой пиццы в слайдере")
    def click_add_to_cart_pizza_1(self):
        self.click_element(HomePageLocators.BUTTON_ADD_TO_PIZZA_1)

    @allure.step("Нажатие кнопки 'В корзину' для второй пиццы в слайдере")
    def click_add_to_cart_pizza_2(self):
        self.click_element(HomePageLocators.BUTTON_ADD_TO_PIZZA_2)

    @allure.step("Нажатие кнопки 'В корзину' для третьей пиццы в слайдере")
    def click_add_to_cart_pizza_3(self):
        self.click_element(HomePageLocators.BUTTON_ADD_TO_PIZZA_3)

    @allure.step("Нажатие кнопки 'В корзину' для четвёртой пиццы в слайдере")
    def click_add_to_cart_pizza_4(self):
        self.click_element(HomePageLocators.BUTTON_ADD_TO_PIZZA_4)

    @allure.step("Получение текущей стоимости корзины")
    def get_basket_cost(self) -> str:
        self.attach_screenshot("basket_cost")
        return self.wait_visible_element(HomePageLocators.BASKET_COST).text

    @allure.step("Наведение курсора на вторую пиццу в слайдере")
    def hover_second_pizza_image(self):
        self.go_to_element(HomePageLocators.IMAGE_PIZZA_2)

    @allure.step("Наведение курсора на четвертую пиццу в слайдере")
    def hover_fourth_pizza_image(self):
        self.go_to_element(HomePageLocators.IMAGE_PIZZA_4)

    @allure.step("Наведение курсора на иконку корзины в хедере страницы")
    def hover_trash_can_icon(self):
        self.go_to_element(HomePageLocators.BASKET_COST)
        time.sleep(1)

    @allure.step("Наведение курсора на вкладку Мой аккаунт в рубрикаторе страницы")
    def hover_my_account_tab(self):
        self.go_to_element(HomePageLocators.BUTTON_MY_ACCOUNT)

    @allure.step("Клик по вкладке Мой аккаунт в рубрикаторе страницы")
    def click_my_account_tab(self):
        self.click_element(HomePageLocators.BUTTON_MY_ACCOUNT)

    @allure.step("Наведение курсора на вкладку Оформить заказ в рубрикаторе страницы")
    def hover_place_order(self):
        self.click_element(HomePageLocators.BUTTON_PLACING_ORDER)

    @allure.step("Клик по вкладке Оформить заказ в рубрикаторе страницы")
    def click_place_order(self):
        self.click_element(HomePageLocators.BUTTON_PLACING_ORDER)

    @allure.step("Клик по иконке корзины в хедере страницы")
    def click_trash_can_icon(self):
        self.click_element(HomePageLocators.BASKET_COST)
        time.sleep(1)

    @allure.step("Сравнение начальной и финальной стоимости корзины")
    def compare_basket_cost(self, old_cost, new_cost):
        self.attach_screenshot("compare_basket_cost")
        logging.info(f" Initial basket amount = {old_cost}")
        logging.info(f" Final cart total = {new_cost}")
        assert old_cost != new_cost

    @allure.step("Функция наведение на кнопку Войти в хедере страницы")
    def hover_authorization_button(self):
        self.go_to_element(HomePageLocators.BUTTON_AUTHORIZED)

    @allure.step("Функция клика по кнопке Войти в хедере страницы")
    def click_authorization_button(self):
        self.click_element(HomePageLocators.BUTTON_AUTHORIZED)

    @allure.step("Переход на главную страницу")
    def go_to_homepage(self):
        self.go_to_element(HomePageLocators.BUTTON_LOGO)
        self.click_element(HomePageLocators.BUTTON_LOGO)
        time.sleep(1)
