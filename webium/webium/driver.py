from selenium import webdriver
import webium.settings
from webium.core.browser_launcher import get_local_driver


_driver_instance = None

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('disable-dev-shm-usage')
options.add_argument('no-sandbox')

def get_driver():
    global _driver_instance
    if not _driver_instance:
        _driver_instance = get_local_driver("chrome", True, "localhost",
                                            None, None, None, None, None,
                                            None, False, None, None, None,
                                            None, None, None, None, None)
        # _driver_instance = webium.settings.driver_class(options=options)
        _driver_instance.implicitly_wait(webium.settings.implicit_timeout)
    return _driver_instance


def get_driver_no_init():
    return _driver_instance


def close_driver():
    global _driver_instance
    if _driver_instance:
        _driver_instance.quit()
        _driver_instance = None


def get_new_driver(browser=None, headless=None,
                       servername=None, port=None, proxy=None, agent=None,
                       switch_to=True, cap_file=None, disable_csp=None,
                       enable_sync=None, incognito=None, user_data_dir=None,
                       extension_zip=None, extension_dir=None, is_mobile=False,
                       d_width=None, d_height=None, d_p_r=None):
    
    if browser == "remote" and servername == "localhost":
        raise Exception('Cannot use "remote" browser driver on localhost!'
                        ' Did you mean to connect to a remote Grid server'
                        ' such as BrowserStack or Sauce Labs? In that'
                        ' case, you must specify the "server" and "port"'
                        ' parameters on the command line! '
                        'Example: '
                        '--server=user:key@hub.browserstack.com --port=80')
    pass
