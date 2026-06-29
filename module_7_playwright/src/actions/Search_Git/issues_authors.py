from playwright.sync_api import Page
from allure import step, title
import logging


@title("Выполняем поиск нужных элементов на странице и вносим искомые данные")
def get_issue_authors_by_name(wait_element, page: Page, author_name):
    logging.info("Выполнение сценария на странице: поиск элементов и ввод данных")

    with step("Выбираем фильтр репозиториев по автору"):
        page.locator("//button[@aria-label='Filter by author']").click()

    with step(f"Вводим название автора '{author_name}'"):
        page.locator("//input[@aria-label='Filter authors']").fill(author_name)

    with step(f" Выполняем выбор отфильтрованного автора '{author_name}'"):
        page.locator(f"//span[text()='author:{author_name}']").click()
        wait_element(f"//a[contains(., '{author_name}')]")
        issue_author = page.locator(f"//a[contains(., '{author_name}')]").filter(has_text=author_name).all()
        logging.info(f"Найдено: записей на странице с автором '{author_name}'={len(issue_author)}")

    with step("Отправляем для проверки полученный результат"):
        logging.info("Передача данных для выполнения проверки")
        return issue_author
