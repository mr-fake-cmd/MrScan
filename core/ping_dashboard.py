from rich.console import Console
from rich.table import Table

from modules.ping import gateway_test

console = Console()


def ping_dashboard():

    data = gateway_test()

    table = Table(title="Gateway Test")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    for key, value in data.items():
        table.add_row(key, str(value))

    console.print(table)