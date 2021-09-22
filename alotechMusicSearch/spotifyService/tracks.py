import requests
from alotechMusicSearch.spotifyService.authentication import get_access_token
from alotechMusicSearch.spotifyService import spotifyConfiguration


def get_top_tracks_of_artist(artist_id):
    try:
        response = requests.get(
            url=spotifyConfiguration.api_base_url + "artists/" + artist_id + "/top-tracks?market=TR",
            headers={"Authorization": "Bearer " + get_access_token()}
        )

        if response.ok:
            return response.json()
    except:
        return None

    return None
