import requests
from config import SHRTLINK_APIKEY

def shorten_link(destination_url, alias=None):
    url = "https://shrtlnk.dev/api/v2/link"
    headers = {
        "api-key": SHRTLINK_APIKEY,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {"url": destination_url}
    if alias:
        payload["alias"] = alias

    response = requests.post(url, headers=headers, json=payload)
    return response.json()['shrtlnk'] if response.ok else {"error": response.status_code, "message": response.text}

def shorten_link_old(destination_url, alias=None):
    url = f"https://ulvis.net/api.php?url={destination_url}&private=1"
    response = requests.get(url)
    return response.text if response.ok else {"error": response.status_code, "message": response.text}

