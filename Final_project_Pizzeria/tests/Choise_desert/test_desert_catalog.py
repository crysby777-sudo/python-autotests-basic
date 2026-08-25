import allure
from allure import step
from config.configuration import Config
from src.actions.pages.home_page import HomePage
from src.actions.pages.menu_desert_page import MenuDropdownDesertPage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story('Функциональное тестирование вкладки "Меню"')
class TestPageMenu:

    @allure.title(
        'Открытие выпадающего списка при наведении курсора на вкладку "Меню" из рубрикатора главной страницы'
    )
    def test_open_page_menu(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор на вкладку "Меню"
        2. Проверка того, что появляется выпадающий список
        """
        open_url(Config.BASE_URL)
        menu_page = MenuDropdownDesertPage(selenium)

        with step('Навести курсор на вкладку "Меню"'):
            menu_page.open_drop_down_menu()

        with step("Проверка того, что появляется выпадающий список"):
            menu_page.is_dropdown_list()

    @allure.title('Переход в каталог «Десерты» из выпадающего списка вкладки "Меню"')
    def test_go_to_desserts(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор на вкладку "Меню" в рубрикаторе
        2. Навести курсор на раздел "Десерты"
        3. Сделать клик по разделу "Десерты"
        4. Проверка того, что открылась страница с десертом
        """
        open_url(Config.BASE_URL)
        desert_page = MenuDropdownDesertPage(selenium)

        with step('Навести курсор на вкладку "Меню"'):
            desert_page.open_drop_down_menu()

        with step('Навести курсор на раздел "Десерты" в выпадающем списке и сделать клик'):
            desert_page.open_desert_in_menu()

        with step("Проверка того, что открылась страница с десертами"):
            desert_page.verifying_menu_deserts_page_opened()

    @allure.title('Фильтрация товаров по цене <= 135 рублей на страницы "Десерты"')
    def test_desert_filtering(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор на правый ползунок фильтра по цене
        2. Установить правый ползунок фильтра по цене товара, в диапазон до 135 рублей, включительно
        3. Навести курсор на кнопку "Применить"
        4. Сделать клик по кнопке "Применить"
        5. Проверка того, что отображается товар удовлетворяющий условиям установленного фильтра
        """
        open_url(Config.DESERT_URL)
        desert_page = MenuDropdownDesertPage(selenium)
        target_price = 135
        with step("Навести курсор на правый ползунок фильтра по цене"):
            desert_page.price_adjustment_right()

        with step(
                "Установить правый ползунок фильтра по цене товара, в диапазон до 135 рублей, включительно"
        ):
            desert_page.setting_price_range(target_price)

        with step('Навести курсор на кнопку Применить'):
            desert_page.hovering_apply_price_button()

        with step('Сделать клик по кнопке Применить'):
            desert_page.click_apply_price_button()

        with step("Проверка того, что стоимость отображаемых "
                  "товаров не превышает {target_price} руб."):
            desert_page.check_on_filtered_products(target_price)

    @allure.title("Добавление десерта в корзину")
    def test_adding_dessert_to_the_cart(self, open_url, selenium):
        """
        Шаги:
        1. Навести курсор на кнопку "В корзину" любого десерта
        2. Сделать клик по кнопке "В корзину"
        3. Проверка того, что сумма корзины изменилась
        """

        open_url(Config.DESERT_URL)
        page_desert = MenuDropdownDesertPage(selenium)
        home_page = HomePage(selenium)

        with step("Фиксируем стартовую стоимость корзины"):
            old_cost = page_desert.get_basket_cost_catalog()

        with step('Навести курсор на кнопку "В корзину" любого десерта'):
            page_desert.hovering_add_to_cart_in_catalog()

        with step('Сделать клик по кнопке "В корзину"'):
            page_desert.click_add_to_cart_in_catalog()

        with step("Проверка того, что сумма корзины изменилась"):
            new_cost = page_desert.get_basket_cost_catalog()
            home_page.compare_basket_cost(old_cost, new_cost)
