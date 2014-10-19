
from sqlalchemy import create_engine

from src.session_manager import SessionManager
from src.classes import User, Class, Task


engine= create_engine('sqlite:///db/data/sqlalchemy.db')
s = SessionManager(engine)

def test_add_one():

    john = User(name= 'John', password='Smith', age= 24)
    mary = User(name= 'Mary', password='Smith', age=57)
    todd = User(name= 'Todd', password= 'Jones', age= 36)
    s.add(john, commit=True)
    s.add(mary, commit=True)
    s.add(todd, commit=True)

    some_class = Class(class_name='CS 101', homework_freq='Often')
    some_class.students.append(john)
    some_class.students.append(mary)
    s.add(some_class, commit= True)

    other_class = Class(class_name='Eng 101', homework_freq='Never')
    other_class.students.append(john)
    other_class.students.append(todd)
    s.add(other_class, commit=True)


def test_add_two():

    task_one = Task(
        description = 'Science Exam', 
        date_str= '2014/09/01',
        total_minutes= 0,
        task_type = 'Exam'
    )

    task_two = Task(
        description = 'Math Homework',
        date_str= '2014/09/01',
        total_minutes= 0,
        task_type = 'Homework'
    )
    john = User(name= 'John', password= 'Smith', age= 24)

    task_one.user = john
    task_two.user = john
    s.add(task_one, commit= True)
    s.add(task_two, commit= True)
    s.add(john, commit= True)


def test_read_one():

    results = s.get_all(User)
    for row in results:
        _classes = row.classes
        for _class in _classes:
            print _class.class_name


    results = s.get_all(Class)
    for row in results:
        students = row.students
        for student in students:
            print student.name

def test_read_two():

    results = s.get_all(User)
    for row in results:
        tasks = row.tasks
        for task in tasks:
            print task.description
            print task.get_score()

    results = s.get_all(Task)
    for row in results:
        user = row.user
        print user.name


test_add_two()
test_read_two()


