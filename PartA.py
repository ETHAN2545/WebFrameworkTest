import random

class Artist:
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def display_info(self):
        print("=" * 40)
        print("Artist:", self.name)
        print("Born:", self.dob)
        print("Country:", self.country)
        print("=" * 40)
        
        print("Album list:")
        for album in self.albums:
            print(album.title)
        print("Song list:")
        for song in self.songs:
            print(song.title)
        print("=" * 40)


class Song:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year

    def display_info(self):
        print(f"Song: {self.title}")
        print(f"Artist: {self.artist_name}")
        print(f"Released: {self.year}")
        print("=" * 40)


class Album:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = []

    def add_song(self, title, year):
        song = Song(title, self.artist_name, year)
        self.songs.append(song)
        return song

    def display_info(self):
        print("Album:", self.title)
        print("By:", self.artist_name)
        print("Year:", self.year)
        print("Tracks:")
        for song in self.songs:
            print(f"{song.title} [{song.year}]")
        print("=" * 40)


class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_songs(self):
        print("Playlist Name:", self.title)
        
        if len(self.songs) == 0:
            print("No songs added yet.")
        else:
            for index, song in enumerate(self.songs, start=1):
                print(f"  {index}) {song.title} - {song.artist_name} ({song.year})")
        print("=" * 40)

    def sort_playlist(self, order="ASC"):
        if order == "DES":
            self.songs.sort(key=lambda x: x.title, reverse=True)
        else:
            self.songs.sort(key=lambda x: x.title)

    def shuffle_playlist(self):
        random.shuffle(self.songs)


if __name__ == "__main__":
    artist = Artist("Taylor Swift", "13-12-1989", "USA")

    album_red = Album("Red", artist.name, 2012)
    album_midnights = Album("Midnights", artist.name, 2022)

    s1 = Song("All Too Well", artist.name, 2012)
    s2 = Song("22", artist.name, 2012)
    s3 = Song("Anti-Hero", artist.name, 2022)
    s4 = Song("Karma", artist.name, 2022)

    album_red.add_song("I Knew You Were Trouble", 2012)
    album_red.add_song("We Are Never Ever Getting Back Together", 2012)

    album_midnights.add_song("Lavender Haze", 2022)
    album_midnights.add_song("Bejeweled", 2022)

    artist.add_album(album_red)
    artist.add_album(album_midnights)

    artist.add_song(s1)
    artist.add_song(s2)
    artist.add_song(s3)
    artist.add_song(s4)

    artist.display_info()
    album_red.display_info()
    album_midnights.display_info()
    s1.display_info()

    playlist = Playlist("Taylor Swift Playlist")

    for song in album_red.songs:
        playlist.add_song(song)

    for song in album_midnights.songs:
        playlist.add_song(song)

    playlist.add_song(s1)
    playlist.add_song(s3)

    print("Original Playlist:")
    playlist.print_all_songs()

    playlist.sort_playlist("ASC")
    print("Sorted (Ascending):")
    playlist.print_all_songs()

    playlist.sort_playlist("DES")
    print("Sorted (Descending):")
    playlist.print_all_songs()

    playlist.shuffle_playlist()
    print("Shuffled Playlist:")
    playlist.print_all_songs()
