import allure
from allure import step
import pytest
from config.configuration import Config
from Test_data.validation_data import ValidationField
from src.actions.pages.bonus_page import BonusProgramPage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Валидация полей формы активации бонусной карты (негативные сценарии)")
class TestFieldValidationNegative:
    @allure.title("Проверка валидации поля Имя при отправке формы (негативные сценарии")
    @pytest.mark.parametrize("case_id, name_input, phone_input,"
                             " expected_name_error",
                             ValidationField.NAME_FIELD_INVALID,
                             ids=[case[0] for case in ValidationField.NAME_FIELD_INVALID]
                             )
    def test_negative_name_fields_validation(self, open_url, selenium,
                                             case_id, name_input, phone_input,
                                             expected_name_error
                                             ):
        """
        Шаги:
             1. Вводим в поле Имя невалидные значения, в поле Телефон +79991234567
             2. Нажимаем кнопку: Оформить карту
             3. Выполняем проверку присутствия сообщения ошибки
        """
        open_url(Config.BONUS_PROGRAM_URL)
        page = BonusProgramPage(selenium)

        with step("Вводим в поле Телефон значения или оставляем пустым"):
            page.fill_form_name_and_phone(name_value=name_input, phone_value=phone_input)

        with step("Нажать Оформить карту"):
            page.click_submit()

        with step("Выполнить проверку валидации поля Имя"):
            page.check_field_validation(expected_name_error, case_id)

    @allure.title("Проверка валидации поля Телефон при отправке формы (негативные сценарии")
    @pytest.mark.parametrize("case_id, name_input, phone_input,"
                             " expected_phone_error",
                             ValidationField.PHONE_FIELD_INVALID,
                             ids=[case[0] for case in ValidationField.PHONE_FIELD_INVALID]
                             )
    def test_negative_phone_fields_validation(self, open_url, selenium,
                                              case_id, name_input, phone_input,
                                              expected_phone_error
                                              ):
        """
        Шаги:
            1. Вводим в поле Телефон невалидные значения, в поле Имя 'Олег'
            2. Нажимаем кнопку: Оформить карту
            3. Выполняем проверку присутствия сообщения ошибки
        """
        open_url(Config.BONUS_PROGRAM_URL)
        page = BonusProgramPage(selenium)

        with step("Вводим в поля значения Имя и Телефон "):
            page.fill_form_name_and_phone(name_value=name_input, phone_value=phone_input)

        with step("Нажать Оформить карту"):
            page.click_submit()

        with step("Выполнить проверку валидации поля Имя"):
            page.check_field_validation(expected_phone_error, case_id)

    @allure.title("Проверка валидации пустых полей Имя и Телефон при отправке формы (негативные сценарии")
    @pytest.mark.parametrize("case_id, name_input, phone_input,"
                             " expected_name_phone_error",
                             ValidationField.NAME_AND_PHONE_FIELD_EMPTY,
                             ids=[case[0] for case in ValidationField.NAME_AND_PHONE_FIELD_EMPTY]
                             )
    def test_name_and_phone_fields_empty(self, open_url, selenium,
                                         case_id, name_input, phone_input,
                                         expected_name_phone_error
                                         ):
        """
        Шаги:
            1. Поля Имя и Телефон оставляем пустыми
            2. Нажимаем кнопку: Оформить карту
            3. Выполняем проверку присутствия под полями сообщений ошибки
        """
        open_url(Config.BONUS_PROGRAM_URL)
        page = BonusProgramPage(selenium)

        with step("Нажать Оформить карту"):
            page.click_submit()

        with step("Выполнить проверку валидации поля Имя и Телефон"):
            page.check_field_validation(expected_name_phone_error, case_id)
