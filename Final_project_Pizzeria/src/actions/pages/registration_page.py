import logging
import allure
from src.actions.helpers.data_generators_helpers import UserDataGenerator
from src.actions.pages.base_page import BasePage
from src.actions.locators.page_locators import RegistrationPageLocators, HomePageLocators, PersonalAccountLocators
from src.actions.pages.home_page import HomePage


"""Функции взаимодействия с элементами и проверки  на странице регистрации пользователя"""


class RegistrationPage(BasePage):

    @allure.step("Проверка что открылась страница Регистрации ")
    def checking_open_register_page(self):
        text_url = "register"
        self.attach_screenshot(name="Страница регистрации")
        current_url = self.extraction_url_contains(text_url)
        assert text_url in current_url, f"Ожидалось {text_url} в URL, но получили: {current_url}"
        logging.info(f"Page opened successfully. Current URL: {current_url}")

    @allure.step('Функция проверки, что ссылка "Войти" изменилась '
                 'на "Выйти" и присутствует сообщение "Регистрация завершена"')
    def checking_successful_registration(self):
        self.attach_screenshot(name="Успешная регистрация")
        button_authorized = self.wait_visible_element(HomePageLocators.BUTTON_AUTHORIZED).text
        message = self.wait_visible_element(RegistrationPageLocators.MESSAGE_REG_SUCCESS).text
        assert button_authorized == 'Выйти' and message == 'Регистрация завершена'

    @allure.step("Функция проверки совпадения логина и email введённых при регистрации"
                 " на странице Личного кабинета")
    def checking_matching_registration_data(self, value_login, value_email):
        self.attach_screenshot(name="Данные личного кабинета")
        login = self.wait_visible_element(PersonalAccountLocators.FIELD_NAME).get_attribute(
            "value"
        )
        email = self.wait_visible_element(PersonalAccountLocators.ADDRESS_EMAIL).get_attribute(
            "value"
        )
        logging.info(f"Personal account login: {login} ")
        logging.info(f"Email in the personal account: {email} ")
        assert login == value_login, email == value_email

    @allure.step("Наведение на поле ввода логина пользователя")
    def hover_input_field_user(self):
        self.go_to_element(RegistrationPageLocators.FIELD_USERNAME)

    @allure.step("Клик по полю ввода логина пользователя")
    def click_input_field_user(self):
        self.click_element(RegistrationPageLocators.FIELD_USERNAME)

    @allure.step("Наведение на поле ввода email пользователя")
    def hover_input_field_email(self):
        self.go_to_element(RegistrationPageLocators.FIELD_EMAIL)

    @allure.step("Клик по полю ввода email пользователя")
    def click_input_field_email(self):
        self.click_element(RegistrationPageLocators.FIELD_EMAIL)

    @allure.step("Наведение на поле ввода пароля пользователя")
    def hover_input_field_password(self):
        self.go_to_element(RegistrationPageLocators.FIELD_PASSWORD)

    @allure.step("Клик по полю ввода пароля пользователя")
    def click_input_field_password(self):
        self.click_element(RegistrationPageLocators.FIELD_PASSWORD)

    @allure.step("Ввод логина пользователя")
    def enter_user_login(self, value_login):
        self.fill_element(RegistrationPageLocators.FIELD_USERNAME, value_login)

    @allure.step("Ввод email пользователя")
    def enter_user_email(self, value_email):
        self.fill_element(RegistrationPageLocators.FIELD_EMAIL, value_email)

    @allure.step("Ввод пароля пользователя")
    def enter_user_password(self, value_password):
        self.fill_element(RegistrationPageLocators.FIELD_PASSWORD, value_password)

    @allure.step("Вызываем функцию генерации логина")
    def login_generation(self):
        logging.info("Launch of the login generation feature")
        random_login = UserDataGenerator.get_fake_login()
        logging.info(f"Registered user login: {random_login}")
        return random_login

    @allure.step("Вызываем функцию генерации email")
    def email_generation(self):
        logging.info("Launching the email generation function")
        random_email = UserDataGenerator.get_fake_email()
        logging.info(f"Registered user's email address: {random_email}")
        return random_email

    @allure.step("Вызываем функцию генерации пароля")
    def password_generation(self):
        logging.info("Launching the password generation function")
        random_password = UserDataGenerator.get_fake_password()
        logging.info(f"Registered user password: {random_password}")
        return random_password

    @allure.step("Функция наведения на кнопку Зарегистрироваться")
    def hover_button_register(self):
        self.go_to_element(RegistrationPageLocators.BUTTON_REGISTER)

    @allure.step("Функция клика по кнопке Зарегистрироваться")
    def click_button_register(self):
        self.click_element(RegistrationPageLocators.BUTTON_REGISTER)

    @allure.step("Функция наведения указателя на вкладку Данные аккаунта ")
    def hover_account_details(self):
        self.go_to_element(PersonalAccountLocators.ACCOUNT_INFO)

    @allure.step("Функция клика  указателя по вкладке Данные аккаунта ")
    def click_account_details(self):
        self.click_element(PersonalAccountLocators.ACCOUNT_INFO)

    @allure.step("Регистрация нового пользователя в системе с использованием "
                 "автоматически генерируемых тестовых данных")
    def register_new_user_generate(self, login=None, email=None, password=None):
        logging.info("Registration of a new user in the system using automatically generated test data")
        user_login = login or self.login_generation()
        user_email = email or self.email_generation()
        user_password = password or self.password_generation()

        self.hover_input_field_user()
        self.click_input_field_user()
        self.enter_user_login(user_login)

        self.hover_input_field_email()
        self.click_input_field_email()
        self.enter_user_email(user_email)

        self.hover_input_field_password()
        self.click_input_field_password()
        self.enter_user_password(user_password)

        self.hover_button_register()
        self.click_button_register()
        home = HomePage(self.driver)
        home.go_to_homepage()

        logging.info(f"logged in: {user_login}, email: {user_email}, password: {user_password}")
        return {"login": user_login, "email": user_email, "password": user_password}
