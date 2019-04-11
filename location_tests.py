import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = None
        self.assertEqual(repr(loc), 'None')  # checks that a location with no information returns None

        # checks several locations
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), 'SLO, Latitude:35.3, Longitude:-120.7')
        loc = Location("Los Angelos", 34.052, -118.243)
        self.assertEqual(repr(loc), 'Los Angelos, Latitude:34.052, Longitude:-118.243')
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc), 'Paris, Latitude:48.9, Longitude:2.4')

        # tests a change in reference
        loc1 = loc
        self.assertEqual(repr(loc1), repr(loc))
        self.assertEqual(repr(loc1), 'Paris, Latitude:48.9, Longitude:2.4')


if __name__ == "__main__":
    unittest.main()
