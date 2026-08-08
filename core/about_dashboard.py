from rich.console import Console
from rich.panel import Panel

console = Console()


def about_dashboard():

    text = """
MrScan v3.0

Professional Network Inspector

Features
• Quick Scan
• Router Information
• Network Information
• ISP Information
• DNS Information
• Gateway Test
• Export Report
• Settings

Developer : Jarif
Language  : Python
Platform  : Termux / Linux
License   : MIT

GitHub:
https://github.com/mr-fake-cmd/MrScan
"""

    console.print(
        Panel.fit(
            text,
            title="About MrScan",
            border_style="cyan",
        )
    )
