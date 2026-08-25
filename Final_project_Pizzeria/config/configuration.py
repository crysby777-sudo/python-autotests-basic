"""
Файл конфигурации для тестового проекта
Содержит URL, тайм-аут, тестовые данные
"""


class Config:
    #  === Базовые URL ===
    BASE_URL = "https://pizzeria.skillbox.cc/"  # Главная страница
    DESERT_URL = "https://pizzeria.skillbox.cc/product-category/menu/deserts/"  # Страница с десертами
    BASKET_URL = "https://pizzeria.skillbox.cc/cart/"  # Страница корзины
    CHECKOUT_URL = "https://pizzeria.skillbox.cc/checkout/"  # Страница с предложением авторизоваться
    PIZZA_URL = "https://pizzeria.skillbox.cc/product-category/menu/pizza/"  # Страница каталога товаров
    PRODUCT_CART_URL = "https://pizzeria.skillbox.cc/product/"  # Страница карточки товара
    REGISTRATION_URL = "https://pizzeria.skillbox.cc/register/"  # Страница регистрации нового пользователя
    AUTHORIZATION_URL = "https://pizzeria.skillbox.cc/my-account/"  # Страница авторизации
    BONUS_PROGRAM_URL = "https://pizzeria.skillbox.cc/bonus/"  # страница оформления карты бонусной программы

    # === Таймауты ===
    IMPLICIT_WAIT = 10

    # ===Тестовые данные===
    TEST_USERNAME = "olegtest"  # Имя пользователя
    TEST_PASSWORD = "12345"  # Пароль

    # ===Данные для заполнения полей===
    FIRST_NAME = "Олег"
    FAMILY_NAME = "Олегов"
    COUNTRY_BELARUS = "Belarus"
    ADDRESS = "ул. Минская 7-49"
    CITY = "Брест"
    REGION = "Брестская"
    INDEX_POST = "777777"
    NUMBER_TEL = "81234567890"
    EMAIL_USER = "olegtest@test.by"
    CORRECT_PROMOCOD = "GIVEMEHALYAVA"
    WRONG_PROMOCOD = "DC120"

    # Данные для оформления бонусной карты
    NAME_BONUS = "Олег"
    PHONE_BONUS = "+70012345678"
