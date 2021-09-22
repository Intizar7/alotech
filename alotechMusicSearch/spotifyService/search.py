import requests

from alotechMusicSearch.spotifyService import spotifyConfiguration
from alotechMusicSearch.spotifyService.authentication import get_access_token


def search_artist(artist_name):
    try:
        response = requests.get(
            url=spotifyConfiguration.api_base_url + "search?q=" + artist_name + "&type=artist",
            headers={"Authorization": "Bearer " + get_access_token()}
        )

        if response.ok:
            return response.json()
    except:
        return None

    return None
