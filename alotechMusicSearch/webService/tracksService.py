from alotechMusicSearch.spotifyService.search import search_artist
from alotechMusicSearch.spotifyService.tracks import get_top_tracks_of_artist


def get_popular_tracks_of_artist(artist_name):
    artist_list = search_artist(artist_name)

    if artist_list is None:
        return None

    artist = artist_list["artists"]["items"][0]
    top_tracks = get_top_tracks_of_artist(artist["id"])

    if top_tracks is None:
        return None

    return top_tracks




