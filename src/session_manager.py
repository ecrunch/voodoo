

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    def delete(self, obj, commit=False):
        self.session.delete(obj)
        if commit:
            self.session.commit()

    def get_all_with_user_id(self, table, user_id):
        return self.session.query(table).filter(table.user_id == user_id).all() 

    def get_all(self, table):
        return self.session.query(table).all()


    def get_one(self, table, unique_id):
        return self.session.query(table).filter(table.id == unique_id).first() 

    def update_one(self, table, values, unique_id, commit=False):
        
        #SHOULD : figure out a better way of committing this query?
        self.session.query(table).filter(table.id == unique_id).update(values)
        if commit:
            self.session.commit()



