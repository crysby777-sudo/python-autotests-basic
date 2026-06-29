import allure
import pytest


@pytest.fixture
def go_to_url(page):
    @allure.step(f"Переход на страницу {page}")
    def callback(url):
        page.goto(url)
    return callback
