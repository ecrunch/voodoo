
from sqlalchemy import(
    Table, MetaData, Column, 
    Integer, String, create_engine,
)


from sqlalchemy.orm import (
    mapper, sessionmaker
)

from sqlalchemy.ext.declarative import declarative_base

import datetime



# Initialize the engine and tables

engine = create_engine('sqlite:///db/data/sqlalchemy.db')
metadata = MetaData() 

task = Table('tasks', metadata,
            Column('unique_id', Integer, primary_key=True, autoincrement=True),
            Column('description', String(50)),
            Column('date_str', String(50)),
            Column('total_minutes', Integer),
            Column('class_id', Integer),
            Column('task_type', String(50)),
            Column('user_id', Integer)
       ) 

metadata.create_all(engine)


# set the metadata to Base()
Base = declarative_base()



BASE_SCORES = {
    "Exam" : 5,
    "Project" : 4,
    "Paper" : 4,
    "Homework" : 3
}



class Task(Base):
        
    __tablename__ = 'tasks'
     
    unique_id  = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(50))
    date_str = Column(String(50))
    total_minutes = Column(Integer)
    class_id = Column(Integer)
    task_type = Column(String(50))
    user_id = Column(Integer)
    
    
    def __init__(self, description, date_str, total_minutes, class_id, task_type, user_id):
        
        self.description = description
        self.date_str = date_str
        self.total_minutes = total_minutes
        self.class_id = class_id
        self.task_type = task_type
        self.user_id = user_id

        
    def __repr__(self):
        return "<Task('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.unique_id, self.description, self.date_str, self.total_minutes, self.class_id, self.task_type, self.user_id
        )             


    #TODO : expand this
    def _get_current_date(self):
        return datetime.datetime.today()

    def _make_datetime(self, datestr):
        return datetime.datetime.strptime(datestr, "%Y/%m/%d")
    
    def _get_days_remaining(self):
        
        current_date = self._get_current_date()
        due_date = self._make_datetime(self.date_str)
                    
        delta = (due_date - current_date).days
        return delta

    
    def get_score(self): 
        days_remaining = self._get_days_remaining()
        if days_remaining <= 10:
            return BASE_SCORES[self.task_type] + (10 - days_remaining)
        else:
            return BASE_SCORES[self.task_type]


    def jsonify(self):
        return{
            "id" : self.unique_id,
            "class" : "Task",
            "type" : self.task_type,
            "description" : self.description,
            "due_date" : self.date_str,
            "score" : self.get_score(),
            "total_minutes" : self.total_minutes,
            "placement" : "TODO"
        }
    


