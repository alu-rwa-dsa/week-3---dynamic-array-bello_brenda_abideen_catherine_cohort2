import unittest
from DSA_Wk3_Q4 import asso_list


class TestQuestion4(unittest.TestCase):
    def testfirst(self):
        p = asso_list()
        self.assertEqual(p.add("onename", 89, "IBT", "UK"), {'name': 'onename', 'age': 89, 'major': 'IBT', 'country': 'UK'})

    def testsecond(self):
        p = asso_list()
        p.add("onename", 89, "IBT", "UK")
        self.assertEqual(p.a_remove("age"), {'name': 'onename', 'major': 'IBT', 'country': 'UK'})

    def testthird(self):
        p = asso_list()
        p.add("onename", 89, "IBT", "UK")
        self.assertEqual(p.a_modify("onename2", "CS", "US"), {'name': 'onename2', 'age' : 89, 'major': 'CS', 'country': 'US'})

    def testfourth(self):
        p = asso_list()
        p.add("onename", 89, "IBT", "UK")
        self.assertEqual(p.a_lookup("age"), "not found")


    if __name__ == "__main__":
        unittest.main()
