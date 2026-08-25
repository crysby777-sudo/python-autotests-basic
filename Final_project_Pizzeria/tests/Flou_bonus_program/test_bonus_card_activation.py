import allure
from allure import step
from config.configuration import Config
from src.actions.pages.bonus_page import BonusProgramPage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Проверка активации карты бонусной программы")
class TestBonusCardActivation:
    @allure.title("Активация карты бонусной программы")
    def test_bonus_card_activation(self, open_url, selenium):
        """
        Шаги:
        1. Ввести в поля Имя и Телефон тестовые данные:
            Имя: Олег
            Телефон: +70012345678
        2. Нажать Оформить карту
        3. В появившемся окне (alert) нажать ОК
        4. Убедиться в наличии сообщения 'Ваша карта оформлена!'
        """
        bonus_page = BonusProgramPage(selenium)
        open_url(Config.BONUS_PROGRAM_URL)

        with step("Вводим в поля Имя и Телефон тестовые данные"):
            bonus_page.fill_form_name_and_phone(Config.NAME_BONUS, Config.PHONE_BONUS)

        with step("Нажимаем кнопку Оформить карту"):
            bonus_page.click_submit()

        with step("Проверяем наличие сообщения успешной активации карты"):
            bonus_page.check_success_card()
