
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="function")
def set_up_browser():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    capabilities = driver.capabilities
    browser_version = capabilities.get('browserVersion')
    driver_version = capabilities.get('chrome', {}).get('chromedriverVersion', 'Unknown')
    driver.implicitly_wait(3)

    print(f"\n[INFO] Используется браузер версии: {browser_version}")
    print(f"[INFO] Используется ChromeDriver версии: {driver_version}")

    yield driver

    driver.quit()