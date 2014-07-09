
import unittest
import datetime

from src.classes import (
    Task,
    Exam, Project, Paper, Homework,
    MockDB,
    Scheduler,
    )


class TestMockDb(unittest.TestCase):

    def setUp(self):
        self.db = MockDB()

    def tearDown(self):
        self.db = None
    
    def test_save_task(self):

        # save a task
        task_1 = Task()
        self.db.save(task_1)

        # confirm various things
        self.assertTrue(task_1 in self.db.contents)


class TestTaskClass(unittest.TestCase):

    def setUp(self):

        self.db = MockDB()

        # datetime objects representing dates in the future
        today = datetime.datetime.today()
        three_days = today + datetime.timedelta(days=3)
        seven_days = today + datetime.timedelta(days=7)

        # fake task one
        self.hw = Homework('Science Paper', three_days)
        self.exam = Exam('Science Test', seven_days)

        # save tasks to mock db
        self.db.save(self.exam)
        self.db.save(self.hw)
        

    def tearDown(self):
        self.db = None
        self.exam = None
        self.hw = None


    def test_hw(self):
        self.assertEqual(self.hw.base_score, 3)

    def test_exam(self):
        self.assertEqual(self.exam.base_score, 5)


    def test_get_days_remaining(self):
        expected_delta = self.exam.due_date.day - self.exam.start_date.day
        actual_delta = self.exam._get_days_remaining()
        self.assertEqual(expected_delta, actual_delta)


    def test_add_days_to_due_date(self):

        self.assertEqual(self.exam._get_days_remaining(), 7)
        self.exam.add_days_to_due_date(2)
        self.assertEqual(self.exam._get_days_remaining(), 9)
        
        
    def test_get_score(self):

        # before we add any days, first day
        score = self.exam.get_score()
        self.assertEqual(score, 8)

        # extend 
        self.exam.add_days_to_due_date(2)
        score_after = self.exam.get_score()
        self.assertEqual(score_after, 6)

        # add 2 more days ( now 11 days out )
        self.exam.add_days_to_due_date(2)
        score_after = self.exam.get_score()
        self.assertEqual(score_after, 5)
        pass
    
class TestSchedulerClass(unittest.TestCase):

    def setUp(self):

        two_days = datetime.datetime.today() + datetime.timedelta(days=2)
        three_days = datetime.datetime.today() + datetime.timedelta(days=3)
        five_days = datetime.datetime.today() + datetime.timedelta(days=5)
        seven_days = datetime.datetime.today() + datetime.timedelta(days=7)

        self.exam = Exam('Test Exam', seven_days)
        self.project = Project('Test Project', five_days)
        self.paper = Paper('Test Paper', three_days)
        self.homework = Homework('Test Homework', two_days)

        self.db = MockDB()
        self.db.save(self.exam)
        self.db.save(self.project)
        self.db.save(self.paper)
        self.db.save(self.homework)
        
        self.scheduler = Scheduler(self.db)
        

    def tearDown(self):
        self.scheduler = None
        

    def test_task_list(self):

        self.assertTrue(self.exam in self.scheduler.task_list)
        self.assertTrue(self.project in self.scheduler.task_list)
        self.assertTrue(self.paper in self.scheduler.task_list)
        self.assertTrue(self.homework in self.scheduler.task_list)

        self.assertEqual(self.scheduler.score_total, 34)


    def test_print_all_scores(self):
        #self.scheduler.print_all_scores()
        pass

    def test_get_mean(self):
        actual_mean = self.scheduler.get_mean()
        expected_mean = 8.5
        self.assertEqual(actual_mean, expected_mean)


    # MAY : come back and fix the test so that the decimal goes
    # out to like 5 or so digits, rather than just flooring it
    def test_variance(self):
        actual_variance = int(self.scheduler.get_variance())
        expected_variance = 4
        self.assertEqual(actual_variance, expected_variance)

    # MAY : same
    def test_standard_dev(self):

        actual_standard_dev = int(self.scheduler.get_standard_dev())
        expected_standard_dev = 2
        self.assertEqual(actual_standard_dev, expected_standard_dev)

    def test_nom_dists(self):
        #print (self.scheduler.nom_dists)
        pass

    def get_percentile(score):
        pass

if __name__ == '__main__':
    unittest.main()


