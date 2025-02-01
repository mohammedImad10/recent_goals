import requests


API_URL = "https://www.scorebat.com/video-api/v3/feed/"
API_TOKEN = "MTQzMTkxXzE3MjM5MTkyMzlfNjJkZjVjNDdiYmFmYzAzMDNmOTk1OTNiNzBlODE1ZmUxMTZjM2UyZg=="


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


# import requests
# from datetime import datetime
# from score_bat_highlights.models import BatHighlight


# API_URL = "https://www.scorebat.com/video-api/v3/feed/"
# API_TOKEN = "MTQzMTkxXzE3MjM5MTkyMzlfNjJkZjVjNDdiYmFmYzAzMDNmOTk1OTNiNzBlODE1ZmUxMTZjM2UyZg=="


# def fetch_and_store_bat_highlights():
#     # API call and data extraction logic
#     response = requests.get(f"{API_URL}?token={API_TOKEN}")
#     embed_code = ""
#     if response.status_code == 200:
#         data = response.json()
#         if 'response' in data and data['response']:
#             new_matches = []
#             for match in data['response']:
#                 title = match.get('title', '')
#                 competition = match.get('competition', '')
#                 date = datetime.strptime(match.get('date', ''), "%Y-%m-%dT%H:%M:%S%z").date()
#                 if match.get("videos"):
#                     first_video = match["videos"][0]
#                     embed_code = first_video.get("embed", "")
#                 # Check for existing match
#                 existing_match = BatHighlight.objects.filter(title=title, competition=competition, date=date).exists()
#                 if existing_match:
#                     print(f"No new matches: {title} already exists.")
#                 else:  
#                     # Save the new match
#                     new_match = BatHighlight(title=title, competition=competition, date=date, embed_video=embed_code)
#                     new_match.save()
#                     new_matches.append(new_match)
#                     print(f"New match saved: {title}")
#             if not new_matches:
#                 print("No new matches found.")
#         else:
#             print("No matches in API response.")
#     else:
#         print(f"API request failed with status code {response.status_code}")
