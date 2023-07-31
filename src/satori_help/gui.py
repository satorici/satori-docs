from textual.app import App, ComposeResult  # , events
from textual.widgets import Footer, Header, MarkdownViewer, Markdown

from pathlib import Path


DOCS_FOLDER = str(Path(__file__).parent) + "/../docs/"


class HelpGui(App):
    BINDINGS = [
        # ("b", "back", "Back"),
        ("h", "home", "Home"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]
    TITLE = "Satori Docs"

    def __init__(self, **kargs):
        super().__init__(**kargs)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Footer()
        yield Markdown2(id="markdown")

    def on_mount(self) -> None:
        self.action_home()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_home(self) -> None:
        md: Markdown2 = self.query_one("#markdown")  # type: ignore
        with open(DOCS_FOLDER + "README.md") as f:
            readme = f.read()
        md.document.update(readme)

    # def action_back(self) -> None:
    #     md: Markdown2 = self.query_one("#markdown")  # type: ignore
    #     md.back()


class Markdown2(MarkdownViewer):
    def _on_markdown_link_clicked(self, message: Markdown.LinkClicked) -> None:
        path = DOCS_FOLDER + message.href
        with open(path) as f:
            readme = f.read()
        self.document.update(readme)

    # def _on_key(self, event: events.Key) -> None:
    #     self.table_of_contents.set_table_of_contents([(1, "str", "link")])
    #     if event.key == "tab":
    #         pass
