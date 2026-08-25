from selenium.webdriver.common.by import By


class HomePageLocators:
    """Локаторы для главной страницы сайта пиццерии"""

    # слайдер "Пицца"
    SLIDER_PIZZA = (By.XPATH, '//aside[@id="accesspress_store_product-5" and contains(., "Пицца")]')
    # слайдер "Десерты"
    SLIDER_DESERTS = (By.XPATH, '//aside[@id="accesspress_store_product-6" '
                                'and contains(., "Десерты")]')
    # слайдер "Напитки"
    SLIDER_DRINKS = (By.XPATH, '//aside[@id="accesspress_store_product-7" '
                               'and contains(., "Напитки")]')
    # правая кнопка прокрутки слайдера
    BUTTON_RIGHT = (By.XPATH, '//*[@aria-label="next"]')
    # левая кнопка прокрутки слайдера
    BUTTON_LEFT = (By.XPATH, '//*[@aria-label="previous"]')
    # 1-я пицца в слайдере
    IMAGE_PIZZA_1 = (By.XPATH, "//li[contains(@class, 'slick-active') "
                               "and contains(., 'Пицца')][1]")
    # 2-я пицца в слайдере
    IMAGE_PIZZA_2 = (By.XPATH, "//li[contains(@class, 'slick-active') "
                               "and contains(., 'Пицца')][2]")
    # 4-я пицца в слайдере
    IMAGE_PIZZA_4 = (By.XPATH, "//li[contains(@class, 'slick-active') "
                               "and contains(., 'Пицца')][4]")
    # 3-я пицца в слайдере
    IMAGE_PIZZA_3 = (By.XPATH, "//li[contains(@class, 'slick-active') "
                               "and contains(., 'Пицца')][3]")
    # 1-й десерт в слайдере
    IMAGE_DESERT_1 = (By.XPATH, "//li[contains(@class, 'slick-active') "
                                "and contains(., 'Десерт')][1]")
    # 1-й напиток в слайдере
    IMAGE_DRINK_1 = (By.XPATH, "//li[contains(@class, 'slick-active') "
                               "and contains(., 'Напиток')][1]")
    # иконка перехода в корзину
    BASKET_COST = (By.XPATH, '//div[@class="view-cart"]')
    # название 1-й пиццы в слайдере
    TITLE_PIZZA_IN_SLIDER_1 = (By.XPATH,
                               "//li[contains(@class, 'slick-active')][1]//h3[contains(text(), 'Пицца')]"
                               )
    # название 2-й пиццы в слайдере
    TITLE_PIZZA_IN_SLIDER_2 = (By.XPATH,
                               "//li[contains(@class, 'slick-active')][2]//h3[contains(text(), 'Пицца')]"
                               )
    # название 3-й пиццы в слайдере
    TITLE_PIZZA_IN_SLIDER_3 = (By.XPATH,
                               "//li[contains(@class, 'slick-active')][3]//h3[contains(text(), 'Пицца')]"
                               )
    # название 4-й пиццы в слайдере
    TITLE_PIZZA_IN_SLIDER_4 = (By.XPATH,
                               "//li[contains(@class, 'slick-active')][4]//h3[contains(text(), 'Пицца')]"
                               )
    # логотип Pizzeria
    BUTTON_LOGO = (By.XPATH, "//a[@class='site-logo']")
    # кнопка "Меню" в рубрикаторе
    PAGE_MENU = (By.XPATH, "//a[contains(text(), 'Меню')]")
    # выпадающее меню
    SUBMENU = (By.XPATH, "//ul[@class='sub-menu']")
    SUBMENU_DESERTS = (By.XPATH, "//a[contains(text(), 'Десерты')]")  # раздел "Десерты" в выпадающем меню
    BUTTON_MY_ACCOUNT = (By.XPATH, "(//a[contains(text(), 'Мой аккаунт')])[1]")
    # вкладка "Мой аккаунт" в рубрикаторе
    BUTTON_AUTHORIZED = (By.XPATH, "//div[@class='login-woocommerce']")  # кнопка "Войти"
    BUTTON_PLACING_ORDER = (By.ID, "menu-item-31")  # кнопка Оформить заказ в рубрикаторе
    BUTTON_BONUS_PROG = (By.ID, "menu-item-363")  # кнопка Бонусная программа в рубрикаторе
    # кнопка "В корзину" для 1-й пиццы в слайдере
    BUTTON_ADD_TO_PIZZA_1 = (By.XPATH, '(//li[contains(@class, "slick-active")])'
                                       '[1]//a[contains(text(), "В корзину")]'
                             )
    # кнопка "В корзину" для 2-й пиццы в слайдере
    BUTTON_ADD_TO_PIZZA_2 = (By.XPATH, '(//li[contains(@class, "slick-active")])[2]'
                                       '//a[contains(text(), "В корзину")]'
                             )
    # кнопка "В корзину" для 3-й пиццы в слайдере
    BUTTON_ADD_TO_PIZZA_3 = (By.XPATH, '(//li[contains(@class, "slick-active")])[3]'
                                       '//a[contains(text(), "В корзину")]'
                             )
    # кнопка "В корзину" для 4-й пиццы в слайдере
    BUTTON_ADD_TO_PIZZA_4 = (By.XPATH, '(//li[contains(@class, "slick-active")])[4]'
                                       '//a[contains(text(), "В корзину")]'
                             )
    # кнопка "В корзину" для 1-го напитка в слайдере
    BUTTON_ADD_TO_CART_DRINK = (By.XPATH, '//a[@data-product_id="431"]')
    # кнопка "В корзину" для 1-го десерта в слайдере
    BUTTON_ADD_TO_CART_DESERT = (By.XPATH, '//a[@data-product_id="437"]')


