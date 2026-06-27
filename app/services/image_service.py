import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")


def get_destination_image(destination):
    url = "https://api.unsplash.com/search/photos"

    headers = {
        "Authorization": f"Client-ID {ACCESS_KEY}"
    }

    params = {
        "query": f"{destination} landmarks",
        "per_page": 1,
        "orientation": "landscape"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()

        if data["results"]:
            return data["results"][0]["urls"]["full"]

        return None

    except Exception:
        return None
