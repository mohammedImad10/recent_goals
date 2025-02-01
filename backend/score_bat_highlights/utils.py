import requests
from recent_goals.settings import API_TOKEN, API_URL


def fetch_bat_highlights_from_api():
    """
    Fetch video highlights from a third-party API and return the response data.
    """
    try:
        response = requests.get(f"{API_URL}?token={API_TOKEN}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None
