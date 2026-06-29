import re
from src.actions.Skillbox.skillbox_filters import apply_skillbox_filters_and_get_results
from allure import suite, feature, step, title
import pytest_check as check
import logging


@suite("Тест сайта SkillBox")
@feature("Фильтрация курсов согласно выбранных критериев")
class TestSkillboxRU:
    @title("Фильтрация курсов по параметрам")
    def test_it_skillbox_ru(self, go_to_url, page, wait_element):
        logging.info("Запуск теста test_skillbox.py")
        with step("Открываем страницу в полноэкранном режиме"):
            page.set_viewport_size({"width": 1920, "height": 1080})

        with step("Выполняем переход на сайт https://skillbox.ru/code/"):
            go_to_url('https://skillbox.ru/code/')

        with step("Вызываем функцию для взаимодействия с элементами на странице"):
            profession_filter, duration_filter = apply_skillbox_filters_and_get_results(wait_element, page)

        for prof in profession_filter:
            criterion_1 = prof.inner_text()
            with step(f"Проверка типа курса: {criterion_1}"):
                check.equal(criterion_1, "Профессия")
        for duration in duration_filter:
            criterion_2 = duration.inner_text()
            with step(f"Проверка длительности: {criterion_2}"):
                assert re.search(r'\b([6-9]|1[0-2])\s+месяцев?\b', criterion_2, re.IGNORECASE)
        logging.info("Завершение теста test_skillbox.py")
