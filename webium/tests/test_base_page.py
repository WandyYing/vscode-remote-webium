import pytest
from unittest import TestCase
from webium.base_page import BasePage
from webium.errors import WebiumException


class PageWithoutUrl(BasePage):
    pass


class TestNoUrlValidation(TestCase):
    def test_no_url_validation(self):
        page = PageWithoutUrl()
        with pytest.raises(WebiumException):
            page.open()