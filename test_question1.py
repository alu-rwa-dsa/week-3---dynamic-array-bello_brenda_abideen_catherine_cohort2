import unittest
from question1 import Array


class MyTestCase(unittest.TestCase):
    def test_size(self):
        x = Array(8, [1,2,3,4,5])
        self.assertEqual(x.size, 8)

    def test_values(self):
        x = Array(8, [1,2,3,4,5])
        self.assertEqual(x.values, [1,2,3,4,5])

    def test_defaultvalue(self):
        x = Array(8, [1,2,3,4,5])
        self.assertIsNone(x.elements[6], x.elements[6] == None)

    def test_sizetype(self):
        x = Array(8, [1,2,3,4,5])
        self.assertRaises(TypeError, x.size,"g")

    def test_valuetype(self):
        x = Array(8, [1,2,3,4,5])
        self.assertRaises(TypeError, x.elements,'j')

    def test_get(self):
        x = Array(8, [1,2,3,4,5])
        self.assertEqual(x.get(4), 5)

    def test_get_correctindex(self):
        x = Array(8, [1,2,3,4,5])
        self.assertRaises(TypeError, x.get(10))

    def test_length(self):
        x = Array(20000, list(range(0,10001)))
        self.assertEqual(x.length(),10000)

    def test_set(self):
        x = Array(8, [1, 2, 3, 4, 5])
        x.set(6,3)
        self.assertEqual(x.get(3),6)

    def test_set_correctindex(self):
        x = Array(8, [1, 2, 3, 4, 5])
        self.assertRaises(TypeError, x.set(6,10))



if __name__ == '__main__':
    unittest.main()
