import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestRoom(unittest.TestCase):
   
    def setUp(self): # Arrange

        self.room_1 = Room("Room_1", 0.00, 5000.00)
        self.room_2 = Room("Room_2", 0.00, 5000.00)
        self.room_3 = Room("Room_3", 0.00, 5000.00)

    def test_room_has_name(self):
        self.assertEqual("Room_1", self.room_1.name)

    def test_add_guest_to_room(self):
        guest = Guest("John", 100.00, "Bat out of hell")
        self.room_1.add_guest_to_room(guest)
        self.assertEqual(3, self.room_1.count_guests())

    def test_remove_guest_from_room(self):
        guest = "guest2"
        self.room_1.remove_guest_from_room(guest)
        self.assertEqual(1, self.room_1.count_guests())

    def test_add_song_to_room(self):
        song = Song("Over the Rainbow")
        self.room_2.add_song_to_room(song)
        self.assertEqual(1, self.room_2.count_songs())

    def test_enough_capacity_in_room(self):
        self.assertEqual("Enough space", self.room_3.enough_capacity_in_room(3))

    def test_not_enough_capacity_in_room(self):
        self.assertEqual("Not enough space", self.room_3.enough_capacity_in_room(7))

    def test_guest_can_afford_entry(self):
        guest = Guest("Jane", 50.00, "Over the Rainbow")
        self.assertEqual("Guest can afford", self.room_3.can_guest_afford_entry(guest.wallet))

    def test_guest_can_not_afford_entry(self):
        guest = Guest("Julie", 20.00, "Jump")
        self.assertEqual("Guest can not afford", self.room_3.can_guest_afford_entry(guest.wallet))

    def test_add_money_to_cash(self):
        self.room_2.add_money_to_cash(1000)
        self.assertEqual(6000, self.room_2.cash)

    def test_guest_pays_entry(self):
        guest = Guest("Jane", 50.00, "Over the Rainbow")
        self.room_3.guest_pays_entry(guest)
        self.assertEqual(25, guest.wallet)
        self.assertEqual(5025, self.room_3.cash)
        self.assertEqual(3, self.room_3.count_guests())

    def test_guests_favourite_song_on_playlist(self):
        guest = Guest("Jack", 100.00, "Born to Run")
        self.assertEqual("Whoo!", self.room_2.guests_favourite_song(guest))

    def test_guests_favourite_song_not_on_playlist(self):
        guest = Guest("Joshua", 45.00, "Jam")
        self.assertEqual("Boo!", self.room_3.guests_favourite_song(guest))

    def test_guests_tab(self):
        guest = Guest("Jane", 50.00, "Over the Rainbow")
        drink = Bar("Beer", 4.50)
        self.room_3.guests_tab(guest, drink)
        self.assertEqual(20.50, guest.wallet)
        self.assertEqual(29.50, self.room_3.tab)
        self.assertEqual(5029.50, self.room_3.cash)









