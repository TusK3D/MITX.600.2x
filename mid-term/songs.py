import random

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    def max_song(song):
        return song[2]
    songs_copy = sorted(songs[1:], key = max_song, reverse = False)

    taken_songs = []
    cur_size = 0
    if songs[0][2] > max_size:
        return []
    else:
        taken_songs.append(songs[0][0])
        cur_size += songs[0][2]
        for song in songs_copy:
            if cur_size + song[2] <= max_size:
                taken_songs.append(song[0])
                cur_size += song[2]
            else:
                return taken_songs
        return taken_songs
    

def test_song_playlist(songs, max_size):
    print(song_playlist(songs, max_size))

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

for r in range(5):
    max_size = random.randint(10,13)
    print(f'loop # {r}, max_size = {max_size}')
    test_song_playlist(songs, max_size)