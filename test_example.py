

class TestExample:
    def test_example(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox' in driver.title

class TestExample_1:
    def test_example(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox' == driver.title

class TestExample_2:
    def test_example(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox' == driver.title

class TestExample_3:
    def test_example(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        assert 'Skillbox' in driver.title

