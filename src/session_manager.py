

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.users import User
from src.tasks import Task
from src.classes import Class
from src.wants import Want
from src.breaks import Break


Session = sessionmaker()


class SessionManager(object):


    def __init__(self, engine):
        self.engine = engine
        
        Session.configure(bind=engine)
        self.session = Session()

        
    def add(self, obj, commit=False):
        self.session.add(obj)
        if commit:
            self.session.commit()


    def get_all(self, table):
        return self.session.query(table).all()


    def get_one(self, table, unique_id):
        return self.session.query(table).filter(table.unique_id == unique_id).first() 

    def update_one(self, table, values, commit=False):
        self.session.query(table).update(values, synchronize_session=False)
        if commit:
            self.session.commit()


# runners for adding shit
def _user(session):
    zack = User('Zack', 'Botkin', 24)
    session.add(zack, commit= True)
    results = session.get_all(User)
    for obj in results:
        print(obj)


def _task(session):
    test_task_one = Task('Study For Science Exam', '2014/09/01', 0, 1, 'Exam', 1)
    session.add(test_task_one, commit= True)
    results = session.get_all(Task)
    for obj in results:
        print(obj.jsonify())

def _class(session):
    test_class = Class('Bio 101', 'Weekly')
    session.add(test_class, commit= True)
    results = session.get_all(Class)
    for obj in results:
        print(obj)
        #print(obj.jsonify())


def _want(session):
    test_want = Want('Go to the gym', 'Health')
    session.add(test_want, commit= True)
    results = session.get_all(Want)
    for obj in results:
        print(obj.jsonify())


def _break(session):
    test_break = Break('Go on reddit', 'http://www.reddit.com')
    session.add(test_break, commit= True)
    results = session.get_all(Break)
    for obj in results:
        #print(obj)
        print(obj.jsonify())




def main():
    
    engine = create_engine('sqlite:///db/data/sqlalchemy.db')
    session = SessionManager(engine)
    
    play_all = False
    if(play_all):
        _user(session)
        _task(session)
        _class(session)    
        _want(session)
        _break(session)
    play_one = True
    if play_one:
        obj = session.get_one(Task, 1)
        print (obj.jsonify())


#main()

