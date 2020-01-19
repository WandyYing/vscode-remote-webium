from selenium import webdriver
import webium.settings


_driver_instance = None

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('disable-dev-shm-usage')
options.add_argument('no-sandbox')

def get_driver():
    global _driver_instance
    if not _driver_instance:
        _driver_instance = webium.settings.driver_class(options=options)
        _driver_instance.implicitly_wait(webium.settings.implicit_timeout)
    return _driver_instance


def get_driver_no_init():
    return _driver_instance


def close_driver():
    global _driver_instance
    if _driver_instance:
        _driver_instance.quit()
        _driver_instance = None