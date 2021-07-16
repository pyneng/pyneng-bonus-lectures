from rich.style import Style
from rich.console import Console
from rich.theme import Theme
from rich.highlighter import RegexHighlighter

from data import ip_list


custom_theme = Theme({
    "success" : "bold green",
    "fail" : "bold red",
    "error": "bold yellow",
    "repr.number": "bold green", # defaults: python -m rich.theme
})
console = Console(theme=custom_theme)
console.print("This is information", style="success")
console.print("[fail]The pod bay doors are locked[/fail]")
console.log("Something terrible happened!", style="error", log_locals=True)
console.print("DANGER!", style="red on black")


# Style
danger_style = Style(color="red", blink=True, bold=True)
console.print("Danger, Will Robinson!", style=danger_style)
base_style = Style.parse("cyan")
console.print("Hello, World", style = base_style + Style(underline=True))


# Custom Highlighter
console.print(ip_list)


class IPHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an IP address."""

    base_style = "example."
    highlights = [r"(?P<ip>\d+\.\d+\.\d+\.\d+)", r"(?P<ip>\d+\.\d+\.\d+\.\d+/\d+)"]


theme = Theme({"example.ip": "bold blue"})
console = Console(highlighter=IPHighlighter(), theme=theme)
console.print(ip_list)
console.log("[red]Connect to [/red]10.1.1.1")
