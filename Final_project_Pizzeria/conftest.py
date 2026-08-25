import logging.config
from os import path
import pytest
import allure
from config.configuration import Config


lof_file_path = path.join(path.dirname(path.abspath(__file__)), 'src/utils/logging.ini')
logging.config.fileConfig(lof_file_path)

pytest_plugins = [
    'src.fixtures.system.browser'
]


def pytest_configure(config):
    allure_dir = config.getoption('--alluredir')
    if allure_dir:
        absolute_allure_dir = config.rootdir / allure_dir
        config.option.allure_report_dir = absolute_allure_dir


def pytest_addoption(parser):

    parser.addini("selenium_url", "Selenium Hub url")
    parser.addini("browser_name", "Browser name for tests")
    parser.addini("browser_version", "Browser version for tests")


@pytest.fixture
def open_url(selenium):
    @allure.step("Переход на страницу: {url}")
    def callback(url):
        logging.info(f"Open web browser url: {url}")
        selenium.get(url)
        selenium.implicitly_wait(Config.IMPLICIT_WAIT)
    return callback
