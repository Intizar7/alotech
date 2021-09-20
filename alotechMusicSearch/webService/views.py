from django.http import JsonResponse

def search_track(request, genre):
    """Search track action."""
    response = JsonResponse([
        {"artistName": "Lorem ipsum", "trackName": "Sed Aliquam", "coverUrl": "http://lorempixel.com/400/200", "previewUrl": "http://lorempixel.com/400/200"},
        {"artistName": "Lorem ipsum", "trackName": "Sed Aliquam", "coverUrl": "http://lorempixel.com/400/200", "previewUrl": "http://lorempixel.com/400/200"},
        {"artistName": "Lorem ipsum", "trackName": "Sed Aliquam", "coverUrl": "http://lorempixel.com/400/200", "previewUrl": "http://lorempixel.com/400/200"},
        {"artistName": "Lorem ipsum", "trackName": "Sed Aliquam", "coverUrl": "http://lorempixel.com/400/200", "previewUrl": "http://lorempixel.com/400/200"},
        {"artistName": "Lorem ipsum", "trackName": "Sed Aliquam", "coverUrl": "http://lorempixel.com/400/200", "previewUrl": "http://lorempixel.com/400/200"},
    ], safe=False)
    return response

