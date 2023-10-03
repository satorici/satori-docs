import webbrowser
from pathlib import Path

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Footer, Header, Markdown

DOCS_FOLDER = Path(__file__).parent / "docs"


class HelpApp(App):
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

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        yield Footer()
        yield Horizontal(
            VerticalScroll(Markdown(id="sidebar"), id="scroll-sidebar"),
            VerticalScroll(Markdown(id="content"), id="scroll-content"),
        )

    def on_mount(self) -> None:
        readme = (DOCS_FOLDER / "_sidebar.md").read_text()
        toc = self.query_one("#sidebar", Markdown)
        toc.update(readme)
        self.action_home()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_home(self) -> None:
        md = self.query_one("#content", Markdown)
        readme = (DOCS_FOLDER / "README.md").read_text()
        md.update(readme)

    @on(Markdown.LinkClicked)
    def link_clicked(self, message: Markdown.LinkClicked):
        if message.href.startswith("http"):
            webbrowser.open(message.href)
            return

        readme = (DOCS_FOLDER / message.href.removeprefix("/")).read_text()
        self.query_one("#content", Markdown).update(readme)
