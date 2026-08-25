import allure
from allure import step
import pytest
from config.configuration import Config
from Test_data.validation_data import ValidationField
from src.actions.pages.bonus_page import BonusProgramPage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Валидация полей формы активации бонусной карты (позитивные сценарии)")
class TestFieldValidationPositive:

    @allure.title("Проверка валидации поля Имя при отправке формы (позитивные сценарии")
    @pytest.mark.parametrize(
        "case_id, name_input, phone_input, expected_name_error",
        ValidationField.NAME_FIELD_VALID,
        ids=[case[0] for case in ValidationField.NAME_FIELD_VALID]
        )
    def test_positive_name_fields_validation(
                                            self, open_url, selenium,
                                            case_id, name_input, phone_input,
                                            expected_name_error
    ):
        """
        Шаги:
             1. Вводим в поле Имя валидные значения, в поле Телефон +79991234567
             2. Нажимаем кнопку: Оформить карту
             3. Выполняем проверку сообщения успешной регистрации карты
        """
        open_url(Config.BONUS_PROGRAM_URL)
        page = BonusProgramPage(selenium)

        with step("Вводим в поля значения Имя и Телефон "):
            page.fill_form_name_and_phone(name_value=name_input, phone_value=phone_input)

        with step("Нажать Оформить карту"):
            page.click_submit()

        with step("Выполнить проверку валидации поля Имя"):
            page.check_field_validation(expected_name_error, case_id)

    @allure.title("Проверка валидации поля Телефон при отправке формы (позитивные сценарии")
    @pytest.mark.parametrize(
                            "case_id, name_input, phone_input,"
                            " expected_phone_error",
                            ValidationField.PHONE_FIELD_VALID,
                            ids=[case[0] for case in ValidationField.PHONE_FIELD_VALID]
    )
    def test_positive_phone_fields_validation(
                                              self, open_url, selenium,
                                              case_id, name_input, phone_input,
                                              expected_phone_error
    ):
        """
        Шаги:
            1. Вводим в поле Телефон валидные значения, в поле Имя 'Олег'
            2. Нажимаем кнопку: Оформить карту
            3. Выполняем проверку сообщения успешной регистрации карты
        """
        open_url(Config.BONUS_PROGRAM_URL)
        page = BonusProgramPage(selenium)

        with step("Вводим в поле Телефон значения"):
            page.fill_form_name_and_phone(name_value=name_input, phone_value=phone_input)

        with step("Нажать Оформить карту"):
            page.click_submit()

        with step("Выполнить проверку валидации поля Имя"):
            page.check_field_validation(expected_phone_error, case_id)
