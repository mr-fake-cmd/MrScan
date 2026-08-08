from core.utils import run


def get_dns_info():

    dns1 = run("getprop net.dns1") or "N/A"
    dns2 = run("getprop net.dns2") or "N/A"

    return {
        "Primary DNS": dns1,
        "Secondary DNS": dns2,
    }