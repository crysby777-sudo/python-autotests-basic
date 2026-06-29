from src.actions.Tooltip.tooltip_in_graphics import get_commit_activity_tooltip_data
from allure import suite, title, feature, step
import logging
from playwright.sync_api import Page


@feature("Страница статистики GitHub")
@suite("Тултип графика вклада в VS Code")
class TestGraph:
    @title("Проверка данных в тултипе графика вклада")
    def test_tooltip(self, go_to_url, page: Page, wait_element):
        logging.info("Запуск теста test_tooltip.py")
        with step("Выполняем переход на сайт https://github.com/microsoft/vscode/graphs/commit-activity"):
            go_to_url('https://github.com/microsoft/vscode/graphs/commit-activity')

        with step(" Вызываем функцию для взаимодействия с элементами на странице"):
            tooltip_text = get_commit_activity_tooltip_data(wait_element, page)

        core_content = ["3 Aug", "2025"]

        logging.info(f"Данные  из тултипа сравниваем с {core_content}")
        with step("Выполняем проверку данных полученных из тултипа"):
            for content in core_content:
                assert content in tooltip_text, f"В тултипе отсутствует '{content}': {tooltip_text}"
        logging.info("Завершение теста test_tooltip.py")
