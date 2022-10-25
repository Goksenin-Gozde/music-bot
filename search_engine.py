def search_track(sp, track_name: str, limit: int):
    result = sp.search(q="track: " + track_name, type="track", limit=limit)
    return result["tracks"]["items"]