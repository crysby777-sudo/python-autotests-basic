import logging
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest


@pytest.fixture()
def selenium(pytestconfig):

    options = ChromeOptions()
    options.browser_name = "Сhrome"
    logging.info(f"Запуск {options.browser_name} браузера...")
    options.set_capability("browserVersion", "latest")
    options.set_capability("selenoid:options", {
        "enableVNC": False
    })

    driver = Remote(
        command_executor=pytestconfig.getini("selenium_url"),
        options=options
    )
    actual_version = driver.capabilities.get('browserVersion', 'unknown')

    logging.info(f"Начало тестирования с помощью браузера {options.browser_name}, версия {actual_version} ...")
    yield driver
    logging.info(f"Остановка браузера {options.browser_name} ...")
    driver.quit()
