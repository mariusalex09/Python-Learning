import unittest

class CheckList(unittest.TestCase):

    mylist = [1, 2, 3]

    def test_mylist(self):

        for i in self.mylist:
            with self.subTest(i=i):
                self.assertEqual(i%2, 0)


if __name__ == '__main__':
    unittest.main()
    x = unittest.TestResult


