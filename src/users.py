

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    password = Column(String(50))
    age = Column(Integer)
    classes = relationship('Class', secondary='students')

    def jsonify(self):
        return {}


class Class(Base):

    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50))
    homework_freq = Column(String(50))
    students = relationship('User', secondary='students')


    def jsonify(self):
        return {}


class Task(Base):

    __tablename__ 'tasks'
    id= Column(Integer, primary_key=True, autoincrement=True)
    description= 

#association table mapping users to classes
class Students(Base):

    __tablename__ = 'students'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('classes.id'), primary_key=True)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///db/data/sqlalchemy.db')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)





