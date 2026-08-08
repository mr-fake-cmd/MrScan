from rich.console import Console
from rich.table import Table
from core.network_dashboard import network_dashboard
from core.isp_dashboard import isp_dashboard
from core.dns_dashboard import dns_dashboard
from core.ping_dashboard import ping_dashboard
from core.report_dashboard import report_dashboard
from core.settings_dashboard import settings_dashboard
from core.about_dashboard import about_dashboard

from core.loading import loading
from core.dashboard import dashboard
from core.router_dashboard import router_dashboard

console = Console()


def menu():

    table = Table(title="Main Menu", show_lines=True)

    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Feature", style="green")

    table.add_row("1", "Quick Scan")
    table.add_row("2", "Router Information")
    table.add_row("3", "Network Information")
    table.add_row("4", "ISP Information")
    table.add_row("5", "DNS Information")
    table.add_row("6", "Gateway Test")
    table.add_row("7", "Export Report")
    table.add_row("8", "Settings")
    table.add_row("9", "About")
    table.add_row("0", "Exit")

    console.print(table)

    while True:

        choice = console.input("\n[bold cyan]MrScan > [/bold cyan]")

        if choice == "1":
            loading("Running Quick Scan...")
            dashboard()

        elif choice == "2":
            loading("Loading Router Information...")
            router_dashboard()

        elif choice == "3":
            loading("Loading Network Information...")
            network_dashboard()

        elif choice == "4":
            loading("Loading ISP Information...")
            isp_dashboard()

        elif choice == "5":
            loading("Loading DNS Information...")
            dns_dashboard()

        elif choice == "6":
            loading("Testing Gateway...")
            ping_dashboard()

        elif choice == "7":
            loading("Exporting Report...")
            report_dashboard()

        elif choice == "8":
            loading("Opening Settings...")
            settings_dashboard()

        elif choice == "9":
            about_dashboard()

        elif choice == "0":
            console.print("[red]Goodbye![/red]")
            break

        else:
            console.print("[yellow]Invalid Option[/yellow]")