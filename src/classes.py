
import math
import datetime
import statistics

EXAM_INITIAL_SCORE = 5 
PROJECT_INITIAL_SCORE = 4
PAPER_INITIAL_SCORE = 4
HW_INITIAL_SCORE = 3


class Task(object):

    # t stands for 'task'
    def __init__(self, t_name=None, due_date=None):

        self.start_date = self._set_start_date()

        self.name = t_name
        self.due_date = due_date

        # decided by subclass
        self.base_score = None


    # TODO : expand
    def _set_start_date(self):
        return datetime.datetime.today()

    def _get_days_remaining(self):
        delta = self.due_date.day - self.start_date.day
        return delta

    def add_days_to_due_date(self, num_days):
        self.due_date = self.due_date + datetime.timedelta(days= num_days)
        return


class Exam(Task):

    def __init__(self, t_name=None, due_date=None):
        Task.__init__(self, t_name, due_date)
        self.base_score = EXAM_INITIAL_SCORE

    def get_score(self):

        days_remaining = self._get_days_remaining()
        if days_remaining <= 10:
            return self.base_score + (10 - days_remaining)
        else:
            return self.base_score
    

class Project(Task):

    def __init__(self, t_name=None, due_date=None):
        Task.__init__(self, t_name, due_date)
        self.base_score = PROJECT_INITIAL_SCORE

    def get_score(self):

        days_remaining = self._get_days_remaining()
        if days_remaining <= 10:
            return self.base_score + (10 - days_remaining)
        else:
            return self.base_score


class Paper(Task):

    def __init__(self, t_name=None, due_date=None):
        Task.__init__(self, t_name, due_date)
        self.base_score = PAPER_INITIAL_SCORE

    def get_score(self):

        days_remaining = self._get_days_remaining()
        if days_remaining <= 10:
            return self.base_score + (10 - days_remaining)
        else:
            return self.base_score


class Homework(Task):

    def __init__(self, t_name=None, due_date=None):
        Task.__init__(self, t_name, due_date)
        self.base_score = HW_INITIAL_SCORE

    def get_score(self):

        days_remaining = self._get_days_remaining()
        if days_remaining <= 5:
            return self.base_score + (5 - days_remaining)
        else:
            return self.base_score



class Scheduler(object):

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




    
