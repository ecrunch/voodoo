import time
import unittest
import sqlite3

from src.adapters import (
    JsonAdapter, TaskJsonAdapter, DbAdapter
    )
from src.classes import (
    Task, Exam, Project, Paper, Homework,
)



TASK_DB = "db/json/task/taskdb.json"
WANT_DB = "db/json/want/wantdb.json"
BREAK_DB = "db/json/break/breakdb.json"

SQLITE_DB = "db/test/example.db"

class TestAdapters(unittest.TestCase):

    def setUp(self):

        self.dbconn = sqlite3.connect(SQLITE_DB)
        self.db_adapter = DbAdapter(self.dbconn)


    def tearDown(self):
        self.dbconn.close()
        self.db_adapter = None



    def test_sequence(self):

        make = self.db_adapter._table_qry('stocks', ['date', 'trans', 'symbol'], ['text', 'text', 'text'])
        print(make)
        self.db_adapter._execute_qry(make)

        insert = self.db_adapter._insert_qry('stocks', ['a', 'b', 'c'])
        print(insert)
        self.db_adapter._execute_qry(insert)

        insert = self.db_adapter._insert_qry('stocks', ['d', 'e', 'f'])
        print(insert)
        self.db_adapter._execute_qry(insert)

        insert = self.db_adapter._insert_qry('stocks', ['g', 'h', 'i'])
        print(insert)
        self.db_adapter._execute_qry(insert)

        all = self.db_adapter._all_qry('stocks')
        print(all)
        res = self.db_adapter._execute_qry(all)
        print(res)

        drop = self.db_adapter._drop_qry('stocks')
        print(drop)
        self.db_adapter._execute_qry(drop)




if __name__ == '__main__':
    unittest.main()
