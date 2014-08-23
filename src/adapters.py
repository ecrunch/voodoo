

##
##  Attempt number 2 at managing our data
##


from sqlalchemy import * 


db = create_engine('sqlite:///db/data/tutorial.db')
db.echo = False

metadata = MetaData(db)


def create_users_table():
    
    users = Table('users', metadata,
        Column('user_id', Integer, primary_key= True),
        Column('name', String(40))
    )
    users.create()


def create_wants_table():
    pass 

def create_breaks_table():
    pass 

def create_classes_table():
    pass 




def create_all_tables():
    create_users_table()
    #create_wants_table()
    #create_breaks_table()
    #create_classes_table()



create_all_tables()




    









