

import json

from sqlalchemy import create_engine

from src.session_manager import SessionManager
from src.users import User
from src.tasks import Task
from src.wants import Want
from src.breaks import Break
from src.classes import Class



JSON_PATH = "db/json/user/users.json"

class JsonAdapter(object):

    def __init__(self, json_path, session, data= None):        
        self.data = self._build_data(json_path)
        self.session = session
        

    def _build_data(self, json_path):
        with open(json_path) as data_file:
            return json.load(data_file)



    def load(self):

        if self.data["class"] == "User":
            self.load_users()
        elif self.data["class"] == "Task":
            self.load_tasks()
        else:
            print("Not implemented yet")


    
    def load_users(self):
        for row in self.data["data"]:
            self.session.add(
                User(row["name"], row["password"], row["age"]),
                commit= True
            )


    def load_tasks(self):
        for row in self.data["data"]:
            self.session.add(
                Task(
                    row["description"], row["date_str"], row["total_minutes"], row["class_id"], row["task_type"], row["user_id"]
                ),
                commit= True
            )


def main():

    #global db shit
    engine = create_engine('sqlite:///db/data/sqlalchemy.db')
    session = SessionManager(engine)

    json_adapter = JsonAdapter(JSON_PATH, session)
    
    json_adapter.load_users()



#main()