class PersonalAccountLocators:
    """Локаторы страницы Личный кабинет"""
    ACCOUNT_INFO = (By.XPATH, "//a[contains(text(), 'Данные аккаунта')]")  # вкладка данные аккаунта
    FIELD_NAME = (By.XPATH, "//input[@id='account_display_name']")  # поле отображаемое имя в данных учетной записи
    ADDRESS_EMAIL = (By.XPATH, "//input[@id='account_email']")  # адрес email в данных учетной записи
    WELCOME_USER = (By.XPATH, "//div[@class='welcome-user']")  # приветствие авторизованного пользователя


class AuthorizedPageLocators:
    """Локаторы страницы авторизации"""
    FIELD_USERNAME = (By.XPATH, "//input[@id='username']")  # поле ввода логина
    FIELD_PASSWORD = (By.XPATH, "//input[@id='password']")  # поле ввода пароля
    BUTTON_AUTHORIZED = (By.XPATH, "//button[@name='login']")  # кнопка авторизоваться
    BUTTON_REGISTRATION = (By.XPATH, "//button[contains(text(),"
                                     " 'Зарегистрироваться')]")  # кнопка Зарегистрироваться


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""

    FIELD_USERNAME = (By.XPATH, "//input[@id='reg_username']")  # поле ввода логина нового пользователя
    FIELD_EMAIL = (By.XPATH, "//input[@id='reg_email']")  # поле ввода email нового пользователя
    FIELD_PASSWORD = (By.XPATH, "//input[@id='reg_password']")  # поле ввода пароля нового пользователя
    BUTTON_REGISTER = (By.XPATH, "//button[@name='register']")  # кнопка Зарегистрироваться
    MESSAGE_REG_SUCCESS = (By.XPATH, "//div[@class='content-page']")  # сообщение об успешной регистрации


class BasketPageLocators:
    """Локаторы страницы Корзина"""

    BUTTON_PLACE_AN_ORDER = (By.XPATH, '//a[contains(text(), "ПЕРЕЙТИ К ОПЛАТЕ")]')  # кнопка перейти к оплате
    LINK_TITLE_PRODUCT = (By.XPATH, '//td[@class="product-name"]//a[contains(text(), "Пицца")]')  # название пиццы
    ADDITIONAL_OPTION = (By.XPATH, '//dd[@class="variation-"]')  # название доп опции пиццы
    CHANGE_QUANTITY = (By.XPATH, '//input[@type="number"]')  # количество пицц одной позиции
    UPDATE_CART = (By.XPATH, '//button[@name="update_cart"]')  # кнопка обновить корзину
    TOTAL_AMOUNT = (By.XPATH, '//td[@data-title="Сумма"]//bdi')  # общая сумма корзины
    BUTTON_REMOVE = (By.XPATH, '//a[@aria-label="Remove this item"]')  # Кнопка удаления товара из корзины
    MESSAGE_CART_EMPTY = (By.XPATH,
                          '//p[@class="cart-empty woocommerce-info"]')  # сообщения при удалении из корзины товара
    REMOVE_COUPON = (By.XPATH, '//a[contains(@class,"coupon")]')  # ссылка Удалить применённый купон


class CardProductLocators:
    """Локаторы страницы Карточка товара"""

    TITLE_CARD_PRODUCT = (By.XPATH, '//h1[@class="product_title entry-title"]')  # название товара
    SELECT_BORT = (By.XPATH, '//select')  # селектор выбора доп опции борта
    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@name = "add-to-cart"]')  # кнопка добавления товара в корзину
    PRICE_PIZZA = (By.XPATH, '//div[@class="summary entry-summary"]//bdi')  # цена товара


