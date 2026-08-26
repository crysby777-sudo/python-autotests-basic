from faker import Faker
from random import randint

fake = Faker()

"""Функции генерации логина, email, пароля для регистрации нового пользователя"""


class UserDataGenerator:

    @staticmethod
    def get_fake_login():
        """Генерирует случайный логин на английском"""
        login = fake.pystr(min_chars=2, max_chars=20)  # min_chars- минимальное кол-во символов, max_chars- максимальное
        return login

    @staticmethod
    def get_fake_email():
        """Генерирует случайный валидный email"""
        email = fake.bothify(text="???????")  # "?"- кол-во символов до знака "@"
        return email + "@test.by"

    @staticmethod
    def get_fake_password():
        """Генерирует случайный валидный пароль"""
        password = fake.password(length=randint(5, 20))  # от "a" и до "b" кол-ва символов в пароле
        return password
