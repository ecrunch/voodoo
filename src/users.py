
from sqlalchemy import(
    Table, MetaData, Column, 
    Integer, String, create_engine,
)


from sqlalchemy.orm import (
    mapper, sessionmaker
)

from sqlalchemy.ext.declarative import declarative_base


# Initialize the engine and tables

engine = create_engine('sqlite:///db/data/sqlalchemy.db')
metadata = MetaData() 

user = Table('users', metadata,
            Column('unique_id', Integer, primary_key=True, autoincrement=True),
            Column('name', String(50), nullable= False),
            Column('password', String(50), nullable= False),
            Column('age', Integer)
       ) 

metadata.create_all(engine)


# set the metadata to Base()
Base = declarative_base()


class User(Base):
        
    __tablename__ = 'users'
     
    unique_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    password = Column(String(50))
    age = Column(Integer)
    
    
    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age
        
    def __repr__(self):
        return "<User('%s', '%s', '%s', '%s')>" % (self.unique_id, self.name, self.password, self.age)             


    def jsonify(self):
        return {
            
        }

    def hello(self):
        print("hello")










