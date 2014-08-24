
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

_break = Table('breaks', metadata,
            Column('unique_id', Integer, primary_key=True, autoincrement=True),
            Column('description', String(50)),
            Column('url', String(50))
       ) 

metadata.create_all(engine)


# set the metadata to Base()
Base = declarative_base()


class Break(Base):
        
    __tablename__ = 'breaks'
     
    unique_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(50))
    url = Column(String(50))
    
    def __init__(self, description, url):
        self.description = description
        self.url = url
        
    def __repr__(self):
        return "<Break('%s', '%s', '%s')>" % (self.unique_id, self.description, self.url)             


    def jsonify(self):
        return{
            "id" : self.unique_id,
            "class" : "Break",
            "description" : self.description,
            "url" : self.url    
        }




