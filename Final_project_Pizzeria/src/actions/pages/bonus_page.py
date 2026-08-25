import logging
import time
from allure import step
from selenium.webdriver.common.keys import Keys
from src.actions.locators.page_locators import BonusProgramPageLocators
from src.actions.pages.base_page import BasePage


"""Функции взаимодействия с элементами и проверки  на странице оформления бонусной карты"""


class BonusProgramPage(BasePage):
    with step("Проверка что открылась страница бонусной программы"):
        def check_open_bonus_page(self):
            text_url = "bonus"
            self.attach_screenshot("bonus_program_page")
            current_url = self.extraction_url_contains(text_url)
            assert text_url in current_url, f"Ожидалось {text_url} в URL, но получили: {current_url}"
            logging.info(f"Page opened successfully. Current URL: {current_url}")

    with step("Проверка успешного оформления бонусной карты"):
        def check_success_card(self):
            self.attach_screenshot("success_card")
            message = self.get_element_text_if_visible(BonusProgramPageLocators.BONUS_CARD_SUCCESS)
            logging.info(f"The page contains the message {message}")
            assert message == 'Ваша карта оформлена!', f"На странице присутствует сообщение {message}"

    with step("Заполнение полей Имя и Телефон"):
        def fill_form_name_and_phone(self, name_value=True, phone_value=True):
            logging.info("Launching the function for filling in the Name and Phone fields")
            name_input = self.wait_visible_element(BonusProgramPageLocators.FIELD_NAME)
            phone_input = self.wait_visible_element(BonusProgramPageLocators.FIELD_PHONE)

            name_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
            if name_value is not None:
                name_input.send_keys(name_value)
                logging.info(f"The Name field is filled in {name_value}")

            phone_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
            if phone_value is not None:
                phone_input.send_keys(phone_value)
                logging.info(f"The Phone field is filled in {phone_value}")

    with step("Нажатие кнопки Оформить карту"):
        def click_submit(self):
            self.suppress_alerts()
            submit_button = self.wait_visible_element(BonusProgramPageLocators.BUTTON_APPLY_CART)
            submit_button.click()
            time.sleep(3)
            logging.info("The submit button is clicked")

    with step("Проверка результатов валидации полей формы бонусной программы"):
        def check_field_validation(self, is_valid_or_error, case_id: str):
            logging.info("Launching the function for checking the field validation")
            self.attach_screenshot("message_bonus_page")
            if case_id.startswith("valid") or is_valid_or_error is True:
                actual_error = self.get_element_text_if_visible(BonusProgramPageLocators.ERROR_MESSAGE)

                assert actual_error is None, (
                    f"Для валидного кейса [{case_id}] неожиданно появилась ошибка в DOM: '{actual_error}'"
                )
                logging.info("The check_field_validation finish")

            else:
                expected_error = is_valid_or_error
                actual_error = self.get_element_text_if_visible(BonusProgramPageLocators.ERROR_MESSAGE)
                assert actual_error == expected_error, (
                    f"Несовпадение ошибки для кейса [{case_id}]:\n"
                    f"Ожидали: '{expected_error}'\n"
                    f"Получили: '{actual_error}'"
                )
                logging.info(f"The field validation is successful: Received {actual_error}")
