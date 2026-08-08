from datetime import datetime

from modules.network import (
    get_private_ip,
    get_gateway,
    get_dns,
    get_public_info,
)


def export_report():

    info = get_public_info()
    dns = get_dns()

    report = f"""MrScan Report
============================

Date: {datetime.now()}

Private IP : {get_private_ip()}
Gateway    : {get_gateway()}
DNS 1      : {dns[0]}
DNS 2      : {dns[1]}

Public IP  : {info.get("ip", "N/A")}
ISP        : {info.get("org", "N/A")}
Country    : {info.get("country", "N/A")}
Region     : {info.get("region", "N/A")}
City       : {info.get("city", "N/A")}
Timezone   : {info.get("timezone", "N/A")}
"""

    filename = datetime.now().strftime("reports/report_%Y%m%d_%H%M%S.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    return filename