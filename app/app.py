import requests


def is_alive_host(hostname):
    if not (hostname.startswith("https://") or hostname.startswith("http://")):
        hostname = "http://" + hostname
    is_alive = True
    try:
        response = requests.head(hostname)
        is_alive = 100 <= response.status_code < 400
    except requests.ConnectionError:
        return False
    return is_alive
    
