import unittest
import lab1
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests that the max_list_inter function in Lab1 returns the maximum of a list"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(lab1.max_list_iter([]), None)  # tests that an empty list returns None

        self.assertEqual(max_list_iter([1, 2, 3, 4, 5]), 5)  # tests one maximum in various locations
        self.assertEqual(max_list_iter([1, 2, 3, 5, 4]), 5)
        self.assertEqual(max_list_iter([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_list_iter([1, 5, 2, 3, 4]), 5)
        self.assertEqual(max_list_iter([5, 1, 2, 3, 4]), 5)

        self.assertEqual(max_list_iter([1, 1, 1, 1, 1]), 1)  # tests all values equal

        self.assertEqual(max_list_iter([9, 1, 1, 1, 1]), 9)  # tests multiple min values and 1 max
        self.assertEqual(max_list_iter([1, 9, 1, 1, 1]), 9)
        self.assertEqual(max_list_iter([1, 1, 9, 1, 1]), 9)
        self.assertEqual(max_list_iter([1, 1, 1, 9, 1]), 9)
        self.assertEqual(max_list_iter([1, 1, 1, 1, 9]), 9)

        self.assertEqual(max_list_iter([1, 9, 9, 9, 9]), 9)  # tests multiple max values and 1 min
        self.assertEqual(max_list_iter([9, 1, 9, 9, 9]), 9)
        self.assertEqual(max_list_iter([9, 9, 1, 9, 9]), 9)
        self.assertEqual(max_list_iter([9, 9, 9, 1, 9]), 9)
        self.assertEqual(max_list_iter([9, 9, 9, 9, 1]), 9)

    def test_reverse_rec(self):
        with self.assertRaises(ValueError):
            reverse_rec(None)
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([1]), [1])  # test one term

        self.assertEqual(reverse_rec([1, 1, 1]), [1, 1, 1])

        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])  # test odd number of terms
        self.assertEqual(reverse_rec([1, 2, 3, 4]), [4, 3, 2, 1])  # test even number of terms

        self.assertEqual(reverse_rec([5, 9, 0]), [0, 9, 5])  # unsymmetrical lists
        self.assertEqual(reverse_rec([1, 5, 9, 0]), [0, 9, 5, 1])

        self.assertEqual(reverse_rec([1, 2, 3, 3, 2, 1]), [1, 2, 3, 3, 2, 1])  # symmetrical lists
        self.assertEqual(reverse_rec([1, 2, 3, 2, 1]), [1, 2, 3, 2, 1])

    def test_bin_search(self):
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, None)

        list_val = [0, 1, 2, 3, 4, 7, 8, 9]  # even number of terms
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, low, high, list_val), 0)  # test first value
        self.assertEqual(bin_search(9, low, high, list_val), 7)  # test last value
        self.assertEqual(bin_search(2, low, high, list_val), 2)  # test value below center
        self.assertEqual(bin_search(7, low, high, list_val), 5)  # test value above center
        self.assertEqual(bin_search(11, low, high, list_val), None)

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]  # odd number of terms
        high += 1
        self.assertEqual(bin_search(0, low, high, list_val), 0)  # test first value
        self.assertEqual(bin_search(10, low, high, list_val), 8)  # test last value
        self.assertEqual(bin_search(2, low, high, list_val), 2)  # test value below center
        self.assertEqual(bin_search(7, low, high, list_val), 5)  # test value above center
        self.assertEqual(bin_search(4, low, high, list_val), 4)  # test center value
        self.assertEqual(bin_search(-1, low, high, list_val), None)

        with self.assertRaises(IndexError):
            bin_search(0, -1, high, list_val)
        # self.assertRaises(bin_search(-1, -1, high, list_val), IndexError)
        # self.assertRaises(bin_search(-1, low, 20, list_val), IndexError)


if __name__ == "__main__":
    unittest.main()
