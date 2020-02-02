from tests.simple_page import SimplePageTest
from webium.controls.webelement import WebElement


class TestType(SimplePageTest):

    def test_find_type(self):
        assert isinstance(self.page.icon_link, WebElement)

    def test_finds_type(self):
        assert isinstance(self.page.paragraphs, list)
        assert isinstance(self.page.paragraphs[4], WebElement)