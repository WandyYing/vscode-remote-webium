import pytest
from tests.simple_page import SimplePageTest, Container
from webium.errors import WebiumException
from webium.find import Find


class TestLogicalContainer(SimplePageTest):
    def test_logical_container(self):
        assert self.page.logical_container.span.text == 'An inline element'

    def test_type_validation(self):
        with pytest.raises(WebiumException):
            Find(Container)
