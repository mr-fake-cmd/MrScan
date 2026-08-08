from core.utils import run, command_exists
import requests


def get_private_ip():

    if command_exists("ip"):

        ip = run(
            "ip route | awk '/src/ {for(i=1;i<=NF;i++) if($i==\"src\") print $(i+1)}'"
        )

        if ip:
            return ip

        ip = run(
            "ip -4 addr show wlan0 | awk '/inet /{print $2}' | cut -d/ -f1"
        )

        if ip:
            return ip

    if command_exists("ifconfig"):

        ip = run(
            "ifconfig wlan0 | awk '/inet /{print $2}'"
        )

        if ip:
            return ip

    ip = run("getprop dhcp.wlan0.ipaddress")

    if ip:
        return ip

    return "N/A"


def get_gateway():

    # Standard Linux gateway
    if command_exists("ip"):
        gw = run("ip route | awk '/default/ {print $3}'")
        if gw:
            return gw

    # Android DHCP properties
    for prop in (
        "dhcp.wlan0.gateway",
        "dhcp.gateway",
        "dhcp.wlan.gateway",
    ):
        gw = run(f"getprop {prop}")
        if gw:
            return gw

    # Fallback: DNS1 (common on many Android devices)
    dns = run("getprop net.dns1")
    if dns.startswith(("192.168.", "10.", "172.")):
        return dns

    return "N/A"


def get_dns():

    dns1 = run("getprop net.dns1") or "N/A"
    dns2 = run("getprop net.dns2") or "N/A"

    return dns1, dns2


def get_public_info():

    try:
        response = requests.get(
            "https://ipinfo.io/json",
            timeout=5
        )

        return response.json()

    except Exception:
        return {}