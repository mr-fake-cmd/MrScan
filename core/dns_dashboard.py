from rich.console import Console
from rich.table import Table

from modules.dns import get_dns_info

console = Console()


def dns_dashboard():

    data = get_dns_info()

    table = Table(title="DNS Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    for key, value in data.items():
        table.add_row(key, value)

    console.print(table)