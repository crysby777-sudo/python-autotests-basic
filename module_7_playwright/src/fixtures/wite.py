import allure
import pytest


@pytest.fixture
def wait_element(page):
    def callback(selector: str):
        with allure.step(f"Ожидание элементов по селектору: {selector}"):
            locators_group = page.locator(selector)
            page.wait_for_timeout(2000)
            return locators_group.all()
    return callback
