from rich.console import Console
from rich.panel import Panel

console = Console()

def banner():
    console.clear()

    logo = r"""
███╗   ███╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
████╗ ████║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔████╔██║██████╔╝███████╗██║     ███████║██╔██╗ ██║
██║╚██╔╝██║██╔══██╗╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║███████║╚██████╗██║  ██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

    panel = Panel.fit(
        f"{logo}\n\n"
        "[bold cyan]Professional Network Inspector[/bold cyan]\n"
        "[green]Version:[/green] 3.0\n"
        "[yellow]Developed by: Jarif[/yellow]",
        title="[bold green]MrScan[/bold green]",
        border_style="bright_green",
        padding=(1, 2)
    )

    console.print(panel)
