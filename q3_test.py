import unittest as ut
from Question3 import *

class TestQuestion2(ut.TestCase):
    def test_contains(self):
        arr = Third([1, 2, 3, 4, 5, 6])
        self.assertNotEqual(arr.contains(5),False)

    def test_reverse(self):
        arr = Third([1, 2, 3, 4, 5, 6])
        arr2 = arr.reverse()
        self.assertNotEqual(arr,arr2)




if __name__ == "__main__":
    ut.main()
