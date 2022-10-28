import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", 100.00, "Bat out of hell")
        self.guest_2 = Guest("Jane", 50.00, "Over the Rainbow")
        self.guest_3 = Guest("Jack", 100.00, "Born to Run")
        self.guest_4 = Guest("Julie", 20.00, "Jump")
        self.guest_5 = Guest("Joshua", 45.00, "Jam")

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest_3.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Jump", self.guest_4.favourite_song)


   

