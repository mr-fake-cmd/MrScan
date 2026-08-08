from rich.console import Console
from rich.table import Table

from modules.network import (
    get_private_ip,
    get_gateway,
    get_dns,
    get_public_info,
)

console = Console()


def network_dashboard():

    info = get_public_info()
    dns = get_dns()

    table = Table(title="Network Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Private IP", get_private_ip())
    table.add_row("Gateway", get_gateway())
    table.add_row("DNS 1", dns[0])
    table.add_row("DNS 2", dns[1])
    table.add_row("Public IP", info.get("ip", "N/A"))
    table.add_row("ISP", info.get("org", "N/A"))
    table.add_row("ASN", info.get("org", "N/A"))
    table.add_row("Country", info.get("country", "N/A"))
    table.add_row("Region", info.get("region", "N/A"))
    table.add_row("City", info.get("city", "N/A"))
    table.add_row("Timezone", info.get("timezone", "N/A"))

    console.print(table)