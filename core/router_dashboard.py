from rich.console import Console
from rich.table import Table

from modules.router import get_router_info

console = Console()


def router_dashboard():

    router = get_router_info()

    table = Table(title="Router Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Gateway", router["Gateway"])
    table.add_row("HTTP", router["HTTP"])
    table.add_row("HTTPS", router["HTTPS"])

    if router["Gateway"] != "N/A":
        table.add_row("Admin URL", f"http://{router['Gateway']}")
    else:
        table.add_row("Admin URL", "N/A")

    console.print(table)