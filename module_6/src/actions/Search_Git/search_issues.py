from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step, title
import logging


@title("Выполняем поиск нужных элементов на странице и вносим искомые данные")
def search_issues_and_get_matches(selenium,
                                  keyword,
                                  search_query):
    logging.info("Выполнение сценария на странице: поиск элементов и ввод данных")

    with step(f"Открываем поиск и вводим ключевое слово '{keyword}'"):
        selenium.find_element(By.CSS_SELECTOR, 'button[aria-label*="Search"]').click()
        selenium.find_element(By.CSS_SELECTOR, '#query-builder-test').send_keys(search_query + Keys.ENTER)

    with step("Ждем появления результатов поиска"):
        wait = WebDriverWait(selenium, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'search-match')]")))

    with step(f"Ищем элементы с ключевым словом '{keyword}'"):
        xpath = (f"//span[contains(@class, 'search-match')]//em[contains(translate"
                 f"(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{keyword}')]")

    key_word = selenium.find_elements(By.XPATH, xpath)

    with step("Отправляем найденные названия задач для проверки"):
        logging.info(f"Передача {key_word} для выполнения проверки")
        return key_word
