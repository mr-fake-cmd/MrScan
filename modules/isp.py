import requests


def get_isp_info():

    try:
        data = requests.get(
            "https://ipinfo.io/json",
            timeout=5
        ).json()

        return {
            "Public IP": data.get("ip", "N/A"),
            "ISP": data.get("org", "N/A"),
            "Hostname": data.get("hostname", "N/A"),
            "Country": data.get("country", "N/A"),
            "Region": data.get("region", "N/A"),
            "City": data.get("city", "N/A"),
            "Timezone": data.get("timezone", "N/A"),
            "Location": data.get("loc", "N/A"),
        }

    except Exception:

        return {
            "Public IP": "N/A",
            "ISP": "N/A",
            "Hostname": "N/A",
            "Country": "N/A",
            "Region": "N/A",
            "City": "N/A",
            "Timezone": "N/A",
            "Location": "N/A",
        }