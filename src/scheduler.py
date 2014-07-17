
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

    def __init__(self, hours):
        self.hours = hours
        self.generator = TimeSlotGenerator(hours)
        self.minutes_array = self.generator
       
        self.task_adapter = TaskJsonAdapter(TASK_DB)
        self.want_adapter = WantJsonAdapter(WANT_DB)
        self.break_adapter = BreakJsonAdapter(BREAK_DB)

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
        
        for item in self.schedule:
            
            print("|--------------------------------->")
            
            print("|Time Slot : %s\nItem : %s" % (item["timeslot"], item["item"]))
 
            print("|--------------------------------->")


scheduler = Scheduler(4)
scheduler.print_schedule()
