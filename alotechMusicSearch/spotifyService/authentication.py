import requests
from alotechMusicSearch.spotifyService import spotifyConfiguration

def get_access_token():
    response = requests.post(
        url=spotifyConfiguration.auth_url,
        data={"grant_type": "client_credentials"},
        headers={"Authorization": "Basic " + spotifyConfiguration.base64ClientAndSecret}
    )

    if response.ok:
        return response.json()["access_token"]

    return None