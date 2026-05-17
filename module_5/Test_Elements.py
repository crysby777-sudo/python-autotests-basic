from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.common.action_chains import ActionChains



class TestSearch:
    def test_search_field(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label*="Search"]').click()
        driver.find_element(By.CSS_SELECTOR, '#query-builder-test').send_keys('in:title copilot' + Keys.ENTER)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'search-match')]")))
        key_word = driver.find_elements(By.XPATH, "//span[contains(@class, 'search-match')]//em[contains(translate\
            (., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',\
            'abcdefghijklmnopqrstuvwxyz'), 'copilot')]")

        for issue in key_word:
            title = issue.text
            assert re.search(r'\bcopilot\b', title, re.IGNORECASE)

        pass


class TestAuthor:
    def test_button_Author(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, "//button[@aria-label='Filter by author']").click()
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Filter authors']")))
        driver.find_element(By.XPATH, "//input[@aria-label='Filter authors']").send_keys('bpasero')
        driver.find_element(By.XPATH, "//span[contains(., 'author:bpasero')]").click()
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,  'bpasero')]")))
        issue_author = driver.find_elements(By.XPATH, "//a[contains(.,  'bpasero')]")

        for nickname in issue_author:
            author = nickname.text
            assert 'bpasero' in author
        pass


class TestRepoStars:
    def test_repo_stars(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        driver.find_element(By.XPATH, "//select[@id='search_language']//option[@value='Python']").click()
        driver.find_element(By.XPATH, "//*[@id='search_stars']").send_keys('>20000')
        driver.find_element(By.XPATH, "//*[@id='search_filename']").send_keys('environment.yml')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]").click()
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@aria-label, 'stars')]")))
        star_elem = driver.find_elements(By.XPATH, "//a[contains(@aria-label, 'stars')]")

        for element in star_elem:
            aria = element.get_attribute('aria-label')
            digits = re.findall(r'\d+', aria, re.IGNORECASE)
            stars = int(digits[0])
            assert stars > 20000
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

        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'programs-filtered')]")))
        profession_filter = driver.find_elements(By.XPATH, "//span[contains(@class, 'product')]\
                           [normalize-space() = 'Профессия']")
        duration_filter = driver.find_elements(By.XPATH, "//li[contains(@class , 'product-card')\
                            and contains(., 'месяцев')]")

        for prof in profession_filter:
            criterion_1 = prof.text
            assert 'Профессия' in criterion_1
        for duration in duration_filter:
            criterion_2 = duration.text
            assert re.search(r'\b(1[0-2]|[6-9])\s+месяцев?\b', criterion_2, re.IGNORECASE)
        pass


class TestGraph:
    def test_tooltip(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        wait = WebDriverWait(driver, 15)
        column = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@aria-label= 'Sunday,  3 Aug 2025, 455. Commits.']")))

        ActionChains(driver).move_to_element(column).perform()
        wait.until(lambda d: 'highcharts-point-hover' in column.get_attribute("class"))
        column_data = column.get_attribute("aria-label")
        tooltip_text = driver.find_element(By.XPATH, "//div[contains(@class,'highcharts-tooltip')]//table/tbody").text

        core_content = ["3 Aug", "2025", "455"]
        for content in core_content:
            assert content in column_data
            assert content in tooltip_text
        pass
