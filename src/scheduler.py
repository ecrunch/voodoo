
import random

from src.generator import TimeSlotGenerator
from src.adapters import (
    JsonAdapter, TaskJsonAdapter, WantJsonAdapter, BreakJsonAdapter
    )


WANT_DB = "db/json/want/wantdb.json"
TASK_DB = "db/json/task/taskdb.json"
BREAK_DB = "db/json/break/breakdb.json"


#generator = TimeSlotGenerator(4)
#print (generator.time_slots)

class Scheduler(object):

    def __init__(self, hours, 
            taskdb=TASK_DB, wantdb=WANT_DB, breakdb=BREAK_DB):
        
        
        self.hours = hours
        self.generator = TimeSlotGenerator(hours)
        self.minutes_array = self.generator
       
        self.task_adapter = TaskJsonAdapter(taskdb)
        self.want_adapter = WantJsonAdapter(wantdb)
        self.break_adapter = BreakJsonAdapter(breakdb)

        self.schedule = self.make_schedule()
    
    def make_schedule(self):
        
        schedule = []
        time_slots = self.generator.time_slots
        for slot in time_slots:
           
            #breaks get 15 min slots
            if slot == 15:
                number_items = len(self.break_adapter.items)
                random_int = random.randint(0, number_items-1)
                schedule.append({"timeslot" : slot, "item" : self.break_adapter.items[random_int]})

            #a want or task
            else:
                random_int = random.randint(1,2)
                
                # a want
                if random_int == 1:
                    number_items = len(self.want_adapter.items)
                    random_int = random.randint(0, number_items-1)
                    schedule.append({"timeslot" : slot, "item" : self.want_adapter.items[random_int]})

                # a task
                else:
                    number_items = len(self.task_adapter.items)
                    random_int = random.randint(0, number_items-1)
                    schedule.append({"timeslot" : slot, "item" : self.task_adapter.items[random_int]})


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

