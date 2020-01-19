from tests.simple_page import SimplePageTest
from tests import get_url

class TestClick(SimplePageTest):
    def test_link(self):
        assert self.page.icon_link.get_href() == get_url('icon.gif')