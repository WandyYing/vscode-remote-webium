import time
from webium.driver import get_driver
from webium.fixtures import constants
from webium import settings

def raise_unable_to_load_jquery_exception(driver):
    """ The most-likely reason for jQuery not loading on web pages. """
    raise Exception(
        '''Unable to load jQuery on "%s" due to a possible violation '''
        '''of the website's Content Security Policy directive. '''
        '''To override this policy, add "--disable-csp" on the '''
        '''command-line when running your tests.''' % driver.current_url)


def activate_jquery(driver):
    """ If "jQuery is not defined", use this method to activate it for use.
        This happens because jQuery is not always defined on web sites. """
    try:
        # Let's first find out if jQuery is already defined.
        driver.execute_script("jQuery('html')")
        # Since that command worked, jQuery is defined. Let's return.
        return
    except Exception:
        # jQuery is not currently defined. Let's proceed by defining it.
        pass
    jquery_js = constants.JQuery.MIN_JS
    activate_jquery_script = (
        '''var script = document.createElement('script');'''
        '''script.src = "%s";document.getElementsByTagName('head')[0]'''
        '''.appendChild(script);''' % jquery_js)
    driver.execute_script(activate_jquery_script)
    for x in range(int(settings.MINI_TIMEOUT * 10.0)):
        # jQuery needs a small amount of time to activate.
        try:
            driver.execute_script("jQuery('html')")
            return
        except Exception:
            time.sleep(0.1)
    # Since jQuery still isn't activating, give up and raise an exception
    raise_unable_to_load_jquery_exception(driver)


class JQuery(object):
    """ JQuery class provides jQuery wrapper for Selenium WebElement.

    Example (set element's value attr through jQuery.val function):
      e = driver.find_element_by_id('id_name')
      JQuery(e).val('New name')
    """

    def __init__(self, element):
        self.driver = get_driver()
        activate_jquery(self.driver)
        self.element = element

    def __getattr__(self, name):
        def jquery_func(*args):
            jquery = 'return $(arguments[0]).%(func)s(%(args)s);' % {
                'func': name,
                'args': ','.join(['arguments[%d]' % (1 + i) for i in range(len(args))])
            }
            print(jquery)
            return self.driver.execute_script(jquery, self.element, *args)
        return jquery_func
