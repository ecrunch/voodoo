
import random

import logging

from src.generator import TimeSlotGenerator
from src.scorer import Scorer
from src.adapters import (
    JsonAdapter, TaskJsonAdapter, WantJsonAdapter, BreakJsonAdapter
    )


# defaults
WANT_DB = "db/json/want/wantdb.json"
TASK_DB = "db/json/task/taskdb.json"
BREAK_DB = "db/json/break/breakdb.json"



class Scheduler(object):

    def __init__(self, hours, 
            taskdb=TASK_DB, wantdb=WANT_DB, breakdb=BREAK_DB):
        
        
        self.hours = hours
        self.generator = TimeSlotGenerator(hours)
       
        self.task_adapter = TaskJsonAdapter(file_name = taskdb)
        self.want_adapter = WantJsonAdapter(file_name = wantdb)
        self.break_adapter = BreakJsonAdapter(file_name = breakdb)


        self.scorer = Scorer(db= None, tasks= self.task_adapter.items)

        self.e_index = 0
        self.n_index = 0
        self.nt_index = 0

        self.e_items = []
        self.n_items = []
        self.nt_items = []

        # fill the items in
        self._fill_items() 


        self.schedule = self.make_schedule()
   
 
 
    def _fill_items(self):
 
        for task in self.task_adapter.items:
            
            placement = self.scorer.get_placement(task)
    
            if placement == 'E':
                self.e_items.append(task)
            
            elif placement == 'N':
                self.n_items.append(task)

            elif placement == 'NT':
                self.nt_items.append(task)
 
            else:
                pass

 
  
    def _reset_index(self): 
        self.e_index = 0
        self.n_index = 0
        self.nt_index = 0
        return
   
    
    def make_schedule(self, repeat_items=True):
        
        schedule = []
        time_slots = self.generator.time_slots
        
        chosen_item_list = self.e_items
        chosen_index = self.e_index

        number = 1


        for slot in time_slots:
           
            #breaks get 15 min slots
            if slot == 15:

                print("A break")
                number_items = len(self.break_adapter.items)
                random_int = random.randint(0, number_items-1)
                schedule.append({"number" : number, "timeslot" : slot, "item" : self.break_adapter.get_ith_json(random_int)})

            #a want or task
            else:
                random_int = random.randint(1,2)
                
                # a want
                if random_int == 1:

                    print("A want")
                    number_items = len(self.want_adapter.items)
                    random_int = random.randint(0, number_items-1)
                    schedule.append({"number" : number, "timeslot" : slot, "item" : self.want_adapter.get_ith_json(random_int)})

                # a task
                else:
          
                    print("A task")          
                    
                    if self.e_index < len(self.e_items):
                        print("Item in I bucket")
                        chosen_item_list = self.e_items
                        chosen_index = self.e_index
                        self.e_index = self.e_index + 1
                    else:
                        if self.n_index < len(self.n_items): 
                            print("Item in G bucket")
                            chosen_item_list = self.n_items
                            chosen_index = self.n_index
                            self.n_index = self.n_index + 1
                        else:
                            # we will need to reset or quit
                            if repeat_items:                 
                                print("Resetting buckets")
                                self._reset_index()
                                #starts off with the first thing of the most recent list
                                chosen_index = 0
                            else:
                                #return schedule
                                pass
                    
                    
                    task = chosen_item_list[chosen_index]
                    placement = self.scorer.get_placement(task)
                   
                    task_struct = {
                        "class" : "Task",
                        "type" : str(type(task)),
                        "description" : task.name,
                        "due_date" : str(task.due_date),
                        "score" : task.get_score(),
                        "placement" : placement      
                    } 
                    schedule.append({"number" : number, "timeslot" : slot, "item" : task_struct}) 
                   
        
            number = number + 1

        return schedule
        

    def print_schedule(self):

        in_minutes = self.hours*60
        total = 0


        for item in self.schedule:
           

            total = total + item["timeslot"]
            time_remaining = in_minutes - total

            print("|--------------------------------->")
            
            print("|Activity length : %s minutes\n|Activity : %s\n|Time Spent : %s minutes\n|Time Remaining : %s minutes" % (
                item["timeslot"], item["item"], total, time_remaining))
 

        print("|--------------------------------->")

