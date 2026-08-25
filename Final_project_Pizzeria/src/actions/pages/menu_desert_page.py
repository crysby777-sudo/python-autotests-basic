import logging
import time
import allure
from src.actions.pages.base_page import BasePage
from src.actions.locators.page_locators import HomePageLocators, CatalogProductLocators


"""Функции взаимодействия с элементами и проверки  на странице товаров Десерты"""


class MenuDropdownDesertPage(BasePage):

    @allure.step("Наведение указателя на раздел 'Меню'")
    def open_drop_down_menu(self):
        self.go_to_element(HomePageLocators.PAGE_MENU)
        time.sleep(1)

    @allure.step("Проверка выдающего списка 'Меню'")
    def is_dropdown_list(self):
        self.attach_screenshot(name="menu_dropdown")
        assert self.wait_visible_element(HomePageLocators.SUBMENU).is_displayed()

    @allure.step("Наведение указателя  на раздел Десерты с последующим кликом")
    def open_desert_in_menu(self):
        self.go_to_element(HomePageLocators.SUBMENU_DESERTS)
        self.click_element(HomePageLocators.SUBMENU_DESERTS)

    @allure.step("Наведение указателя на правый ползунок фильтра по цене")
    def price_adjustment_right(self):
        self.go_to_element(CatalogProductLocators.RIGHT_PRICE_FILTER_SLIDER)

    @allure.step("Установка фильтра цены до 135 р.")
    def setting_price_range(self, target_price: int = 135):
        self.price_filter_actions(CatalogProductLocators.PRICE_FILTER_UP_TO,
                                  target_price,
                                  CatalogProductLocators.RIGHT_PRICE_FILTER_SLIDER)

    @allure.step("Наведение указателя на кнопку Применить фильтра по цене")
    def hovering_apply_price_button(self):
        self.go_to_element(CatalogProductLocators.BUTTON_APPLY_FILTER)

    @allure.step("Клик по кнопке Применить фильтра по цене")
    def click_apply_price_button(self):
        self.click_element(CatalogProductLocators.BUTTON_APPLY_FILTER)

    @allure.step("Выполнение проверки стоимости отфильтрованных товаров (не более 135 руб.)")
    def check_on_filtered_products(self, target_price: int):
        self.attach_screenshot(name="filtered_products")
        price_elements = self.find_elements_page(CatalogProductLocators.PRICE_DESERT)
        if not price_elements:
            raise AssertionError("После применения фильтра товары не найдены на странице!")

        for element in price_elements:
            raw_text = element
            current_price = int(raw_text.text[:3])

            if current_price > target_price:
                raise AssertionError(
                    f"Ошибка фильтрации! Найден товар с ценой {current_price} руб., "
                    f"что превышает лимит {target_price} руб. "
                    f"(Исходный текст элемента: '{raw_text}')"
                )

        logging.info(f"Успешно! Все {len(price_elements)} товаров имеют цену <= {target_price} руб.")
        assert len(price_elements) <= target_price

    @allure.step("Получить текущую стоимость корзины")
    def get_basket_cost_catalog(self) -> str:
        self.attach_screenshot(name="get_basket_cost_catalog")
        return self.wait_visible_element(HomePageLocators.BASKET_COST).text

    @allure.step("Наведение на кнопку 'В корзину' на странице каталога товаров")
    def hovering_add_to_cart_in_catalog(self):
        self.go_to_element(CatalogProductLocators.BUTTON_IN_CART)

    @allure.step("Клик по кнопке 'В корзину' на странице каталога товаров")
    def click_add_to_cart_in_catalog(self):
        self.click_element(CatalogProductLocators.BUTTON_IN_CART)
        time.sleep(1)

    @allure.step("Проверка того что открылась страница товаров Десерты")
    def verifying_menu_deserts_page_opened(self):
        text_url = "menu/deserts"
        self.attach_screenshot(name="page_menu_deserts_opened")
        current_url = self.extraction_url_contains(text_url)
        assert text_url in current_url, f"Ожидалось {text_url} в URL, но получили: {current_url}"
        logging.info(f"Page opened successfully. Current URL: {current_url}")
