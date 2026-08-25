import allure
from allure import step
from config import Config
from src.actions.pages.home_page import HomePage
from src.actions.pages.registration_page import RegistrationPage
from src.actions.pages.authorization_page import AuthorizationPage


@allure.epic("Финальная работа по курсу «Автотесты на Python")
@allure.feature("Тестирование функционала сайта Pizzeria")
@allure.story("Регистрация и авторизация")
class TestRegistrationAuthorization:

    @allure.title("Переход к регистрации через «Мой аккаунт»")
    def test_registration_through_my_account(self, selenium, open_url):
        """
        Шаги:
        1. Навести курсор на вкладку "Мой аккаунт"
        2. Сделать клик по вкладке "Мой аккаунт"
        3. Навести курсор на кнопку "Зарегистрироваться"
        4. Сделать клик по кнопке "Зарегистрироваться"
        5. Проверка того, что открылась страница Регистрации
        """
        open_url(Config.BASE_URL)

        home_page = HomePage(selenium)
        authorized_page = AuthorizationPage(selenium)
        register_page = RegistrationPage(selenium)

        with step("Проверяем что пользователь не авторизован, если авторизован выполняем выход из аккаунта"):
            home_page.logout_else_authorized()

        with step('Навести курсор в рубрикаторе страницы на вкладку "Мой аккаунт" '):
            home_page.hover_my_account_tab()

        with step('Сделать клик по вкладке "Мой аккаунт"'):
            home_page.click_my_account_tab()

        with step('Навести курсор на кнопку "Зарегистрироваться"'):
            authorized_page.hover_register_button()

        with step('Сделать клик по кнопке "Зарегистрироваться"'):
            authorized_page.click_register_button()

        with step('Выполнить проверку что открылась страница Регистрации'):
            register_page.checking_open_register_page()

    @allure.title("Регистрация пользователя")
    def test_user_registration(self, selenium, open_url):
        """
        Предусловие: открыта страница регистрации нового пользователя

        Шаги:
        1. Навести курсор на поле "Имя пользователя"
        2. Сделать клик по полю "Имя пользователя"
        3. Ввести в поле "Имя пользователя" валидное значение
        4. Навести курсор на поле "Адрес почты"
        5. Сделать клик по полю "Адрес почты"
        6. Ввести в поле "Адрес почты" валидный email
        7. Навести курсор на поле "Пароль"
        8. Сделать клик по полю "Пароль"
        9. Ввести в поле "Пароль" валидный пароль
        10. Навести курсор на кнопку "Зарегистрироваться"
        11. Сделать клик по кнопке "Зарегистрироваться"
        12. Проверка того, что ссылка "Войти" изменилась на "Выйти"
        """
        open_url(Config.REGISTRATION_URL)
        home_page = HomePage(selenium)
        register_page = RegistrationPage(selenium)

        with step("Проверяем что пользователь не авторизован, если авторизован выполняем выход из аккаунта"):
            home_page.logout_else_authorized()

        with step('Навести курсор на поле "Имя пользователя"'):
            register_page.hover_input_field_user()

        with step('Сделать клик по полю "Имя пользователя"'):
            register_page.click_input_field_user()

        with step('Ввести в поле "Имя пользователя" валидное значение'):
            random_login = register_page.login_generation()
            register_page.enter_user_login(random_login)

        with step('Навести курсор на поле "Адрес почты"'):
            register_page.hover_input_field_email()

        with step('Сделать клик по полю "Адрес почты"'):
            register_page.click_input_field_email()

        with step('Ввести в поле "Адрес почты" валидное значение'):
            random_email = register_page.email_generation()
            register_page.enter_user_email(random_email)

        with step('Навести курсор на поле "Пароль"'):
            register_page.hover_input_field_password()

        with step('Сделать клик по полю "Пароль"'):
            register_page.click_input_field_password()

        with step('Ввести в поле "Пароль" валидное значение'):
            random_password = register_page.password_generation()
            register_page.enter_user_password(random_password)

        with step('Навести курсор на кнопку "Зарегистрироваться"'):
            register_page.hover_button_register()

        with step('Сделать клик по кнопке "Зарегистрироваться"'):
            register_page.click_button_register()

        with step('Выполняем проверку успешной регистрации'):
            register_page.checking_successful_registration()

    @allure.title("Проверка успешной авторизации после регистрации")
    def test_verification_after_registration(self, selenium, open_url):
        """
        Предусловие: открыта страница регистрации нового пользователя
        Шаги:
        1. Навести курсор на поле "Имя пользователя"
        2. Сделать клик по полю "Имя пользователя"
        3. Ввести в поле "Имя пользователя" валидное значение на кириллице
        4. Навести курсор на поле "Адрес почты"
        5. Сделать клик по полю "Адрес почты"
        6. Ввести в поле "Адрес почты" валидный email
        7. Навести курсор на поле "Пароль"
        8. Сделать клик по полю "Пароль"
        9. Ввести в поле "Пароль" валидный пароль
        10. Навести курсор на кнопку "Зарегистрироваться"
        11. Сделать клик по кнопке "Зарегистрироваться"
        12. Навести курсор на вкладку "Мой аккаунт"
        13. Сделать клик по вкладке "Мой аккаунт"
        14. Навести курсор на вкладку "Данные аккаунта"
        15. Сделать клик по вкладке "Данные аккаунта"
        16. Проверка того, что введённые данные отображаются корректно
        """
        open_url(Config.REGISTRATION_URL)
        home_page = HomePage(selenium)
        register_page = RegistrationPage(selenium)

        with step("Проверяем что пользователь не авторизован, если авторизован выполняем выход из аккаунта"):
            home_page.logout_else_authorized()

        with step('Навести курсор на поле "Имя пользователя"'):
            register_page.hover_input_field_user()

        with step('Сделать клик по полю "Имя пользователя"'):
            register_page.click_input_field_user()

        with step('Ввести в поле "Имя пользователя" валидное значение'):
            random_login = register_page.login_generation()
            register_page.enter_user_login(random_login)

        with step('Навести курсор на поле "Адрес почты"'):
            register_page.hover_input_field_email()

        with step('Сделать клик по полю "Адрес почты"'):
            register_page.click_input_field_email()

        with step('Ввести в поле "Адрес почты" валидное значение'):
            random_email = register_page.email_generation()
            register_page.enter_user_email(random_email)

        with step('Навести курсор на поле "Пароль"'):
            register_page.hover_input_field_password()

        with step('Сделать клик по полю "Пароль"'):
            register_page.click_input_field_password()

        with step('Ввести в поле "Пароль" валидное значение'):
            random_password = register_page.password_generation()
            register_page.enter_user_password(random_password)

        with step('Навести курсор на кнопку "Зарегистрироваться"'):
            register_page.hover_button_register()

        with step('Сделать клик по кнопке "Зарегистрироваться"'):
            register_page.click_button_register()

        with step('Навести курсор в рубрикаторе страницы на вкладку "Мой аккаунт" '):
            home_page.hover_my_account_tab()

        with step('Сделать клик по вкладке "Мой аккаунт"'):
            home_page.click_my_account_tab()

        with step('Навести курсор на вкладку "Данные аккаунта"'):
            register_page.hover_account_details()

        with step('Сделать клик по вкладке "Мой аккаунт"'):
            register_page.click_account_details()

        with step('Проверка того, что введённые данные отображаются корректно'):
            register_page.checking_matching_registration_data(random_login, random_email)

    @allure.title('Авторизация пользователя через кнопку "Войти"')
    def test_authorization_through_login_button(self, selenium, open_url):
        """
        Шаги:
        1. Навести курсор на ссылку "Войти"
        2. Сделать клик по ссылке "Войти"
        3. Навести курсор на поле "Имя пользователя или почта"
        4. Сделать клик по полю "Имя пользователя или почта"
        5. Ввести в поле "Имя пользователя или почта" существующие данные
        6. Навести курсор на поле "Пароль"
        7. Сделать клик по полю "Пароль"
        8. Ввести в поле "Пароль" пароль от аккаунта
        9. Навести курсор на кнопку "Войти"
        10. Сделать клик по кнопке "Войти"
        11. Проверка того, что появилось сообщение об успешной авторизации
        """

        open_url(Config.BASE_URL)
        home_page = HomePage(selenium)
        authorization_page = AuthorizationPage(selenium)
        home_page.logout_else_authorized()

        with step('Навести курсор на ссылку "Войти"'):
            home_page.hover_authorization_button()

        with step('Сделать клик по ссылке "Войти"'):
            home_page.click_authorization_button()

        with step('Навести курсор на поле "Имя пользователя или почта"'):
            authorization_page.hover_login_field()

        with step('Сделать клик по полю "Имя пользователя или почта"'):
            authorization_page.click_login_field()

        with step('Ввести в поле "Имя пользователя или почта" существующие данные'):
            authorization_page.fill_login_field()

        with step('Навести курсор на поле "Пароль"'):
            authorization_page.hover_password_field()

        with step('Сделать клик по полю "Пароль"'):
            authorization_page.click_password_field()

        with step('Ввести в поле "Пароль" пароль от аккаунта'):
            authorization_page.fill_password_field()

        with step('Навести курсор на кнопку "Войти"'):
            authorization_page.hover_button_log_in()

        with step('Сделать клик по кнопке "Войти"'):
            authorization_page.click_button_log_in()

        with step('Проверка успешной авторизации'):
            authorization_page.checking_user_authorization()
