
import unittest

from src.adapters import JsonAdapter, DbAdapter
from src.classes import (
    Task, Exam, Project, Paper, Homework,
)



TEST_DATA_1 = "db/json/test_data_one.json"
adapter = JsonAdapter(file_name=TEST_DATA_1)

#FAKE_DATA_1 = "test/test_data/not_real"
#adapter = JsonAdapter(file_name=FAKE_DATA_1)

adapter.print_tasks()


class TestAdapter(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