class CatalogProductLocators:
    """Локаторы страницы каталога товаров"""

    # правая кнопка регулировки фильтра по цене
    RIGHT_PRICE_FILTER_SLIDER = (By.XPATH, '//span[contains(@class, "ui-slider-handle ui")][2]')
    BUTTON_APPLY_FILTER = (By.XPATH, '//button[contains(text(), "Применить")]')  # кнопка Применить фильтра по цене
    PRICE_DESERT = (By.XPATH, '//span[@class="price"]/span[contains(@class, "amount")]//bdi')  # цена товара в каталоге
    PRICE_FILTER_UP_TO = (By.XPATH, '//span[@class="to"]')  # Максимальная цена в фильтре
    BUTTON_IN_CART = (By.XPATH, "//a[contains(text(), 'В корзину')]")  # Кнопка 'В корзину'


class CheckoutLocators:
    """Локаторы страницы предложения авторизации"""

    LINK_AUTHORIZATION = (By.XPATH, '//a[@class="showlogin"]')  # ссылка на предложение Авторизации
    LINK_COUPON = (By.XPATH, '//a[@class="showcoupon"]')  # ссылка для ввода купона


class OrderPageLocators:
    """Локаторы страницы оформления заказа"""

    FIRST_NAME = (By.XPATH, "//input[@autocomplete='given-name']")  # поле ИМЯ
    FAMILY_NAME = (By.XPATH, "//input[@autocomplete='family-name']")  # поле Фамилия
    COUNTRY = (By.XPATH, "//span[@class='selection']")  # поле Страна
    COUNTRY_FIELD = (By.XPATH, "//input[@class='select2-search__field']")  # поле ввода страны
    ADDRESS = (By.XPATH, "//input[@autocomplete='address-line1']")  # поле Адрес
    CITY = (By.XPATH, "//input[@autocomplete='address-level2']")  # поле Город
    REGION = (By.XPATH, "//input[@autocomplete='address-level1']")  # поле Область
    INDEX_POST = (By.XPATH, "//input[@autocomplete='postal-code']")  # поле Индекс почты
    NUMBER_TEL = (By.XPATH, "//input[@autocomplete='tel']")  # поле Номер телефона
    INPUT_DATA = (By.XPATH, '//input[@name="order_date"]')  # поле ввода даты
    PAYMENT_UPON_DELIVERY = (By.XPATH, "//input[@value='cod']")  # радио баттон оплата при получении
    TITLE_PAYMENT = (By.XPATH, '//label[@for="payment_method_cod"]')  # название способа оплаты Оплата при доставке
    CHECKBOX_CONSENT = (By.XPATH, "//input[@name='terms']")  # чекбокс I have read and agree to the website
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[@id='place_order']")  # кнопка Оформить заказ
    TOTAL_COST = (By.XPATH, '//tr[@class="cart-subtotal"]//bdi')  # общая стоимость заказа (до применения промокода)
    TOTAL_ORDER = (By.XPATH, "//tr[@class='order-total']//bdi")  # сумма заказа
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")  # оле email пользователя
    LINK_PROMOCOD = (By.XPATH, '//a[@class="showcoupon"]')  # ссылка для активации окна ввода промокода
    PROMOCOD_FIELD = (By.XPATH, '//input[@name="coupon_code"]')  # поле ввода промокода
    APPLY_PROMOCOD = (By.XPATH, '//button[@name="apply_coupon"]')  # кнопка Применить купон
    ERROR_COUPON = (By.XPATH, '//ul[@role="alert"]/li')  # сообщение Неверный купон


class OrderConfirmationPageLocators:
    """Локаторы страницы подтверждения заказа"""
    POST_TITLE = (By.XPATH, '//h2[@class="post-title"]')  # сообщение Заказ получен
    TOTAL = (By.XPATH, '//li//span[contains(@class, "amount")]/bdi')  # общая сумма заказа
    EMAIL = (By.XPATH, '//li[contains(@class, "email")]/strong')  # email пользователя
    PAYMENT_METHOD = (By.XPATH, '//li[contains(@class, "method")]/strong')  # метод оплаты
    DATA = (By.XPATH, '//li[contains(@class, "date")]/strong')  # дата заказа


class BonusProgramPageLocators:
    """Локаторы страницы активации бонусной программы"""
    POST_TITLE = (By.XPATH, '//h2[@class="post-title"]')  # заголовок страницы Бонусной программы
    FIELD_NAME = (By.XPATH, '//input[@id="bonus_username"]')  # поле ввода Имя
    FIELD_PHONE = (By.XPATH, '//input[@id="bonus_phone"]')  # поле ввода Телефон
    BUTTON_APPLY_CART = (By.XPATH, '//button[@name="bonus"]')  # кнопка Оформить карту
    BONUS_CARD_SUCCESS = (By.XPATH, '//div[@id="bonus_main"]/h3')  # сообщение Ваша карта оформлена!
    ERROR_MESSAGE = (By.XPATH, '//div[@id="bonus_content"]')  # сообщение ошибки валидации полей
