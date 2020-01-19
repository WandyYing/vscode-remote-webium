from selenium.webdriver.remote.webelement import WebElement as selenium_WebElement

class WebElement(selenium_WebElement):

    def __init__(self, *args, **kwargs):
        super(WebElement, self).__init__(*args, **kwargs)