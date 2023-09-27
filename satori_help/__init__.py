from .tui import HelpApp
from .webui import start_docs_server


def cli():
    import sys
    from argparse import ArgumentParser

    parser = ArgumentParser(prog="satori-docs")
    group = parser.add_argument_group("webdocs")
    group.add_argument("-w", "--web", action="store_true")
    group.add_argument("-p", "--port", default=9090, type=int)

    args = parser.parse_args()

    try:
        if args.web:
            print(f"Docs server running on: http://localhost:{args.port}")
            start_docs_server(args.port)
        else:
            HelpApp().run()
    except KeyboardInterrupt:
        print("Interrupted by user")
        sys.exit(1)
