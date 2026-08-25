import time
from actions.pages.base_page import BasePage
from src.actions.locators.page_locators import BasketPageLocators
import logging
import allure


"""Функции взаимодействия с элементами и проверки  на странице Корзина"""


class BasketPage(BasePage):
    @allure.step("Проверка совпадения добавленной пиццы в корзине")
    def pizza_added_basket(self, name_added_pizza):
        name_pizza_in_basket = self.wait_visible_element(BasketPageLocators.LINK_TITLE_PRODUCT).text
        actual = self.normalize_text(name_added_pizza)
        expected = self.normalize_text(name_pizza_in_basket)
        logging.info(f" Name of the added pizza <{actual}>")
        logging.info(f" The pizza that is displayed in the cart <{expected}>")
        assert actual == expected

    @allure.step("Проверка соответствие выбранной доп опции 'борт' у добавленной пиццы в корзине")
    def pizza_basket_title_bort(self):
        additional_option = self.wait_visible_element(BasketPageLocators.ADDITIONAL_OPTION).text
        logging.info(f" The name of the side of the pizza in the basket <{additional_option}>")
        assert additional_option == 'Колбасный борт'

    @allure.step("Наведение указателя на окно добавления товаров в корзине")
    def hover_increase_in_quantity(self):
        self.go_to_element(BasketPageLocators.CHANGE_QUANTITY)

    @allure.step("Наведение указателя на кнопку 'ПЕРЕЙТИ К ОПЛАТЕ'")
    def hover_over_the_payment_button(self):
        self.go_to_element(BasketPageLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step("Клик по кнопке 'ПЕРЕЙТИ К ОПЛАТЕ'")
    def click_over_the_payment_button(self):
        self.click_element(BasketPageLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step("Увеличение количества товара в корзине")
    def added_products_on_the_cart_page(self):
        self.click_change_quantity_up(BasketPageLocators.CHANGE_QUANTITY)

    @allure.step("Наведение указателя на кнопку <Обновить корзину> ")
    def hover_button_update_cart(self):
        self.go_to_element(BasketPageLocators.UPDATE_CART)

    @allure.step("Сделать клик по кнопке <Обновить корзину> ")
    def click_button_update_cart(self):
        self.click_element(BasketPageLocators.UPDATE_CART)
        time.sleep(3)

    @allure.step("Получение общей суммы корзины")
    def total_amount_of_the_cart(self) -> str:
        self.attach_screenshot(name="total_amount_of_the_basket")
        total_sum = self.wait_visible_element(BasketPageLocators.TOTAL_AMOUNT).text
        logging.info(f" Total amount of the_cart = {total_sum}")
        return total_sum

    @allure.step("Выполнение проверки изменения общей стоимости корзины после"
                 " увеличения количества товара на одну позицию")
    def checking_adding_quantity(self, old_amount):
        self.attach_screenshot(name="checking_adding_quantity")
        new_amount = self.wait_visible_element(BasketPageLocators.TOTAL_AMOUNT).text
        old_amount = self.extract_price(old_amount)
        new_amount = self.extract_price(new_amount)
        logging.info(f" Initial basket amount = {old_amount}")
        logging.info(f" Final cart total = {new_amount}")
        assert new_amount == old_amount * 2

    @allure.step("Наведение на кнопку удаления (крестик) пиццы из корзины")
    def hovering_over_the_pizza_removal_button(self):
        self.go_to_element(BasketPageLocators.BUTTON_REMOVE)

    @allure.step("Клик по кнопке удаления (крестик) товара из корзины")
    def click_over_the_pizza_removal_button(self):
        self.click_element(BasketPageLocators.BUTTON_REMOVE)
        time.sleep(1)

    @allure.step("Проверка того, что появилось сообщение 'Корзина пуста'")
    def verifying_message_has_appeared(self):
        self.attach_screenshot(name="Cart is empty")
        message = self.wait_visible_element(BasketPageLocators.MESSAGE_CART_EMPTY).text
        logging.info(f"There is a message on the official page: {message}")
        assert 'Корзина пуста' in message

    @allure.step("Проверка присутствия кнопки 'ПЕРЕЙТИ К ОПЛАТЕ' на странице")
    def checking_button_PROCEED_TO_PAYMENT(self):
        self.attach_screenshot(name="button_PROCEED_TO_PAYMENT")
        assert self.wait_visible_element(BasketPageLocators.BUTTON_PLACE_AN_ORDER)
        logging.info("The button to proceed to payment is present on the page")

    @allure.step("Клик по кнопке 'ПЕРЕЙТИ К ОПЛАТЕ' на странице")
    def click_button_PROCEED_TO_PAYMENT(self):
        self.go_to_element(BasketPageLocators.BUTTON_PLACE_AN_ORDER)
        self.click_element(BasketPageLocators.BUTTON_PLACE_AN_ORDER)
        time.sleep(1)

    @allure.step("Сброс применения промокода,если он был применен ранее")
    def reset_coupon(self):
        logging.info("Removing an applied promo code from the cart")
        coupon = self.find_elements_page(BasketPageLocators.REMOVE_COUPON)
        if coupon:
            self.click_element(BasketPageLocators.REMOVE_COUPON)
            logging.info("Coupon successfully deactivated")
            time.sleep(3)
        else:
            logging.info("The coupon has not been used before.")
            return
