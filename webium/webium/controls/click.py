from webium.jquery import JQuery
from webium.controls.webelement import WebElement

__author__ = 'm_solonin'


class Clickable(WebElement):

    def click(self, jquery=False):
        """
        Click by WebElement, if not, JQuery click
        """
        if jquery:
            e = JQuery(self)
            e.click()
        else:
            super(Clickable, self).click()
