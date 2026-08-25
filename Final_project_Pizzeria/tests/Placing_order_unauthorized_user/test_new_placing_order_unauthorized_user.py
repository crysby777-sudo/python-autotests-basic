import allure
from allure import epic, feature, step, story, title
from config import Config
from src.actions.pages.home_page import HomePage
from src.actions.pages.basket_page import BasketPage
from src.actions.pages.chekout_page import CheckoutPage


@epic("Финальная работа по курсу «Автотесты на Python")
@feature("Тестирование функционала сайта Pizzeria")
@story("Оформление заказа не авторизованным пользователем")
class TestPlacingOrderUnauthorizedUser:

    @title(
        'Проверка присутствия кнопки "Перейти к оплате" на странице корзины'
        ' при оформлении заказа не авторизованным пользователем'
    )
    def test_displaying_place_order_button(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Убедиться в переходе на страницу "КОРЗИНА" и наличии кнопки "ПЕРЕЙТИ К ОПЛАТЕ"
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)
        basket_page = BasketPage(selenium)
        home_page.logout_else_authorized()

        with step("Навести курсор на первую картинку с пиццей"):
            home_page.hover_pizza_image_1()

        with step("Нажать кнопку 'В корзину'"):
            home_page.click_add_to_cart_pizza_1()

        with step('Наведение курсора на иконку корзины в хедере страницы'):
            home_page.hover_trash_can_icon()

        with step('Сделать клик по иконке корзины в хедере страницы'):
            home_page.click_trash_can_icon()

        """with step('Навести указатель на кнопку "ПЕРЕЙТИ К ОПЛАТЕ'):
            basket_page.hover_over_the_payment_button()

            with step('Сделать клик по кнопке "ПЕРЕЙТИ К ОПЛАТЕ'):
                basket_page.click_over_the_payment_button()"""

        with step('Выполнить проверку присутствия кнопки "ПЕРЕЙТИ К ОПЛАТЕ" на странице корзины'):
            basket_page.checking_button_PROCEED_TO_PAYMENT()

    @allure.title(
        'Оформление заказа не авторизованным пользователем при нажатии кнопки "Перейти к оплате"'
    )
    def test_placing_order_unauthorized_user(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор на любую пиццу в слайдере
        2. Навести курсор на кнопку "В корзину"
        3. Сделать клик по кнопке "В корзину"
        4. Навести курсор на иконку корзины
        5. Сделать клик по иконке корзины
        6. Навести курсор на кнопку "Перейти к оплате"
        7. Сделать клик по кнопке "Перейти к оплате"
        8. Убедиться в наличии ссылок авторизации и купон
        """
        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)
        basket_page = BasketPage(selenium)
        checkout_page = CheckoutPage(selenium)
        home_page.logout_else_authorized()

        with step("Навести курсор на первую картинку с пиццей"):
            home_page.hover_pizza_image_1()

        with step("Нажать кнопку 'В корзину'"):
            home_page.click_add_to_cart_pizza_1()

        with step('Наведение курсора на иконку корзины в хедере страницы'):
            home_page.hover_trash_can_icon()

        with step('Сделать клик по иконке корзины в хедере страницы'):
            home_page.click_trash_can_icon()

        with step('Навести указатель на кнопку "ПЕРЕЙТИ К ОПЛАТЕ'):
            basket_page.hover_over_the_payment_button()

            with step('Сделать клик по кнопке "ПЕРЕЙТИ К ОПЛАТЕ'):
                basket_page.click_over_the_payment_button()

        with step("Выполнить проверку наличия ссылки авторизации и активации купона"):
            checkout_page.checking_link_authorized_and_coupon()
