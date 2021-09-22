from django.http import JsonResponse
from alotechMusicSearch.webService.genreService import find_artist_name_by_genre
from alotechMusicSearch.webService.tracksService import get_popular_tracks_of_artist


def search_track(request, genre):
    """Search track action."""
    artist_name = find_artist_name_by_genre(genre)

    if artist_name is None:
        return JsonResponse({
            "message": "No artist found"
        }, status=404)

    tracks = get_popular_tracks_of_artist(artist_name)

    if tracks is None:
        return JsonResponse({
            "message": "No track found"
        }, status=404)

    new_track_list = []
    for track in tracks["tracks"]:
        new_track_list.append({
            "artist": track["artists"][0]["name"],
            "track": track["name"],
            "preview_url": track["preview_url"],
            "album_image_url": track["album"]["images"][0]["url"],
        })

    response = JsonResponse(new_track_list, safe=False)
    return response

