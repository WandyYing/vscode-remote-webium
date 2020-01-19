from webium.driver import get_driver
from tests.simple_page import SimplePageTest


class TestCheckbox(SimplePageTest):


    def test_jquery_click(self):
        assert not self.page.checkbox.is_selected()
        self.page.checkbox.check()
        assert self.page.checkbox.is_selected()