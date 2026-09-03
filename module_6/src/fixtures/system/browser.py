import logging
from idlelib import window

from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def selenium(pytestconfig):

    options = ChromeOptions()
    options.browser_name = "Сhrome"
    logging.info(f"Запуск {options.browser_name} браузера...")
    options.set_capability("browserVersion", "latest")
    options.set_capability("selenoid:options", {
        "enableVNC": False
    })
    options.add_argument("--window-size=1920,1080")  # Установка размера окна браузера
    options.add_argument("--start-maximized")  # Запуск браузера в развёрнутом на весь экран состоянии

    """driver = Remote(
        command_executor=pytestconfig.getini("selenium_url"),
        options=options
    )"""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    actual_version = driver.capabilities.get('browserVersion', 'unknown')

    logging.info(f"Начало тестирования с помощью браузера {options.browser_name}, версия {actual_version} ...")
    yield driver
    logging.info(f"Остановка браузера {options.browser_name} ...")
    driver.quit()
