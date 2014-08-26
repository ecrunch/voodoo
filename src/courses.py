from sqlalchemy import(
	Table, MetaData, Column, Integer, String, create_engine, ForeignKey
)

from sqlalchemy import (
	mapper, sessionmaker, relationship, backref
)

from sqlalchemy.ext.declarative import declarative_base

engine = create_enginer('sqlite://db/data/sqlalchemy.db')
metadata = MetaData()

course = Table('courses', metadata, 
				Column('course_num', Integer, primary_key=True),
			)
				
blackboards = Table('board', metadata,
				Column('course_num', Integer),
				Column('bulletin', String(50))
			)
				
				
courseTasks = Table('junction', metadata,
				Column('course_num', Integer),
				Column('task_id', Integer)
			)
			
class Course(Base):

	__tablename__ = 'courses'
	course_num = Column(Integer, primary_key=True)
	
	__tablename__ = 'blackboards'
	course_num = Column(Integer)
	bulletin = Column(String(50))
	
	__tablename__ = 'courseTasks'
	course_num = Column(Integer)
	tasks = Column(Integer)
	
	
	def jsonify(self):
		return{
			"course_num" : self.course_num,
			
		}
