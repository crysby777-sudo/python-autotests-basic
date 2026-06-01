from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure import step, title
import logging


@title("Выполняем поиск нужных полей и заполняем форму расширенного поиска")
def search_repos_and_get_star_elements(driver, language, stars, filename):
    logging.info("Переходим к заполнению формы расширенного поиска")

    with step(f" В поле 'Written in this language' выбираем '{language}' "):
        driver.find_element(By.XPATH, f"//select[@id='search_language']//option[@value='{language}']").click()

    with step(f" В поле 'With this many stars' вводим  '{stars}' "):
        driver.find_element(By.XPATH, "//*[@id='search_stars']").send_keys(stars)

    with step(f" В поле 'With this file name' вводим  '{filename}' "):
        driver.find_element(By.XPATH, "//*[@id='search_filename']").send_keys(filename)

    with step(" Нажинаем кнопку поиска"):
        driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]").click()

    with step("Ждем появления результатов"):
        wait = WebDriverWait(driver, 15)
        star_locator = (By.XPATH, "//a[contains(@aria-label, 'stars')]")
        wait.until(EC.presence_of_element_located(star_locator))

    with step("Возвращаем элементы с количеством звезд"):
        logging.info("Передача данных для выполнения проверки")
        return driver.find_elements(*star_locator)
