
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


# set the metadata to Base()
Base = declarative_base()


class Class(Base):

    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50))
    homework_frequency = Column(String(50))
    students = relationship('User', secondary='students')


    def jsonify(self):
        return {}


from sqlalchemy import create_engine
engine = create_engine('sqlite:///db/data/sqlalchemy.db')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
