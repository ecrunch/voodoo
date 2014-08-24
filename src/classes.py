
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

_class = Table('classes', metadata,
            Column('class_id', Integer, primary_key=True, autoincrement=True),
            Column('class_name', String(50)),
            Column('homework_frequency', String(50))
       ) 

metadata.create_all(engine)


# set the metadata to Base()
Base = declarative_base()


class Class(Base):
        
    __tablename__ = 'classes'
     
    class_id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50))
    homework_frequency = Column(String(50))
    
    def __init__(self, class_name, homework_frequency):
        self.class_name = class_name
        self.homework_frequency = homework_frequency
        
    def __repr__(self):
        return "<Class('%s', '%s', '%s')>" % (self.class_id, self.class_name, self.homework_frequency)             


    def hello(self):
        print("hello")

