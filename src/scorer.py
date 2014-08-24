
import math
import datetime
from lib import statistics



class Scorer(object):

    # needs a db to look at
    def __init__(self, db, tasks):
        self.db = db
        self.score_total = 0
        self.score_list = []
        self.task_list = tasks
 
        for task in self.task_list:
            self.score_list.append(task.get_score())
       

        for score in self.score_list:
            self.score_total = self.score_total + score       
 
        self.placement_list = self._get_placement()

        self.current_task = None
       
        

    def print_all_scores(self):
        for task in self.task_list:
            print ("%s : %s" % (task.description, task.get_score()))

    def get_mean(self):   
        return statistics.mean(self.score_list)

    def get_variance(self):
        return statistics.variance(self.score_list)
    
    def get_standard_dev(self):
        return statistics.stdev(self.score_list)


    def _get_placement(self):
        
        placement_list = []
        for task in self.task_list:
            placement_list.append(self.get_placement(task))

        return placement_list

    def get_placement(self, task):
       
       x = task.get_score()
       task_name = task.description
       mean = self.get_mean()
       
       
       #SHOULD : come back and fix
       try:
            sd = self.get_standard_dev()
       except:
            sd = 0.001
      


       # HACK AS FUCK FIX TO MAKE IT WORK FIX SOON
       if sd == 0:
           sd = sd + 0.001
 
       
       zscore =(x-mean)/sd


       if zscore >=.8416:
           placement='E'
       elif zscore >=-.2533:
           placement='N'
       else:
           placement='NT'
           
       
       return placement


