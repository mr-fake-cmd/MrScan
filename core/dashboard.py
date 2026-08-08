from rich.console import Console
from rich.table import Table

from modules.network import (
    get_private_ip,
    get_gateway,
    get_dns,
    get_public_info
)

from modules.internet import is_online
from modules.router import get_router_info

console = Console()


def dashboard():

    info = get_public_info()
    dns = get_dns()
    router = get_router_info()

    status = "[green]Online[/green]" if is_online() else "[red]Offline[/red]"

    table = Table(title="Quick Scan")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Internet", status)
    table.add_row("Private IP", get_private_ip())
    table.add_row("Gateway", get_gateway())
    table.add_row("DNS 1", dns[0])
    table.add_row("DNS 2", dns[1])
    table.add_row("Public IP", info.get("ip", "N/A"))
    table.add_row("ISP", info.get("org", "N/A"))
    table.add_row("Country", info.get("country", "N/A"))
    table.add_row("City", info.get("city", "N/A"))
    table.add_row("HTTP Panel", router["HTTP"])
    table.add_row("HTTPS Panel", router["HTTPS"])

    console.print(table)