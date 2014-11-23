
import random

import logging

import datetime

from src.generator import TimeSlotGenerator
from src.scorer import Scorer


class Scheduler(object):

    def __init__(self, hours, tasks):
               
        self.hours = hours
        self.generator = TimeSlotGenerator(hours)

        self.tasks = tasks

        self.e_index = 0
        self.n_index = 0
        self.nt_index = 0

        self.e_items = []
        self.n_items = []
        self.nt_items = []

        self.scorer = Scorer(db= None, tasks= self.tasks)

        self._determine_task_priorities(self.scorer)

        self.start_time = datetime.datetime.now()
        self.current_time = self.start_time
        self.minutes_to_add = 0

        self.schedule = self.make_schedule()


    def _determine_task_priorities(self, scorer):

        for task in self.tasks:

            placement = scorer.get_placement(task)

            if placement == 'E':
                self.e_items.append(task)

            elif placement == 'N':
                self.n_items.append(task)

            elif placement == 'NT':
                self.nt_items.append(task)

            # TODO : create a more specific failure case
            else:
                pass


    def _reset_index(self):
        self.e_index = 0
        self.n_index = 0
        self.nt_index = 0
        return


    # SHOULD : refactor into smaller chunks
    def make_schedule(self, repeat_items=True):

        schedule = []
        time_slots = self.generator.time_slots

        chosen_item_list = self.e_items
        chosen_index = self.e_index

        number = 1

        for slot in time_slots:

            self.current_time = self.current_time + datetime.timedelta(minutes=self.minutes_to_add)
            self.minutes_to_add = slot
            
            
            if self.e_index < len(self.e_items):
                chosen_item_list = self.e_items
                chosen_index = self.e_index
                self.e_index = self.e_index + 1
            else:
                if self.n_index < len(self.n_items): 
                    chosen_item_list = self.n_items
                    chosen_index = self.n_index
                    self.n_index = self.n_index + 1

                        # TODO : are we just not caring about nt?
                else:
                    if self.nt_index < len(self.nt_items): 
                        chosen_item_list = self.nt_items
                        chosen_index = self.nt_index
                        self.nt_index = self.nt_index + 1
                            
                    else:
                                # we will need to reset or quit
                        if repeat_items:
                            self._reset_index()
                                    #starts off with the first thing of the most recent list
                            chosen_index=0
                            else:
                                pass


            task = chosen_item_list[chosen_index]

            schedule.append({"number" : number, "minutes" : slot, "item" : task.jsonify(), "time" : str(self.current_time.time())})


    number = number + 1

        return schedule


    def jsonify(self):
        return self.schedule


    


