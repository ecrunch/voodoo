

import json

from sqlalchemy import create_engine

from src.session_manager import SessionManager
from src.classes import(
    User, Task, Class, Assignment, Want, Break
)


#JSON_PATH = "json/user/users.json"
#JSON_PATH = "json/task/tasks.json"
#JSON_PATH = "json/want/wants.json"
#JSON_PATH = "json/break/breaks.json"

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
        elif self.data["class"] == "Want":
            self.load_wants()
        elif self.data["class"] == "Break":
            self.load_breaks()
        else:
            print("Not implemented yet")

    
    def load_users(self):
        for row in self.data["data"]:
            self.session.add(
                User(
                    name= row["name"], 
                    password= row["password"], 
                    age= row["age"]
                ),
                commit= True
            )


    def load_tasks(self):
        for row in self.data["data"]:
            self.session.add(
                Task(
                    description= row["description"], 
                    date_str= row["date_str"], 
                    total_minutes= row["total_minutes"], 
                    task_type= row["task_type"], 
                    user_id= row["user_id"]
                ),
                commit= True
            )


    def load_wants(self):
        for row in self.data["data"]:
            self.session.add(
                Want(
                    description= row["description"],
                    category= row["category"],
                    user_id= row["user_id"]
                ),
                commit= True
            )


    def load_breaks(self):
        for row in self.data["data"]:
            self.session.add(
                Break(
                    description= row["description"],
                    url= row["url"],
                    user_id= row["user_id"]
                ),
                commit= True
            )


def main():

    #global db shit
    engine = create_engine('sqlite:///db/data/sqlalchemy.db')
    session = SessionManager(engine)

    json_adapter = JsonAdapter(JSON_PATH, session)
    
    json_adapter.load()



main()





