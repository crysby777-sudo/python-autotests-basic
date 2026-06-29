from allure import title, step
import logging


@title("Поиск элементов и применение фильтров на странице")
def apply_skillbox_filters_and_get_results(wait_element, page):
    with step("Открываем страницу в полноэкранном режиме"):
        page.set_viewport_size({"width": 1920, "height": 1080})

    logging.info("Поиск элементов и применение фильтров на странице")

    with step("Поиск и нажатие кнопки «Профессия»"):
        wait_element("//button/span[contains(., 'Профессия')]").click()

    with step("Поиск и нажатие кнопки 'Длительность'"):
        wait_element("//button//span[contains(., 'Длительность')]").click()

    with step("Поиск и выбор в меню 'Длительность' значения 'От 6 до 12 мес.'"):
        wait_element( "//ul/li[contains(text(), 'От 6 до 12 мес.')]").click()

    with step("Поиск и нажатие кнопки 'Тематика'"):
        wait_element("(//button[@aria-label='Открыть список'])[3]").click()

    with step("Поиск и выбор в меню 'Тематика' значения 'Тестирование'"):
        wait_element("//li[contains(text(), 'Тестирование')]").click()

    with step("Поиск и нажатие кнопки 'Применить' в меню 'Тематика'"):
        wait_element("//button[contains(text(), 'Применить')]").click()

    with step("Ожидание и поиск отфильтрованных профессий"):
        wait_element("//span[contains(@class, 'programs-filtered')]")

    with step("Поиск в отфильтрованных элементах значения 'Профессия'"):
        profession_filter = page.locator("//span[contains(@class, 'product')]"
                                                   "[normalize-space() = 'Профессия']").all()

    with step("Поиск в отфильтрованных элементах значения 'Продолжительность'"):
        duration_filter = page.locator("//li[contains(@class , 'product-card')"
                                                 " and contains(., 'месяцев')]").all()
    with step("Возвращаем значения для проверки"):
        logging.info("Возвращаем значения для проверки")
    return profession_filter, duration_filter
