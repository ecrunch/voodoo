




import unittest

from src.classes import Task



class TestTaskClass(unittest.TestCase):

    def setUp(self):
        self.task_one = Task(user= None)

    def tearDown(self):
        pass

    # TODO : name something more clever
    def testOne(self):
        print(self.task_one)




# this function is the thing that runs the tests
if __name__ == '__main__':
    unittest.main()  ## <-- 'main' referring to the function that python initial calls when script is launched




