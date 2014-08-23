

##
##  Attempt number 2 at managing our data
##


from sqlalchemy import * 


class DbConnection(object):

    def __init__(self, db_conn):
        self.db_conn = db_conn



def create_users_table():
    
    users = Table('users', metadata,
        Column('user_id', Integer, primary_key= True),
        Column('name', String(40))
    )
    users.create()


# TODO : figure out if we can somehow
# enter collections of items into the db

# example : could I enter 'users' as a list or something?

def create_tasks_table():
    tasks = Table('tasks', metadata,
        Column('task_id', Integer, primary_key= True),
        Column('description', String(40)),
        Column('total_minutes', Integer),
        Column('class_id', Integer),
        Column('type', String(40))
    )
    tasks.create()


def create_wants_table():
    wants = Table('wants', metadata,
        Column('want_id' , Integer, primary_key= True),
        Column('description', String(40))
    )
    wants.create()

def create_breaks_table():
    breaks = Table('breaks', metadata,
        Column('break_id', Integer, primary_key= True),
        Column('description', String(40)),
        Column('url', String(60))
    )
    breaks.create()


def create_classes_table():
    classes = Table('classes', metadata,
        Column('class_id', Integer, primary_key= True),
        Column('class_name', String(40)),
        Column('homework_frequency', String(40))
    )
    classes.create()


def create_all_tables():
    create_users_table()
    create_wants_table()
    create_breaks_table()
    create_classes_table()



create_all_tables()






db = create_engine('sqlite:///db/data/tutorial.db')
db.echo = False

metadata = MetaData(db)








