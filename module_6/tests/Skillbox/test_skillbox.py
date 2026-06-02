import re
import time
from src.actions.Skillbox.skillbox_filters import apply_skillbox_filters_and_get_results
from allure import suite, feature, step, title
import pytest_check as check
import logging


@suite("Тест сайта SkillBox")
@feature("Фильтрация курсов согласно выбранных критериев")
class TestSkillboxRU:
    @title("Фильтрация курсов по параметрам")
    def test_it_skillbox_ru(self, selenium):
        logging.info("Запуск теста test_skillbox.py")
        with step(" Выполняем переход на сайт https://skillbox.ru/code/"):
            selenium.get('https://skillbox.ru/code/')
        with step("Устанавливаем полноэкранный режим браузера"):
            selenium.maximize_window()
            time.sleep(3)

        with step("Вызываем функцию для взаимодействия с элементами на странице"):
            profession_filter, duration_filter = apply_skillbox_filters_and_get_results(selenium)
        logging.info("Проверяем полученный результат")
        with step("Проверяем полученный результат"):
            for prof in profession_filter:
                criterion_1 = prof.text
                with step(f"Соответствие критерию {criterion_1} в отфильтрованных курсах"):
                    check.equal(criterion_1, "Профессия")
            for duration in duration_filter:
                criterion_2 = duration.text
                with step(f"Соответствие критерию {criterion_2} в отфильтрованных курсах"):
                    assert re.search(r'\b(1[0-2]|[6-9])\s+месяцев?\b', criterion_2, re.IGNORECASE)
            logging.info("Завершение теста test_skillbox.py")
