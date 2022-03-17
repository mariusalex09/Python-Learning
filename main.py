import unittest

class TestTraining(unittest.TestCase):

    def calc_sum(self, a, b):
        return a + b


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO1')


    def test_split(self):
        s = "Hello world"
        self.assertEqual(s.split(), ["Hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)


    def test_calc_sum(self):
        self.assertAlmostEqual(self.calc_sum(5, 10), 15)


    


if __name__ == '__main__':
    unittest.main()
