


#
#
#   Tests for task class
#   currently located at src/classes, about halfway down the file
#
#


import unittest
import datetime

from src.classes import Task



class TestTaskClass(unittest.TestCase):

    def setUp(self):
         
        today = datetime.datetime.today()
        days_away = 11  ## <-- what happens to the score if the days is less than 11....?
        due_date = today + datetime.timedelta(days= days_away)
        date_str = datetime.datetime.strftime(due_date, "%Y/%m/%d")

        self.exam_basic = Task(total_minutes = 0, task_type= 'Exam', date_str= date_str)
        self.paper_basic = Task(total_minutes = 0, task_type= 'Paper', date_str= date_str)
        self.project_basic = Task(total_minutes = 0, task_type= 'Project', date_str= date_str)
        self.homework_basic = Task(total_minutes = 0, task_type= 'Homework', date_str= date_str)

    def tearDown(self):
        self.exam_one = None  ## <-- resets after every test
        self.paper_basic = None
        self.project_basic = None
        self.homework_basic = None


    # tests the starting scores 
    def testBaseScores(self):
        self.assertEqual(self.exam_basic.get_score(), 5)
        self.assertEqual(self.paper_basic.get_score(), 4)
        self.assertEqual(self.project_basic.get_score(), 4)
        self.assertEqual(self.homework_basic.get_score(), 3)




# this function is the thing that runs the tests
if __name__ == '__main__':
    unittest.main()  ## <-- 'main' referring to the function that python initial calls when script is launched




