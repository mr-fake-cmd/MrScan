from core.utils import run
from modules.network import get_gateway


def get_router_info():

    gateway = get_gateway()

    info = {
        "Gateway": gateway,
        "HTTP": "Unknown",
        "HTTPS": "Unknown",
    }

    if gateway == "N/A":
        return info

    http = run(f"curl -L -I --max-time 3 http://{gateway} | head -n 1")
    https = run(f"curl -k -L -I --max-time 3 https://{gateway} | head -n 1")

    if http:
        info["HTTP"] = "Available"

    if https:
        info["HTTPS"] = "Available"

    return info