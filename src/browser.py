import pytest
import subprocess
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


""" Фикстура сессии: запускает Selenium Grid перед всеми тестами и останавливает после их завершения."""

@pytest.fixture(scope="session", autouse=True)
def selenium_grid_server():
    process = subprocess.Popen([
        "java", "-jar", "selenium-server-4.41.0.jar", "standalone"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(30):
        try:
            requests.get("http://127.0.0.1:4444/status")
            break
        except requests.ConnectionError:
            time.sleep(1)
    yield
    process.terminate()
    """ Конец Selenium Grid"""

@pytest.fixture()
def set_up_browser():
    chrome_options = Options()
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        options=chrome_options
    )
    yield driver
    driver.quit()


