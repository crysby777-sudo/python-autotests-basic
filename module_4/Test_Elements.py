from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class TestInput:
    def test_search_field(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label*="Search"]').click()
        driver.find_element(By.CSS_SELECTOR, '#query-builder-test').send_keys('in:title bug'+ Keys.ENTER)
        pass

class TestAuthor:
    def test_button_Author(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, "//button[contains(., 'Author')]").click()
        driver.find_element(By.XPATH, "//*[@aria-label='Filter authors']").send_keys('bpasero')
        driver.find_element(By.XPATH, "//*[contains(text(), 'bpasero')]").click()
        pass

class TestRepoPython:
    def test_repo_python(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        driver.find_element(By.XPATH, "//select[@id='search_language']//option[@value='Python']").click()
        driver.find_element(By.XPATH, "//*[@id='search_stars']").send_keys('>20000')
        driver.find_element(By.XPATH, "//*[@id='search_filename']").send_keys('environment.yml')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]").click()
        pass


class TestSkillboxRU:
    def test_it_skillbox_ru(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru/code/')
        driver.find_element(By.XPATH, "//button/span[contains(., 'Профессия')]").click()
        driver.find_element(By.XPATH, "//button//span[contains(., 'Длительность')]").click()
        driver.find_element(By.XPATH, "//ul/li[contains(text(), 'От 6 до 12 мес.')]").click()
        driver.find_element(By.XPATH, "(//button[@aria-label= 'Открыть список'])[3]").click()
        driver.find_element(By.XPATH, "//li[contains(text(), 'Тестирование')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Применить')]").click()
        pass

class TestGraph:
    def test_tooltip(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(driver)
        time.sleep(3)
        action_chains.move_to_element(driver.find_element\
            (By.XPATH, "//*[@aria-label='Sunday,  3 Aug 2025, 435. Commits.']")).perform()
        pass
