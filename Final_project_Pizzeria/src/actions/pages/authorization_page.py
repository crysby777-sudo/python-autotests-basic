import logging
import allure
from config.configuration import Config
from actions.pages.base_page import BasePage
from src.actions.locators.page_locators import AuthorizedPageLocators, PersonalAccountLocators

"""Функции взаимодействия с элементами и проверки  на странице Авторизация"""


class AuthorizationPage(BasePage):

    @allure.step("Функция наведения на кнопку Зарегистрироваться")
    def hover_register_button(self):
        self.go_to_element(AuthorizedPageLocators.BUTTON_REGISTRATION)

    @allure.step("Функция клика по кнопке Зарегистрироваться")
    def click_register_button(self):
        self.click_element(AuthorizedPageLocators.BUTTON_REGISTRATION)

    @allure.step("Функция наведения на поле Имя пользователя или почта")
    def hover_login_field(self):
        self.go_to_element(AuthorizedPageLocators.FIELD_USERNAME)

    @allure.step("Функция клика по полю Имя пользователя или почта")
    def click_login_field(self):
        self.click_element(AuthorizedPageLocators.FIELD_USERNAME)

    @allure.step("Функция ввода логина в поле Имя пользователя или почта")
    def fill_login_field(self):
        self.fill_element(AuthorizedPageLocators.FIELD_USERNAME, Config.TEST_USERNAME)
        logging.info(f"Username : {Config.TEST_USERNAME}")

    @allure.step("Функция наведения на поле Пароль")
    def hover_password_field(self):
        self.go_to_element(AuthorizedPageLocators.FIELD_PASSWORD)

    @allure.step("Функция клика по полю Пароль")
    def click_password_field(self):
        self.click_element(AuthorizedPageLocators.FIELD_PASSWORD)

    @allure.step("Функция ввода пароля в поле Пароль")
    def fill_password_field(self):
        self.fill_element(AuthorizedPageLocators.FIELD_PASSWORD, Config.TEST_PASSWORD)
        logging.info(f"Username : {Config.TEST_PASSWORD}")

    @allure.step("Функция наведения указателя на кнопку Войти в форме авторизации")
    def hover_button_log_in(self):
        self.go_to_element(AuthorizedPageLocators.BUTTON_AUTHORIZED)

    @allure.step("Функция клика указателем по кнопке Войти в форме авторизации")
    def click_button_log_in(self):
        self.click_element(AuthorizedPageLocators.BUTTON_AUTHORIZED)

    @allure.step('Функция проверки того, что появилось сообщение об успешной авторизации')
    def checking_user_authorization(self):
        self.attach_screenshot(name="Успешная авторизация")
        welcome_user = self.wait_visible_element(PersonalAccountLocators.WELCOME_USER).text
        logging.info(f"Successful login greeting message | Привет {Config.TEST_USERNAME} !")
        assert welcome_user == f"| Привет {Config.TEST_USERNAME} !"
