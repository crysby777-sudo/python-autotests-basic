# conftest.py
import pytest
import subprocess
import time
import requests
from pathlib import Path
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def selenium_grid_server():
    # Путь к JAR-файлу в корне проекта
    jar_path = Path(__file__).parent / "selenium-server-4.41.0.jar"
    # Запуск сервера
    process = subprocess.Popen(
        ["java", "-jar", str(jar_path), "standalone"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    # Ожидание готовности
    for _ in range(30):
        try:
            requests.get("http://127.0.0.1:4444/status")
            break
        except requests.ConnectionError:
            time.sleep(1)
    yield
    process.terminate()

@pytest.fixture
def driver(selenium_grid_server):
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444",
        options=webdriver.ChromeOptions()
    )
    yield driver
    driver.quit()