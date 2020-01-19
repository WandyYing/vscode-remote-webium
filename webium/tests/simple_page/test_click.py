from webium.driver import get_driver
from tests.simple_page import SimplePageTest


class TestClick(SimplePageTest):
    def test_basic_click(self):
        self.page.icon_link.click()
        assert get_driver().current_url.endswith('icon.gif'), 'Page after click wasn\'t opened'

    def test_jquery_click(self):
        assert not self.page.checkbox.is_selected()
        self.page.checkbox.click(True)
        assert self.page.checkbox.is_selected()
