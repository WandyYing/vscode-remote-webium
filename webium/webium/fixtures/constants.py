"""
Webium constants are stored in this file.
"""


class JQuery:
    VER = "3.4.1"
    MIN_JS = "//cdnjs.cloudflare.com/ajax/libs/jquery/%s/jquery.min.js" % VER
    LOCAL_JQUERY_PATH = './webium/jquery/jquery-3.4.1.min.js' #todo: Local


class Browser:
    GOOGLE_CHROME = "chrome"
    EDGE = "edge"
    FIREFOX = "firefox"
    INTERNET_EXPLORER = "ie"
    OPERA = "opera"
    PHANTOM_JS = "phantomjs"
    SAFARI = "safari"
    ANDROID = "android"
    IPHONE = "iphone"
    IPAD = "ipad"
    REMOTE = "remote"


class Files:
    DOWNLOADS_FOLDER = "downloaded_files"
    ARCHIVED_DOWNLOADS_FOLDER = "archived_files"