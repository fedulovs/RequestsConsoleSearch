import requests

# Parse response
def parse_results(result):
    songs = {}
    for song in results:
        artist = song['artist']
        song_name = song['title']

        if songs.get(artist) is None:
            songs.update({artist: [song_name]})
        else:
            songs.get(artist).append(song_name)
    return songs


# Print all the found songs in alphabetical order, sorted primarily by the artist name, and then by the song name
def sort_and_print(songs):
    sorted_artists = sorted(songs)

    for artist in sorted_artists:
        artists_songs = sorted(songs[artist])

        for artists_song in artists_songs:
            print(artist + " - " + artists_song)


# Check if request was successful
def is_response_successful(res):
    print('Checking response status')
    if res and res.status_code == 200:
        print('Response OK')
        return True
    else:
        print('Response Failed')
        print(res.reason)
        return False


if __name__ == '__main__':

    url = 'https://api.yousician.com/library/search'
    query = input('Enter your query: ')
    if query != '':
        params = dict(search=query)
        headers = {'X-Application-Name': 'SongsLibrarySite', 'Accept': '*/*'}
        try:
            res = requests.get(url, params=params, headers=headers)
            if is_response_successful(res):
                results = res.json()['exercises']
                if len(results) > 0:
                    songs = parse_results(results)
                    sort_and_print(songs)
                else:
                    print('There are no results')
            else:
                print('Error in request')
                print(res.text)
        except Exception as e:
            print('Error \n' + str(e))
    else:
        print('Incorrect query')
