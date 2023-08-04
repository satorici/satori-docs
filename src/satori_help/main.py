#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from .gui import HelpGui, DOCS_FOLDER


def main():
    baseparser = ArgumentParser(add_help=False)
    parser = ArgumentParser(parents=[baseparser], prog="satori-docs")
    parser.add_argument("-w", "--web", default=False, action="store_true")

    args = parser.parse_args()
    try:
        if args.web:
            handler = partial(SimpleHTTPRequestHandler, directory=DOCS_FOLDER)
            httpd = HTTPServer(("localhost", 9090), handler)
            print("Docs server running on: http://localhost:9090")
            httpd.serve_forever()
        else:
            gui = HelpGui()
            gui.run()
    except KeyboardInterrupt:
        print("Interrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
