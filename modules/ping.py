from core.utils import run
from modules.network import get_gateway


def gateway_test():

    gateway = get_gateway()

    if gateway == "N/A":
        return {
            "Gateway": "N/A",
            "Status": "Unavailable",
            "Latency": "N/A",
        }

    output = run(f"ping -c 1 -W 2 {gateway}")

    status = "Offline"
    latency = "N/A"

    if "1 packets transmitted, 1 received" in output or "1 received" in output:
        status = "Online"

        for line in output.splitlines():
            if "time=" in line:
                latency = line.split("time=")[1].split()[0] + " ms"
                break

    return {
        "Gateway": gateway,
        "Status": status,
        "Latency": latency,
    }