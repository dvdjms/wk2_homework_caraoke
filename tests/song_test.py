import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestSong(unittest.TestCase):
   
    def setUp(self):
        self.song_01 = Song("Bat Out of Hell")
        self.song_02 = Song("Born to Run")
        self.song_03 = Song("Over the Rainbow")
        self.song_04 = Song("Jump")
        self.song_05 = Song("Bat Out of Hell")

    def test_song_has_name(self):
        self.assertEqual("Born to Run", self.song_02.name)

