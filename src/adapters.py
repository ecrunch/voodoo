

#
#
#   Class for extracting input
#       idea : a sort of API for 
#       dealing with the classes
#
#

import json
import sys
import datetime
import sqlite3


from src.classes import (
    Task, Exam, Project, Paper, Homework,
)



class DbAdapter(object):

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    # TODO : 
    # Write a sqlite db adapter 
    
    def read_task(self, task_id):
        pass

    def write_task(self, task):
        pass

    def print_all_tasks(self):
        pass 



class JsonAdapter(object):

    def __init__(self, file_name):
        
        self.file_name = file_name
        try:
            self.data = self._load_json_data(file_name)
        except:
            self.data = []

        if self.data:
            self.tasks = self._make_tasks()
        else:
            self.tasks = []


    def _load_json_data(self, file_name):

        with open(file_name) as f:
            d = json.load(f)
            return d


    def _make_tasks(self):

        tasks = []
        
        for item in self.data:
            
            name = item["name"]

            # MUST : convert from string to datetime
            d_datestr = item["due_date"]
            d_date = self._make_datetime(d_datestr)
            
            # SHOULD : make this more pythonic
            if item["type"] == "Exam":
                tasks.append(Exam(name, d_date))
            elif item["type"] == "Project":
                tasks.append(Project(name, d_date))
            elif item["type"] == "Paper":
                tasks.append(Paper(name, d_date))
            elif item["type"] == "Homework":
                tasks.append(Homework(name, d_date))
            #other wise it is just a general task
            else:
                tasks.append(Task(name, d_date))

        return tasks

    def _make_datetime(self, datestr):
        return datetime.datetime.strptime(datestr, "%Y%m%d")
        
        
        
    def print_data(self):
        for item in self.data:
            print(item)

    def print_tasks(self):
        for task in self.tasks:

            print("|--------------------------->")
            print("| Name : %s\n| Due Date : %s\n| Score : %s" % (
                task.name, task.due_date.strftime("%Y%m%d"),
                task.get_score()))
            print("|--------------------------->")

