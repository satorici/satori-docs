from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Markdown
from textual.containers import Horizontal, VerticalScroll
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
    CSS = """
        #scroll-sidebar{
            width: 26;
            padding: 0;
            scrollbar-size: 1 1;
        }
        #sidebar{
            width: 1fr;
            padding: 1 0;
        }
        #scroll-content{
            padding: 0;
            scrollbar-size: 1 1;
            width: 1fr
        }
    """

    def __init__(self, **kargs):
        super().__init__(**kargs)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Footer()
        yield Horizontal(
            VerticalScroll(CustomMarkdown("a", id="sidebar"), id="scroll-sidebar"),
            VerticalScroll(CustomMarkdown(id="content"), id="scroll-content"),
        )

    def on_mount(self) -> None:
        path = DOCS_FOLDER + "_sidebar.md"
        with open(path) as f:
            readme = f.read()
        toc = self.query_one("#sidebar", Markdown)
        toc.update(readme)
        self.action_home()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_home(self) -> None:
        md = self.query_one("#content", CustomMarkdown)
        with open(DOCS_FOLDER + "README.md") as f:
            readme = f.read()
        md.update(readme)


class CustomMarkdown(Markdown):
    def _on_markdown_link_clicked(self, message: Markdown.LinkClicked) -> None:
        path = DOCS_FOLDER + message.href
        with open(path) as f:
            readme = f.read()
        self.app.query_one("#content", CustomMarkdown).update(readme)
