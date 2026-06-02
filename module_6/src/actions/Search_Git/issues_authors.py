from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step, title
import logging


@title("Выполняем поиск нужных элементов на странице и вносим искомые данные")
def get_issue_authors_by_name(selenium, author_name):
    logging.info("Выполнение сценария на странице: поиск элементов и ввод данных")

    with step("Выбираем фильтр репозиториев по автору"):
        selenium.find_element(By.XPATH, "//button[@aria-label='Filter by author']").click()

    with step("Ждем появления элемента на странице"):
        wait = WebDriverWait(selenium, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Filter authors']")))

    with step(f"Вводим название автора '{author_name}'"):
        selenium.find_element(By.XPATH, "//input[@aria-label='Filter authors']").send_keys(author_name)

    with step(f" Ожидаем появление имени автора '{author_name}'"):
        wait.until(EC.presence_of_element_located((By.XPATH, f"//span[contains(., 'author:{author_name}')]")))

    with step(f" Выполняем выбор отфильтрованного автора '{author_name}'"):
        selenium.find_element(By.XPATH, f"//span[contains(., 'author:{author_name}')]").click()

    with step("Ждём загрузки отфильтрованных задач"):
        wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(., '{author_name}')]")))

    issue_author = selenium.find_elements(By.XPATH, f"//a[contains(., '{author_name}')]")

    with step("Отправляем для проверки полученный результат"):
        logging.info("Передача данных для выполнения проверки")
        return issue_author
