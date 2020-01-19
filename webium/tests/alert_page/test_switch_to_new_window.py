from unittest import TestCase
from tests.alert_page import AlertPage
from webium.windows_handler import WindowsHandler


class TestSwitchToNewWindow(TestCase):

    def test_switch_to_new_window(self):
        page = AlertPage()
        handler = WindowsHandler()
        page.open()
        parent = handler.active_window
        handler.save_window_set()
        assert not (handler.is_new_window_present())
        page.open_new_window_link.click()
        assert (handler.is_new_window_present())
        new = handler.new_window
        handler.switch_to_new_window()
        assert new == handler.active_window
        handler.drop_active_window()
        assert parent == handler.active_window
