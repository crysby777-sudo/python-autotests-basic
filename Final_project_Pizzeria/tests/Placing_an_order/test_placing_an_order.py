import time
import allure
from src.actions.helpers.preconditions_helpers import Preconditions
from allure import step
from config.configuration import Config
from src.actions.pages.basket_page import BasketPage
from src.actions.pages.order_page import PlacingAnOrder


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Оформление заказа валидными данными")
class TestPlacingAnOrder:
    @allure.title("Оформление заказа валидными данными")
    def test_placing_an_order(self, selenium, open_url):
        """
        Предусловия: пользователь авторизован под тестовыми данными Имя: olegtest Пароль: 12345
                    В корзине присутствуют добавленные товары: пицца, десерт, напиток

        Шаги:
        1. Навести указатель к кнопке 'Перейти к оплате' и кликнуть
        2. Заполнить форму заказа
        3. Фиксируем данные на странице оформления заказа: общая стоимость,
           email пользователя, дату заказа, способ оплаты
        4. Нажимаем кнопку оформить заказ
        5. Выполняем проверку подтверждение заказа, общую сумму и свои личные данные.
        """

        basket_pages = BasketPage(selenium)
        order_pages = PlacingAnOrder(selenium)

        with step("Выполняем предусловия: авторизация, добавление товаров в корзину"):
            open_url(Config.AUTHORIZATION_URL)
            precondition_actions = Preconditions(selenium)
            precondition_actions.authorize_user()
            precondition_actions.add_products_from_different_slider_to_cart()

        with step("Навести указатель к кнопке 'Перейти к оплате' и кликнуть"):
            basket_pages.click_button_PROCEED_TO_PAYMENT()

        with step("Заполнить форму заказа"):
            order_pages.filling_in_the_fields_on_the_order()

        with step("Фиксируем данные на странице оформления заказа: общая стоимость,"
                  " email пользователя, дату заказа, способ оплаты"):
            total, email, payment, order_date = order_pages.recording_order_information()

        with step("Нажимаем кнопку Оформить заказ"):
            order_pages.click_place_an_order()
            time.sleep(1)

        with step("Выполняем проверку подтверждение заказа, общую сумму и свои личные данные."):
            order_pages.check_final_order(total, email, payment, order_date)
