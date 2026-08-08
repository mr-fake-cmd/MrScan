from rich.console import Console
from rich.panel import Panel

from modules.report import export_report

console = Console()


def report_dashboard():

    filename = export_report()

    console.print(
        Panel.fit(
            f"[green]Report exported successfully![/green]\n\n{filename}",
            title="Export Report"
        )
    )