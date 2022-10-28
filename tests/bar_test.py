import unittest
from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestBar(unittest.TestCase):
   
    def setUp(self): 
        self.drink_1 = Bar("Beer", 4.50)
        self.drink_2 = Bar("Wine", 5.50)
        self.drink_3 = Bar("Cocktail", 9.00)
        self.drink_4 = Bar("Water", 2.50)

    def test_drink_has_name(self):
        self.assertEqual("Wine", self.drink_2.name)


