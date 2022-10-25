import auth_manager
import search_engine


if __name__ == '__main__':
    sp = auth_manager.getSpotifyClient()
    track_name = input("Choose a track name to search: ")
    songs = search_engine.search_track(sp, track_name=track_name, limit=5)
    for item in songs:
        print(item["artists"][0]["name"], "-", item["name"])
        print("Popularity: ", item["popularity"])
        print("Release Date: ", item["album"]["release_date"])
        print("Album URI: ", item["album"]["uri"])
        print("Album Cover:", item["album"]["images"][0]["url"])
        print("Spotify Url: ", item["external_urls"]["spotify"])
        print("##################################################")