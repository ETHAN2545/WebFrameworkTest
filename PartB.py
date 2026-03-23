import unittest
from PartA import Artist, Song, Album, Playlist

class TestMusicClasses(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Taylor Swift", "13-12-1989", "USA")
        self.song1 = Song("All Too Well", "Taylor Swift", 2012)
        self.song2 = Song("Karma", "Taylor Swift", 2022)
        self.song3 = Song("Anti-Hero", "Taylor Swift", 2022)
        self.album = Album("Red", "Taylor Swift", 2012)
        self.playlist = Playlist("Taylor Swift Playlist")

    def test_artist_is_instance(self):
        self.assertIsInstance(self.artist, Artist)

    def test_song_is_instance(self):
        self.assertIsInstance(self.song1, Song)

    def test_album_is_instance(self):
        self.assertIsInstance(self.album, Album)

    def test_playlist_is_instance(self):
        self.assertIsInstance(self.playlist, Playlist)

    def test_artist_is_not_song(self):
        self.assertNotIsInstance(self.artist, Song)

    def test_song_is_not_album(self):
        self.assertNotIsInstance(self.song1, Album)

    def test_album_is_not_playlist(self):
        self.assertNotIsInstance(self.album, Playlist)

    def test_playlist_is_not_artist(self):
        self.assertNotIsInstance(self.playlist, Artist)

    def test_identical_objects(self):
        same_song = self.song1
        self.assertIs(self.song1, same_song)

    def test_similar_but_not_identical_objects(self):
        another_song = Song("All Too Well", "Taylor Swift", 2012)
        self.assertEqual(self.song1.title, another_song.title)
        self.assertEqual(self.song1.artist_name, another_song.artist_name)
        self.assertEqual(self.song1.year, another_song.year)
        self.assertIsNot(self.song1, another_song)

    def test_artist_add_album(self):
        self.artist.add_album(self.album)
        self.assertIn(self.album, self.artist.albums)

    def test_artist_add_song(self):
        self.artist.add_song(self.song1)
        self.assertIn(self.song1, self.artist.songs)

    def test_album_add_song(self):
        new_song = self.album.add_song("22", 2012)
        self.assertIn(new_song, self.album.songs)

    def test_playlist_add_song(self):
        self.playlist.add_song(self.song1)
        self.assertIn(self.song1, self.playlist.songs)

    def test_sort_playlist_ascending(self):
        self.playlist.add_song(self.song2)   
        self.playlist.add_song(self.song1)   
        self.playlist.sort_playlist("ASC")
        self.assertEqual(self.playlist.songs[0].title, "All Too Well")
        self.assertEqual(self.playlist.songs[1].title, "Karma")

    def test_sort_playlist_descending(self):
        self.playlist.add_song(self.song2)   
        self.playlist.add_song(self.song1)
        self.playlist.sort_playlist("DES")
        self.assertEqual(self.playlist.songs[0].title, "Karma")
        self.assertEqual(self.playlist.songs[1].title, "All Too Well")

    def test_shuffle_playlist(self):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song3)

        before_shuffle = len(self.playlist.songs)
        self.playlist.shuffle_playlist()
        after_shuffle = len(self.playlist.songs)

        self.assertEqual(before_shuffle, after_shuffle)

if __name__ == "__main__":
    unittest.main()
