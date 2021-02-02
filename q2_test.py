import unittest as ut
from Question2 import *

class TestQuestion2(ut.TestCase):
    def testfirst(self):
        Array1 = DyArray([1,3,5,6])
        arr2 = [1, 3, 5, 6]
        self.assertNotEqual(Array1, arr2)

    def testsecond(self):
        Array = DyArray([1, 3, 5, 6])
        self.assertEqual(Array.add(7), [1, 3, 5, 6, 7])

    def testthird(self):
        Array3 = DyArray([1, 4])
        self.assertEqual(Array3.delete(), [1])



if __name__ == "__main__":
    ut.main()
