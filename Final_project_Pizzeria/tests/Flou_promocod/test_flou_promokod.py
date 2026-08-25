import allure
from allure import step
from src.actions.pages.home_page import HomePage
from src.actions.pages.order_page import PlacingAnOrder
from src.actions.helpers.preconditions_helpers import Preconditions
from src.actions.pages.registration_page import RegistrationPage
from config.configuration import Config
from src.actions.pages.basket_page import BasketPage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала использования промокодов сайта Pizzeria")
@allure.story("Проверка применение валидного и невалидного промокодов")
class TestDiscount:
    @allure.title("Проверка применения скидки 10% по валидному промокоду GIVEMEHALYAVA")
    def test_applying_code_GIVEMEHALYAVA(self, open_url, selenium):
        """
        Сценарий №1
        Предусловия: пользователь авторизован под тестовыми данными Имя: olegtest Пароль: 12345
                    Купон в корзине не применён ранее
                    В корзине присутствуют добавленные товары: пицца, десерт, напиток
           Шаги:
            1. Перейти в окно оформления товаров.
            2. Применить промокод GIVEMEHALYAVA.
            3. Убедиться, что конечная сумма заказа уменьшилась на 10%.
        """

        basket_page = BasketPage(selenium)
        order_page = PlacingAnOrder(selenium)

        with step("Выполняем предусловия"):
            open_url(Config.AUTHORIZATION_URL)
            precondition_actions = Preconditions(selenium)
            precondition_actions.authorize_user()
            precondition_actions.add_products_from_different_slider_to_cart()
            basket_page.reset_coupon()

        with step("Выполнение перехода на страницу оформления заказа"):
            basket_page.click_button_PROCEED_TO_PAYMENT()

        with step("Фиксируем начальную стоимость заказа"):
            total_order_old = order_page.recording_order_information()[0]

        with step("Активация промокода GIVEMEHALYAVA"):
            order_page.using_the_promo_code(Config.CORRECT_PROMOCOD)

        with step("Фиксируем обновленную стоимость заказа"):
            total_order_new = order_page.recording_order_information()[0]

        with step("Выполнить проверку уменьшения стоимости заказа на 10%"):
            order_page.check_order_reduction_by_10proc(total_order_old, total_order_new)

    @allure.title("Проверка применения невалидного промокода DC120")
    def test_applying_wrong_code_DC120(self, open_url, selenium):
        """
        Сценарий №2
        Предусловия: пользователь авторизован под тестовыми данными Имя: olegtest Пароль: 12345
                    В корзине присутствуют добавленные товары: пицца, десерт, напиток
                    Купон в корзине не применён ранее

            Шаги:
            1. Перейдите в окно оформления товаров.
            2. Зафиксировать начальную стоимость заказа
            2. Примените промокод DC120.
            3. Проверка, что невалидный промокод не применяется и цена не меняется
        """

        basket_page = BasketPage(selenium)
        order_page = PlacingAnOrder(selenium)
        home_page = Preconditions(selenium)

        with step("Выполняем предусловия"):
            open_url(Config.AUTHORIZATION_URL)
            home_page.authorize_user()
            home_page.add_products_from_different_slider_to_cart()
            basket_page.reset_coupon()

        with step("Выполнение перехода на страницу оформления заказа"):
            basket_page.click_button_PROCEED_TO_PAYMENT()

        with step("Фиксируем начальную стоимость заказа"):
            total_order_old = order_page.recording_order_information()[0]

        with step("Активация промокода DC120"):
            order_page.using_the_promo_code(Config.WRONG_PROMOCOD)

        with step("Фиксируем обновленную стоимость заказа"):
            total_order_new = order_page.recording_order_information()[0]

        with step("Выполнить проверку что промокод не применился,"
                  " присутствует сообщение о неверном купоне"):
            order_page.check_order_wrong_promo_code(total_order_old, total_order_new)

    @allure.title("Проверка применения промокода GIVEMEHALYAVA с блокировкой "
                  "отправки запроса на сервер")
    def test_blocking_the_sending_of_requests_to_the_server(self, open_url, selenium):
        """
        Сценарий №3
        Предусловия: пользователь авторизован под тестовыми данными Имя: olegtest Пароль: 12345
                    В корзине присутствуют добавленные товары: пицца, десерт, напиток


            Шаги:
            1. Перейти в окно оформления товаров.
            2. Подготовить перехват запроса применения промокода на сервер.
            3. Зафиксировать общую стоимость заказа
            4. Применить промокод GIVEMEHALYAVA.
            5. Проверить, что конечная сумма заказа не уменьшилась на 10% и промокод не
               применился,
        """

        basket_page = BasketPage(selenium)
        order_page = PlacingAnOrder(selenium)

        with step("Выполняем предусловия"):
            open_url(Config.AUTHORIZATION_URL)
            home_page = Preconditions(selenium)
            home_page.authorize_user()
            home_page.add_products_from_different_slider_to_cart()
            basket_page.reset_coupon()

        with step("Выполнение перехода на страницу оформления заказа"):
            basket_page.click_button_PROCEED_TO_PAYMENT()

        with step("Запускаем функцию перехвата запроса применения промокода"):
            order_page.blocking_request_server_coupon(selenium, blocked_request="*apply_coupon*")

        with step("Фиксируем начальную стоимость заказа"):
            total_order_old = order_page.recording_order_information()[0]

        with step("Активация промокода GIVEMEHALYAVA"):
            order_page.using_the_promo_code(Config.CORRECT_PROMOCOD)

        with step("Фиксируем обновленную стоимость заказа"):
            total_order_new = order_page.recording_order_information()[0]

        with step("Выполнить проверку что промокод не применился"):
            order_page.check_order_reduction_blocking_request(total_order_old, total_order_new)

    @allure.title("Проверка применения промокода GIVEMEHALYAVA повторно")
    def test_rechecking_promo_code_application(self, open_url, selenium):
        """
        Сценарий №4
         Шаги:
         1. Регистрируем нового пользователя
         2. Добавляем товары в корзину
         3. Переходим к странице оформления заказа и заполняем форму оформления заказа
         4. Вводим и применяем промокод GIVEMEHALYAVA
         5. Оформляем заказ нажимаем оформить заказ
         6. Переходим на главную страницу
         7. Добавляем со слайдера пиццу в корзину
         8. Переходим к оформлению заказа
         9. Вводим и применяем промокод GIVEMEHALYAVA
         10. Выполняем проверку, что промокод не применился, общая стоимость и итоговая сумма одинаковы
        """
        open_url(Config.REGISTRATION_URL)
        order_page = PlacingAnOrder(selenium)
        filling_shopping_cart = Preconditions(selenium)
        home_page = HomePage(selenium)
        register_page = RegistrationPage(selenium)
        home_page.logout_else_authorized()

        with step("Регистрируем нового пользователя"):
            register_page.register_new_user_generate()

        with step("Добавляем товары в корзину"):
            filling_shopping_cart.add_products_from_different_slider_to_cart()

        with step("Переходим к странице оформления заказа"):
            home_page.hover_place_order()
            home_page.click_place_order()

        with step("Заполняем форму оформления заказа"):
            order_page.filling_in_the_fields_on_the_order()

        with step("Вводим и применяем промокод GIVEMEHALYAVA"):
            order_page.using_the_promo_code(Config.CORRECT_PROMOCOD)

        with step("Нажать оформить заказ"):
            order_page.click_place_an_order()

        with step("Переходим на главную страницу"):
            home_page.go_to_homepage()

        with step("Добавляем третью пиццу в слайдере в корзину"):
            home_page.hover_pizza_image_3()
            home_page.click_add_to_cart_pizza_3()

        with step("Переходим к странице оформлению заказа"):
            home_page.hover_place_order()
            home_page.click_place_order()

        with step("Вводим и применяем промокод GIVEMEHALYAVA"):
            order_page.using_the_promo_code(Config.CORRECT_PROMOCOD)

        with step("Фиксируем общую стоимость и итоговую сумму заказа"):
            total_cost, total_sum = order_page.recording_order_cost()

        with step("Выполняем проверку что промокод не применился: общая стоимость и итоговая сумма заказа одинаковы"):
            order_page.check_re_use_promo_code_next_order(total_cost, total_sum)
