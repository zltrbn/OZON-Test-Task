import requests

URL = "https://akabab.github.io/superhero-api/api/all.json"

def get_heros():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()
