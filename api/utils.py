import requests
from django.conf import settings


def fetch_ip_details(ip_or_url):
    """Retrieve IPStack details about provided either ip address or url."""
    try:
        api_url = f"http://api.ipstack.com/{ip_or_url}?access_key={settings.IP_STACK_API_KEY}"
        return requests.get(api_url).json()
    except:
        return
