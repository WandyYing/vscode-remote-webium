from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver_class = Chrome
implicit_timeout = 30
wait_timeout = 30

default_search_type = By.ID

try:
    from local_webium_settings import *
except ImportError:
    pass

# Default maximum time (in seconds) to wait for page elements to appear.
# Different methods/actions in base_case.py use different timeouts.
# If the element to be acted on does not appear in time, the test fails.
MINI_TIMEOUT = 2
SMALL_TIMEOUT = 6
LARGE_TIMEOUT = 10
EXTREME_TIMEOUT = 30