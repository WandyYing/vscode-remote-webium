from unittest import TestCase
from webium.jquery import JQuery

from tests.simple_page import SimplePage, SimplePageTest


class SimpleJQueryPage(SimplePage):
    def get_text_by_jquery(self):
        return JQuery(self.one_line).text()

    def change_text_by_jquert(self):
        return JQuery(self.input_user).val("a user name")
    
    def get_value_by_jquery(self):
        return JQuery(self.input_user).val()

class TestJQuery(TestCase):
    def test_jquery_call(self):
        page = SimpleJQueryPage()
        page.open()
        assert page.get_text_by_jquery() == 'A single line of text'
        page.change_text_by_jquert()
        assert page.get_value_by_jquery() == "a user name"
        