import requests


def is_online():
    try:
        requests.get("https://1.1.1.1", timeout=3)
        return True
    except:
        return False