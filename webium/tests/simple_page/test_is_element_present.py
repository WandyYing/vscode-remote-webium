import pytest
from tests.simple_page import SimplePageTest
from webium.errors import WebiumException


class TestIsElementPresent(SimplePageTest):
    def test_is_element_present(self):
        assert self.page.is_element_present('icon_link')
        assert not self.page.is_element_present('unexistent_element')

    def test_no_attribute(self):
        with pytest.raises(WebiumException):
            self.page.is_element_present('no_such_attribute')
