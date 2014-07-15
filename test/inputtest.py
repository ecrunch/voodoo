
import unittest

from src.input import Extractor
from src.classes import (
    Task, Exam, Project, Paper, Homework,
)



TEST_DATA_1 = "test/test_data/test_data_one.json"
extracter = Extractor(file_name=TEST_DATA_1)

#FAKE_DATA_1 = "test/test_data/not_real"
#extracter = Extractor(file_name=FAKE_DATA_1)

extracter.print_tasks()


class TestExtractor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
