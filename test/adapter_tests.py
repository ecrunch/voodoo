
import unittest

from src.adapters import JsonAdapter, TaskJsonAdapter
from src.classes import (
    Task, Exam, Project, Paper, Homework,
)



TASK_DB = "db/json/task/taskdb.json"
WANT_DB = "db/json/want/wantdb.json"
BREAK_DB = "db/json/break/breakdb.json"



class TestAdapters(unittest.TestCase):

    def setUp(self):
        self.tasks_from_file = TaskJsonAdapter(file_name = TASK_DB) 

    def tearDown(self):
        pass

    def test_data(self):
        print self.tasks_from_file.data



if __name__ == '__main__':
    unittest.main()
