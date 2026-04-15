
class TestSkillbox:
    def test_skillbox_title(self,set_up_browser):
        driver = set_up_browser
        set_up_browser.get("https://skillbox.ru/")
        assert "Skillbox" in driver.title

    def test_skillbox_title_1(self,set_up_browser):
        driver = set_up_browser
        set_up_browser.get("https://sales.skillbox.by/")
        assert 'Скидка до 55%' in driver.title

    def test_user_profile_placeholder(self):
        pass

    def test_search_functional_placeholder(self):
        pass


