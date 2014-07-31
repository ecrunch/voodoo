import time
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
        self.db_adapter = DbAdapter(SQLITE_DB)


    def tearDown(self):
        pass        



    def test_start(self): 
        
        make = self.db_adapter._table_qry('stocks', ['date', 'trans', 'symbol'], ['text', 'text', 'text'])
        print(make)
        self.db_adapter._execute_qry(make)


    #def test_insert(self):
    
        insert = self.db_adapter._insert_qry('stocks', ['a', 'b', 'c'])
        print(insert)
        self.db_adapter._execute_qry(insert)


    def test_drop(self):
        drop = self.db_adapter._drop_qry('stocks')
        print(drop)
        self.db_adapter._execute_qry(drop)




if __name__ == '__main__':
    unittest.main()
