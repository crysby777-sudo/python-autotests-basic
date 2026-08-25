import time
import allure
from allure import step
from config.configuration import Config
from src.actions.pages.basket_page import BasketPage
from src.actions.pages.home_page import HomePage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Удаление и добавление товаров со страницы 'Корзина'")
class TestBasketPage:
    @allure.title("Проверка отображения в корзине добавленного товара со слайдера <Пицца>")
    def test_displaying_the_added_product_in_the_cart(self, open_url, selenium):
        """ Шаги:
    1. Навести курсор первую картинку с пиццей в слайдере
    2. Навести курсор на кнопку добавления пиццы в корзину
    3. Сделать клик по кнопке "В корзину"
    4. Навести курсор на иконку корзины в хедере страницы
    5. Сделать клик по иконке корзины в хедере страницы
    6. Поверить наличия добавленной пиццы в корзине
    """
        open_url(Config.BASE_URL)
        basket_page = BasketPage(selenium)
        home_page = HomePage(selenium)

        with step("Зафиксировать название первой пиццы в слайдере"):
            name_added_pizza = home_page.get_first_pizza_name()

        with step("Навести курсор первую картинку с пиццей в слайдере <Пицца>"):
            home_page.hover_pizza_image_1()

        with step("Навести курсор первую картинку с пиццей в слайдере <Пицца>"):
            home_page.hover_pizza_image_1()

        with step("Кликнуть кнопку <В корзину>"):
            home_page.click_add_to_cart_pizza_1()

        with step("Навести курсор на иконку корзины в хедере страницы"):
            home_page.hover_trash_can_icon()
            time.sleep(3)

        with step("Выполнить клик по иконке корзины в хедере страницы"):
            home_page.click_trash_can_icon()

        with step("Поверить наличия добавленной пиццы на странице корзины"):
            basket_page.pizza_added_basket(name_added_pizza)

    @allure.title("Увеличение количества товаров  на странице 'Корзина'")
    def test_increase_item_quantity_in_cart(self, open_url, selenium):
        """
        Шаги:
            1. Навести курсор первую картинку с пиццей в слайдере
            2. Навести курсор на кнопку добавления пиццы в корзину
            3. Сделать клик по кнопке "В корзину"
            4. Навести курсор на иконку корзины в хедере страницы
            5. Сделать клик по иконке корзины в хедере страницы
            6. Зафиксировать стартовую стоимость корзины
            7. Навести курсор на кнопку на окно добавления количества пицц
            8. Увеличить количество пицц на одну позицию
            9. Навести курсор на кнопку "Обновить корзину"
            10. Сделать клик по кнопке "Обновить корзину"
            11. Выполнить проверку того что итоговая сумма корзины изменилась
        """
        open_url(Config.BASE_URL)
        basket_page = BasketPage(selenium)
        home_page = HomePage(selenium)

        with step("Навести курсор вторую картинку с пиццей в слайдере <Пицца>"):
            home_page.hover_second_pizza_image()

        with step("Кликнуть кнопку <В корзину>"):
            home_page.click_add_to_cart_pizza_2()

        with step("Навести курсор на иконку корзины в хедере страницы"):
            home_page.hover_trash_can_icon()

        with step("Выполнить клик по иконке корзины в хедере страницы"):
            home_page.click_trash_can_icon()

        with step("Фиксируем стартовую стоимость корзины"):
            old_amount = basket_page.total_amount_of_the_cart()

        with step('Навести указатель мыши на окно изменения количества товаров'):
            basket_page.hover_increase_in_quantity()

        with step('Увеличить количество товара на одну позицию'):
            basket_page.added_products_on_the_cart_page()

        with step('Навести указатель мыши на кнопку "Обновить корзину"'):
            basket_page.hover_button_update_cart()

        with step('Сделать клик по кнопке "Обновить корзину"'):
            basket_page.click_button_update_cart()

        with step("Проверка того, что общая стоимость корзины изменилась"):
            basket_page.checking_adding_quantity(old_amount)

    @allure.title("Удаление пиццы из корзины на странице 'Корзина'")
    def test_delete_pizza_with_option_from_cart(self, selenium, open_url):
        """
            Шаги:
                1. Навести курсор на четвёртую пиццу в слайдере
                2. Навести курсор на кнопку добавления пиццы в корзину
                3. Сделать клик по кнопке "В корзину"
                4. Навести курсор на кнопку перехода на страницу корзины
                5. Сделать клик по кнопке перехода на страницу корзины
                6. Навести курсор на кнопку удаления товара из корзины(крестик)
                7. Сделать клик по кнопке удаления товара из корзины(крестик)
                8. Выполнить проверку того что появилось сообщение "Корзина пуста"
                """
        open_url(Config.BASE_URL)
        basket_page = BasketPage(selenium)
        home_page = HomePage(selenium)

        with step("Навести курсор на четвёртую картинку с пиццей в слайдере <Пицца>"):
            home_page.hover_fourth_pizza_image()

        with step("Кликнуть кнопку <В корзину>"):
            home_page.click_add_to_cart_pizza_4()

        with step("Навести курсор на иконку корзины в хедере страницы"):
            home_page.hover_trash_can_icon()

        with step("Выполнить клик по иконке корзины в хедере страницы"):
            home_page.click_trash_can_icon()

        with step('Навести указатель мыши на кнопку удаления товара из корзины'):
            basket_page.hovering_over_the_pizza_removal_button()

        with step('Сделать клик по кнопке(крестик)'):
            basket_page.click_over_the_pizza_removal_button()

        with step('Выполнить проверку появления сообщения на странице "Корзина пуста"'):
            basket_page.verifying_message_has_appeared()
