import pytest
from tests.simple_page import SimplePageTest
from webium.driver import get_driver
from webium.errors import WebiumException
from webium.find import Find


class TestDynamic(SimplePageTest):
    def test_positive_flow(self):
        assert Find(value='oneline', context=get_driver()).text == 'A single line of text'

    def test_context_validation(self):
        with pytest.raises(WebiumException):
            getattr(Find(value='oneline'), 'text')