
import math
import datetime
from lib import statistics


class Scorer(object):

    # needs a db to look at
    def __init__(self, db):
        self.db = db
        self.score_total = 0
        self.score_list = []
        self.task_list = self._populate_task_list()
        self.placement_list = self._get_placement()

        self.current_task = None
        

    def _populate_task_list(self):
        task_list = []
        for task in self.db.contents:

            task_list.append(task)

            score = task.get_score()
            self.score_total = self.score_total + score
            self.score_list.append(score)
            
        return task_list


    def print_all_scores(self):
        for task in self.task_list:
            print ("%s : %s" % (task.name, task.get_score()))

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
       task_name = task.name
       mean = self.get_mean()
       sd = self.get_standard_dev()
       
       zscore =(x-mean)/sd

       print ("task name : %s" % task_name)
       print ("z score : %s" % zscore)

       if zscore >=.8416:
           placement='I'
       elif zscore >=.2533:
           placement='G'
       elif zscore >=-.2533:
           placement='R'
       else:
           placement='N'
           
       print ("placement: %s" % placement)
       
       return placement

    """def _get_nom_dists(self):
        
        nom_dist = []
        for task in self.task_list:
            nom_dist.append(self.get_nom_dist(task))

        return nom_dist"""
    """def get_nom_dist(self, task):

        x = task.get_score()
        task_name = task.name
        mean = self.get_mean()
        sd = self.get_standard_dev()
        var = self.get_variance()
        pi = 3.1415926

        #print ("task name : %s" % task_name)
        #print ("x score : %s" % x)
        #print ("mean : %s" % mean)
        #print ("var : %s" % var)
        #print ("sd : %s" % sd)

        num = math.exp(-(float(x)-float(mean))**2/(2*var))
        denom = (sd*(2*pi)**.5)
        #print ("num : %s" % num)
        #print ("denom : %s" % denom) 
        result = num/denom
        #print("percent : %s" % result)
        #print ("------------------")
        return result"""

        




## wrapper for DB
# will have actual DB connection code here
class MockDB(object):

    def __init__(self):
        self.contents = []

    def save(self, task):
        self.contents.append(task)




    
