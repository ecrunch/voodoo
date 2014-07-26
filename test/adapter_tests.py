
import unittest

from src.adapters import (
    JsonAdapter, TaskJsonAdapter, DbAdapter
    )
from src.classes import (
    Task, Exam, Project, Paper, Homework,
)



TASK_DB = "db/json/task/taskdb.json"
WANT_DB = "db/json/want/wantdb.json"
BREAK_DB = "db/json/break/breakdb.json"

SQLITE_DB = "db/example.db"

class TestAdapters(unittest.TestCase):

    def setUp(self):
        self.db = DbAdapter(SQLITE_DB)


    def tearDown(self):
        pass

    def test_data(self):
        pass


if __name__ == '__main__':
    unittest.main()
