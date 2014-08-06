

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
import logging


from src.classes import (
    Task, Exam, Project, Paper, Homework,
)


class DbAdapter(object):

    def __init__(self, dbconn):
        self.dbconn = dbconn
    
     
    def make_table(self, table_name, fields, types):

        qry = self._table_qry(table_name, fields, types)
        self._execute_qry(qry)
   
   
    def insert_row(self, table_name, values):
        
        qry = self._insert_qry(table_name, values)
        self._execute_qry(qry)
    
   
    def get_all(self, table_name):

        qry = self._all_qry(table_name)
        return self._execute_qry(qry)

    def delete_table(self, table_name):

        qry = self._drop_qry(table_name)
        self._execute_qry(qry)


    def _execute_qry(self, qry):


        c = self.dbconn.cursor()
        c.execute(qry)
        res = c.fetchall()

        #saves
        self.dbconn.commit()

        return res


    def _table_qry(self, table_name, names, types):

        qry_str = "CREATE TABLE %s (" % table_name
        index = 0
        for i in range(0, len(names)):
            qry_str = qry_str + "%s %s, " % (names[index], types[index])
            index = index + 1

        return qry_str[:-2] + ")"


    def _insert_qry(self, table_name, values):

        qry_str = "INSERT INTO " + table_name + " VALUES ("

        index = 0
        for i in range(0, len(values)):
            qry_str = qry_str + "'%s', " % values[index]
            index = index + 1

        return qry_str[:-2] + ")"


    def _all_qry(self, table_name):
        return "SELECT * FROM %s" % table_name


    def _drop_qry(self, table_name):
        return "DROP TABLE %s" % table_name



class TaskDbAdapter(DbAdapter):

    def __init__(self, dbconn):
        DbAdapter.__init__(self, dbconn)
        self.items = self._get_all_tasks()


    # private method that builds the objects
    def _get_all_tasks(self):
        results = self.get_all('tasks')

        tasks = []

        for result in results:

            user = str(result[0])
            description = str(result[1])
            date_string = str(result[2])
            due_date = self._make_datetime(date_string)
            t_type = str(result[3])
            #total_minutes = int(result[4])
            total_minutes = result[4]


            if t_type == 'Exam':
                tasks.append(Exam(description, due_date, total_minutes))
            elif t_type == 'Paper':
                tasks.append(Paper(description, due_date, total_minutes))
            elif t_type == 'Project':
                tasks.append(Project(description, due_date, total_minutes))
            elif t_type == 'Homework':
                tasks.append(Homework(description, due_date, total_minutes))
            else:
                tasks.append(Task(description, due_date, total_minutes))

        return tasks

    # public method
    def get_all_tasks(self):
        results = self.get_all('tasks')
        return results

    def _make_datetime(self, datestr):
        return datetime.datetime.strptime(datestr, "%Y%m%d")

    def get_ith_item(self, index):
        
        task = self.items[index]
       
        print("total_minutes = %s" % total_minutes)
        
        task_struct = {
            "class" : "Task",
            "type" : str(type(task)),
            "description" : task.name,
            "due_date" : str(task.due_date),
            "score" : task.get_score(),
            "total_minutes" : task.total_minutes
        } 

        return task_struct             


class WantDbAdapter(DbAdapter):

    def __init__(self, dbconn):
        DbAdapter.__init__(self, dbconn)
        self.items = self._get_all_wants()

    #private method that builds the objects
    def _get_all_wants(self):

        results = self.get_all('wants')
        wants = []
        for result in results:
            user = result[0]
            description = result[1]
            category = result[2]
            wants.append({"description" : description, "category" : category}) 
        return wants 

    # public method
    def get_all_wants(self):
        results = self.get_all('wants')
        return results

    def get_ith_item(self, index):
        
        want = self.items[index]
        
        want_struct = {
            "class" : "Want",
            "description" : want["description"],
            "category" : want["category"]
        } 

        return want_struct             


class BreakDbAdapter(DbAdapter):

    def __init__(self, dbconn):
        DbAdapter.__init__(self, dbconn)
        self.items = self._get_all_breaks()

    #private method that builds the objects
    def _get_all_breaks(self):

        results = self.get_all('breaks')
        breaks = []
        for result in results:
            user = result[0]
            description = result[1]
            url = result[2]
            breaks.append({"description" : description, "url" : url}) 
        return breaks 

    def get_all_breaks(self):

        results = self.get_all('breaks')
        return results

    # gets a randomized json form for the index
    # passed in
    def get_ith_item(self, index):
        
        _break = self.items[index]
        
        break_struct = {
            "class" : "Break",
            "description" : _break["description"],
            "url" : _break["url"]
        } 

        return break_struct             

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


    # gets a randomized json form for the index
    # passed in
    def get_ith_item(self, index):
        
        task = self.items[index]
        
        task_struct = {
            "class" : "Task",
            "type" : str(type(task)),
            "description" : task.name,
            "due_date" : str(task.due_date),
            "score" : task.get_score()
        } 

        return task_struct             


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

    # gets a randomized json form for the index
    # passed in
    def get_ith_item(self, index):
        
        want = self.items[index]
        
        want_struct = {
            "class" : "Want",
            "description" : want["description"],
            "category" : want["category"]
        } 

        return want_struct             
    
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
            
            if item["url"]:
                url = item["url"]
            else:
                url = "N/A"
            breaks.append({"description" : description, "url" : url}) 
        return breaks
        
    def print_data(self):
        for item in self.data:
            print(item)
        return

    # gets a randomized json form for the index
    # passed in
    def get_ith_item(self, index):
        
        _break = self.items[index]
        
        break_struct = {
            "class" : "Break",
            "description" : _break["description"],
            "url" : _break["url"]
        } 

        return break_struct             
    
    def print_items(self):
        
        for _break in self.items:
            print("|--------------------------->")
            print("| Description : %s" % _break["description"])
            print("|--------------------------->")



