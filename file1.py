import requests
import time

def fetch_customers(url):
    response = requests.get(url, timeout=30)

    if response.status_code == 429:
        time.sleep(5)
        response = requests.get(url, timeout=30)

    response.raise_for_status()
    return response.json()
