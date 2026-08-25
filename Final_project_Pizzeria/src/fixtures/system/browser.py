import logging
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

"""Конфигурация параметров запуска браузера Chrome перед инициализацией тестового сценария"""


@pytest.fixture(scope="function")
def selenium():
    options = ChromeOptions()
    logging.info("Launching Chrome browser...")

    options.add_argument("--incognito")  # Запуск браузера в режиме "Инкогнито" (приватный режим)
    options.add_argument("--headless=new")  # Запуск браузера в фоновом режиме (без графического интерфейса)
    options.add_argument("--window-size=1920,1080")  # Установка размера окна браузера
    options.add_argument("--start-maximized")  # Запуск браузера в развёрнутом на весь экран состоянии

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    actual_version = driver.capabilities.get('browserVersion', 'unknown')
    logging.info(f"Начало тестирования с помощью браузера Chrome, версия {actual_version} ...")

    yield driver

    logging.info("Closing Chrome Browser...")
    driver.quit()
