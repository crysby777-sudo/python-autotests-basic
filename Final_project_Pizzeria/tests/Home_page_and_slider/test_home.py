import logging
import time
from allure import epic, feature, step, story, title
from config import Config
from src.actions.pages.home_page import HomePage


@epic("Финальная работа по курсу «Автотесты на Python")
@feature("Тестирование функционала сайта Pizzeria")
@story("Функциональное тестирование главной страницы и слайдера Пицца")
class TestHomePage:

    @title("Отображение главной страницы сайта")
    def test_home_page(self, open_url, selenium):
        """
        Шаги:
            1. Выполнить переход на главную страницу сайта.
            2. Выполнить проверку того, что открылся нужный сайт.
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)

        with step("Проверяем, что открылся нужный сайт"):
            home_page.is_page_opened()

    @title("Проверка наличия на странице слайдера с пиццами")
    def test_page_slider(self, open_url, selenium):
        """
        Шаги:
            1. Выполнить переход на главную страницу сайта.
            2. Проверить присутствие слайдера 'Пицца'.
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)

        with step("Проверяем, что на странице присутствует слайдер с пиццами"):
            home_page.is_pizza_slider_visible()

    @title("Отображение кнопки 'В корзину' при наведении указателя мыши на изображение пиццы в слайдере")
    def test_slider_add_to_cart(self, open_url, selenium):
        """
        Шаги:
            1. Навести указатель мыши на любую пиццу в слайдере.
            2. Проверить появление кнопки 'В корзину'.
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)

        with step("Навести курсор на картинку с пиццей"):
            home_page.hover_pizza_image_1()

        with step("Проверяем, что появилась кнопка 'В корзину'"):
            home_page.is_add_to_cart_button_visible()

    @title("Проверка кликабельности кнопки прокрутки слайдера 'Пицца' влево")
    def test_button_slider_left(self, open_url, selenium):
        """
        Шаги:
            1. Получить название первой пиццы.
            2. Кликнуть по кнопке прокрутки влево.
            3. Проверить, что первая пицца сместилась вправо.
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)

        with step("Навести курсор на слайдер и зафиксировать название первой пиццы"):
            home_page.hover_pizza_image_1()
            product_name_pizza_first = home_page.get_first_pizza_name()

        with step("Сделать клик по левой кнопке слайдера"):
            home_page.click_slider_left()
            product_name_pizza_second = home_page.get_second_pizza_name()

        with step("Проверка того, что первая пицца сместилась вправо"):
            assert product_name_pizza_first == product_name_pizza_second

    @title("Проверка кликабельности кнопки прокрутки слайдера 'Пицца' вправо")
    def test_button_slider_right(self, open_url, selenium):
        """
        Шаги:
            1. Навести курсор на слайдер и зафиксировать название последней пиццы.
            2. Кликнуть по правой кнопке слайдера.
            3. Проверить, что последняя пицца сместилась влево.
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)

        with step("Навести курсор на слайдер и зафиксировать название последней пиццы"):
            home_page.hover_pizza_image_4()
            product_name_pizza_last = home_page.get_last_pizza_name()

        with step("Сделать клик по правой кнопке слайдера"):
            home_page.click_slider_right()
            product_name_pizza_penultimate = home_page.get_penultimate_pizza_name()

        with step("Проверка того, что последняя пицца сместилась влево на одну позицию"):
            logging.info(f"Last: {product_name_pizza_last}, Penultimate: {product_name_pizza_penultimate}")
            assert product_name_pizza_last == product_name_pizza_penultimate

    @title("Проверка добавления нескольких пицц в корзину со слайдера главной страницы")
    def test_pizza_name_matching_slider_and_card(self, open_url, selenium):
        """
        Шаги:
            1. Зафиксировать начальную стоимость корзины.
            2. Добавить первую пиццу в корзину.
            3. Прокрутить слайдер вправо и добавить ещё пиццы.
            4. Проверить, что стоимость корзины изменилась.
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)

        with step("Фиксируем стартовую стоимость корзины"):
            old_cost = home_page.get_basket_cost()

        with step("Навести курсор на первую пиццу и нажать 'В корзину'"):
            home_page.hover_pizza_image_1()
            home_page.click_add_to_cart_pizza_1()

        with step("Нажать правую кнопку прокрутки слайдера"):
            home_page.hover_pizza_image_1()
            home_page.click_slider_right()

        with step("Добавить первую пиццу в корзину"):
            home_page.hover_pizza_image_1()
            home_page.click_add_to_cart_pizza_1()

        with step("Навести курсор на третью пиццу и добавить в корзину"):
            home_page.hover_pizza_image_3()
            home_page.click_add_to_cart_pizza_3()
            time.sleep(1)

        with step("Проверка того, что стоимость корзины изменилась"):
            new_cost = home_page.get_basket_cost()
            home_page.compare_basket_cost(old_cost, new_cost)
