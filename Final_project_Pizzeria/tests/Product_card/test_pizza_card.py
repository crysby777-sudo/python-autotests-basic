import allure
from src.actions.locators import CardProductLocators, HomePageLocators
from allure import step
from config import Config
from src.actions.pages.home_page import HomePage
from src.actions.pages.card_pizza_page import PizzaCard
from src.actions.pages.basket_page import BasketPage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Функциональное тестирование карточки товара")
class TestPizzaCard:

    @allure.title("Переход на страницу описания пиццы при клике на изображение")
    def test_open_pizza_card(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Проверка того, что открылась карточка товара
        """
        open_url(Config.BASE_URL)
        pizza_page = PizzaCard(selenium)

        with step("Навести курсор на третью пиццу в слайдере и кликнуть"):
            pizza_page.hover_and_click_pizza_image(HomePageLocators.IMAGE_PIZZA_3)

        with step("Проверка того, что открылась страница с карточкой товара"):
            pizza_page.verifying_product_pizza_page_opened()

    @allure.title("Проверка соответствия названия пиццы в слайдере и карточке товара")
    def test_pizza_names_slider_and_product_card(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Запомнить название пиццы и сделать клик по картинке товара
        3. Сравнить название пиццы в карточке товара с названием на картинке в слайдере
        """

        open_url(Config.BASE_URL)
        pizza_page = PizzaCard(selenium)
        home_page = HomePage(selenium)

        with step("Зафиксировать название и цену второй пиццы в слайдере"):
            title_pizza_in_slider = home_page.get_second_pizza_name().lower()

        with step("Навести курсор на вторую пиццу в слайдере и кликнуть"):
            pizza_page.hover_and_click_pizza_image(HomePageLocators.IMAGE_PIZZA_2)

        with step(
                "Сравнение название пиццы в карточке товара с названием на картинке в слайдере"
        ):
            pizza_page.assert_product_card_opened(title_pizza_in_slider)

    @allure.title("Выбор дополнительных опций в каточке пиццы (сырный борт)")
    def test_selecting_additional_options_on_the_pizza_card(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Навести курсор на селектор с выбором борта для пиццы
        4. Сделать клик по селектору с выбором борта для пиццы
        5. Сделать клик по любому виду борта пиццы
        6. Проверка того, что стоимость пиццы изменилась
        """
        open_url(Config.BASE_URL)
        pizza_page = PizzaCard(selenium)

        with step("Навести курсор на первую пиццу в слайдере и кликнуть"):
            pizza_page.hover_and_click_pizza_image(HomePageLocators.IMAGE_PIZZA_1)

        with step("Фиксируем стартовую стоимость пиццы"):
            old_price = pizza_page.get_pizza_cost()

        with step("Навести курсор на селектор с выбором борта для пиццы"):
            pizza_page.hover_selector_bort()

        with step("Сделать клик по селектору с последующим выбором борта 'Сырный'"):
            pizza_page.select_option_bort(CardProductLocators.SELECT_BORT, "Сырный - 55.00 р.")

        with step("Проверка того, что стоимость пиццы изменилась"):
            pizza_page.assert_pizza_cost(old_price)

    @allure.title("Добавление пиццы в корзину с дополнительной опцией (колбасный борт")
    def test_add_map_options_to_cart(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор любую понравившуюся картинку с пиццей
        2. Сделать клик по картинке с пиццей
        3. Навести курсор на селектор с выбором борта для пиццы
        4. Сделать клик по селектору с выбором борта для пиццы
        5. Сделать клик по виду 'Колбасный' борт пиццы
        6. Навести курсор на кнопку добавления пиццы в корзину
        7. Перейти в корзину
        8. Проверка того что в корзине отображается добавленная пицца с доп опцией
        """
        open_url(Config.BASE_URL)
        pizza_page = PizzaCard(selenium)
        home_page = HomePage(selenium)
        basket_page = BasketPage(selenium)

        with step("Навести курсор на вторую пиццу в слайдере и кликнуть"):
            pizza_page.hover_and_click_pizza_image(HomePageLocators.IMAGE_PIZZA_2)

        with step("Навести курсор на селектор с выбором борта для пиццы"):
            pizza_page.hover_selector_bort()

        with step("Сделать клик по селектору с последующим выбором борта 'Колбасный'"):
            pizza_page.select_option_bort(CardProductLocators.SELECT_BORT, "Колбасный - 65.00 р.")

        with step('Навести указатель мыши и кликнуть по кнопке "В корзину"'):
            pizza_page.hover_and_click_add_to_cart()

        with step('Наведение курсора на иконку корзины в хедере страницы'):
            home_page.hover_trash_can_icon()

        with step('Сделать клик по кнопке перехода в корзину'):
            home_page.click_trash_can_icon()

        with step(
            'Выполняем проверку, что в корзине отображается пицца с доп опцией "Колбасный борт"'
        ):
            basket_page.pizza_basket_title_bort()
