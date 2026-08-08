from rich.console import Console
from rich.table import Table

from modules.isp import get_isp_info

console = Console()


def isp_dashboard():

    data = get_isp_info()

    table = Table(title="ISP Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    for key, value in data.items():
        table.add_row(key, str(value))

    console.print(table)