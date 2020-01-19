from unittest import TestCase
from tests.alert_page import AlertPage
from webium.windows_handler import WindowsHandler


class TestAlert(TestCase):
    def test_alert_presence(self):
        page = AlertPage()
        page.open()
        handler = WindowsHandler()
        assert not (handler.is_alert_present())
        page.alert_link.click()
        assert handler.is_alert_present()
        assert handler.get_alert_text() == 'cheese'
        handler.accept_alert()
        assert not (handler.is_alert_present())
