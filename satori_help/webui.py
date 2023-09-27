from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

from .tui import DOCS_FOLDER


def start_docs_server(port=9090):
    "Start a local docs HTTP server"

    handler = partial(SimpleHTTPRequestHandler, directory=DOCS_FOLDER)
    httpd = HTTPServer(("localhost", port), handler)
    httpd.serve_forever()
