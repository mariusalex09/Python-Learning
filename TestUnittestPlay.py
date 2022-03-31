import unittest
import sys


#@unittest.skip("Skippping whole class")
class TestTraining(unittest.TestCase):
    """this is a test class for training"""
    
    def setUp(self) -> None:
        print(f"Precondition performed.")
        return super().setUp()

    def calc_sum(self, a, b):
        return a + b
    
    
    @classmethod
    def setUpClass(cls) -> None:
        print(f"Preconditon at class level")
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        print(f"Cleanup at class level")
        return super().tearDownClass()


    #@unittest.skip("demonstrate skipping")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO1', f"Expected F001 and got {'foo'.upper()}")


    #@unittest.skipIf(sys.platform.startswith("win"), "requires Windows")
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_split(self):
        s = "Hello world"
        self.assertEqual(s.split(), ["Hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)


    def test_calc_sum(self):
        self.assertEqual(self.calc_sum(5, 10), 15)
        

    def tearDown(self) -> None:
        print(f"Cleanup performed.")
        return super().tearDown()


if __name__ == '__main__':
    #TestTraining.skipTest(TestTraining.test_calc_sum, reason="dsdasfa")
    print(sys.platform)
    unittest.main(verbosity=2)

    

