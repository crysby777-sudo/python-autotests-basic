import time
import allure
from allure import step
from src.actions.locators import HomePageLocators
from config.configuration import Config
from src.actions.pages.bonus_page import BonusProgramPage
from src.actions.pages.home_page import HomePage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Проверка перехода на страницу оформления карты бонусной программы")
class TestOpenBonusProgramPage:

    @allure.title("Проверка перехода  к странице оформления карты бонусной программы с главной страницы")
    def test_open_bonus_program_page(self, open_url, selenium):
        """
        Шаги:
        1. Открыть главную страницу сайта
        2. Перейти к рубрикатору и нажать раздел Бонусная программа
        3. Проверить что открылась страница оформления карты бонусной программы
        """
        home_page = HomePage(selenium)
        bonus_page = BonusProgramPage(selenium)
        open_url(Config.BASE_URL)

        with step("Переходим к главному рубрикатору страницы и нажимаем Бонусная программа"):
            home_page.click_element(HomePageLocators.BUTTON_BONUS_PROG)
            time.sleep(1)
        with step("Выполняем проверку что открылась страница Бонусной программы"):
            bonus_page.check_open_bonus_page()
