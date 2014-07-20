

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


from src.classes import (
    Task, Exam, Project, Paper, Homework,
)




# Multi purpose adapter class that can accept a json struct
# or a json file

class JsonAdapter(object):

    def __init__(self, data=None, file_name=None):
        
        # we don't have a json struct
        if data is None:
            
            # we have a file name
            if file_name:
                
                try:
                    self.data = self._load_json_from_file(file_name)
                except:
                    self.data = []


            # data is []
            else:
                self.data = []

        # use the default data
        else:
            self.data = data



    def _load_json_from_file(self, file_name):

        with open(file_name) as f:
            d = json.load(f)
            return d





class TaskJsonAdapter(JsonAdapter):

    def __init__(self, data = None, file_name = None):
        JsonAdapter.__init__(self, data = data, file_name = file_name)
        self.items = self._make_tasks()

    def _make_tasks(self):

        tasks = []
      
        for item in self.data:
            
            name = item["description"]

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


    def print_items(self):
        for task in self.items:

            print("|--------------------------->")
            print("| Name : %s\n| Due Date : %s\n| Score : %s" % (
                task.name, task.due_date.strftime("%Y%m%d"),
                task.get_score()))
            print("|--------------------------->")



class WantJsonAdapter(JsonAdapter):
 
    def __init__(self, data = None, file_name = None):
        JsonAdapter.__init__(self, data = data, file_name = file_name)
        self.items = self._make_wants()


    def _make_wants(self):

        wants = []
        for item in self.data:
            description = item["description"]
            category = item["category"]
            wants.append({"description" : description, "category" : category}) 
        return wants 
        
    def print_data(self):
        for item in self.data:
            print(item)

    def print_items(self):
        for want in self.items:
            print("|--------------------------->")
            print("| Desciption : %s\n| Category : %s" % (want["description"], want["category"]))
            print("|--------------------------->")



class BreakJsonAdapter(JsonAdapter):


    def __init__(self, data = None, file_name = None):
        JsonAdapter.__init__(self, data = data, file_name = file_name)
        self.items = self._make_breaks()
    
    
    def _make_breaks(self):

        breaks = []
        for item in self.data:
            description = item["description"]
            breaks.append({"description" : description}) 
        return breaks
        
    def print_data(self):
        for item in self.data:
            print(item)
        return

    def print_items(self):
        
        for _break in self.items:
            print("|--------------------------->")
            print("| Description : %s" % _break["description"])
            print("|--------------------------->")



