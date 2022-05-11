from unittest import result
import TestUnittestPlay
import unittest


def suite():
    suite = unittest.TestSuite()
    #suite.addTest(TestUnittestPlay.TestTraining('test_calc_sum'))
    #suite.addTest(TestUnittestPlay.TestTraining('test_upper'))
    suite.addTests(unittest.makeSuite(TestUnittestPlay.TestTraining))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
    #unittest.main()


"""Nice approach for creating suite from source https://stackoverflow.com/questions/3156782/how-to-add-dozen-of-test-cases-to-a-test-suite-automatically-in-python
import os, unittest

class Tests():   

    def suite(self): #Function stores all the modules to be tested


        modules_to_test = []
        test_dir = os.listdir('.')
        for test in test_dir:
            if test.startswith('test') and test.endswith('.py'):
                modules_to_test.append(test.rstrip('.py'))

        alltests = unittest.TestSuite()
        for module in map(__import__, modules_to_test):
            module.testvars = ["variables you want to pass through"]
            alltests.addTest(unittest.findTestCases(module))
        return alltests

if __name__ == '__main__':
    MyTests = Tests()
    unittest.main(defaultTest='MyTests.suite')

#If you want to add results to a log file add this at the end instead:

if __name__ == '__main__':
    MyTests = Tests()
    log_file = 'log_file.txt'
    f = open(log_file, "w") 
    runner = unittest.TextTestRunner(f)
    unittest.main(defaultTest='MyTests.suite', testRunner=runner)

#Also at the bottom of the modules you are testing place code like this:

class SomeTestSuite(unittest.TestSuite):

    # Tests to be tested by test suite
    def makeRemoveAudioSource():
        suite = unittest.TestSuite()
        suite.AddTest(TestSomething("TestSomeClass"))

        return suite

    def suite():
        return unittest.makeSuite(TestSomething)

if __name__ == '__main__':
    unittest.main()
"""