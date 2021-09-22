import json
import random


def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def read_json(path):
    return json.loads(read_file(path))

def find_artist_name_by_genre(genre):
    genresJson = read_json('alotechMusicSearch/webService/genres.json')

    if genre in genresJson:
        return random.choice(genresJson[genre])

    return None