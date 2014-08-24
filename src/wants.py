
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

want = Table('wants', metadata,
            Column('unique_id', Integer, primary_key=True, autoincrement=True),
            Column('description', String(50)),
            Column('category', String(50))
       ) 

metadata.create_all(engine)


# set the metadata to Base()
Base = declarative_base()


class Want(Base):
        
    __tablename__ = 'wants'
     
    unique_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(50))
    category = Column(String(50))
    
    def __init__(self, description, category):
        self.description = description
        self.category = category
        
    def __repr__(self):
        return "<Want('%s', '%s', '%s')>" % (self.unique_id, self.description, self.category)             


    def jsonify(self):
        return {
            "id" : self.unique_id,
            "description" : self.description,
            "category" : self.category
        }

