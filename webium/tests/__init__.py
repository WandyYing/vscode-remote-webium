import http.server as SimpleHTTPServer
import socketserver

from threading import Thread

httpd = socketserver.TCPServer(('', 0), SimpleHTTPServer.SimpleHTTPRequestHandler)
PORT = httpd.server_address[1]


def setup_module():
    print("serving at port", PORT)
    thread = Thread(target=lambda: httpd.serve_forever())
    thread.daemon = True
    thread.start()


def teardown_module():
    pass


def get_url(suffix=''):
    return 'http://127.0.0.1:%s/tests/pages/%s' % (PORT, suffix)