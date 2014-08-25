import sqlite3

from src.adapters import DbAdapter


DB_PATH = "db/data/data.db"


def create_users_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'users',
        [
            'id integer primary key autoincrement', 
            'username', 
            'password'
        ]
    )

def create_tasks_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'tasks',
        [
            'id integer primary key autoincrement', 
            'user_id',
            'class_id',
            'description', 
            'due_date', 
            'type', 
            'total_minutes',
        ],
    )


def create_wants_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'wants',
         [
            'id integer primary key autoincrement', 
            'user_id', 
            'description', 
            'category'
        ],
    )

def create_breaks_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'breaks',
        [
            'id integer primary key autoincrement', 
            'user_id', 
            'description', 
            'link'
        ],
    )


def create_classes_db(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'classes',
        [
            'id integer primary key', 
            'class_name', 
            'homework_frequency'
        ],
    )


def create_assignments_db(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'assignments',
        [ 
            'id integer primary key', 
            'task_id', 
            'user_id'
        ],
    )


def create_rosters_db(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    
    db_adapter.make_table(
        'rosters',
        [    
            'id integer primary key', 
            'class_id', 
            'user_id'
        ],
    )



def insert_user(DB_CONN, username, password):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('users', [username, password])


def insert_task(DB_CONN, user_id, class_id, description, due_date, type):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('tasks', [user_id, class_id, description, due_date, type, '0'])

def insert_want(DB_CONN, user, want, category):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('wants', [user, want, category])

def insert_break(DB_CONN, user, description, link):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('breaks', [user, description, link])

def insert_class(DB_CONN, class_name, homework_frequency):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('classes', [class_name, homework_frequency])

def insert_assignment(DB_CONN, task_id, user_id):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('assignments', [task_id, user_id])

def insert_roster(DB_CONN, class_id, user_id):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('rosters', [class_id, user_id])

def list_users(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('users')
    for result in results:
        print(result)

def list_tasks(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('tasks')
    for result in results:
        print(result)

def list_wants(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('wants')
    for result in results:
        print(result)

def list_breaks(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('breaks')
    for result in results:
        print(result)

def list_classes(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('classes')
    for result in results:
        print(result)

def list_assignments(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('assignments')
    for result in results:
        print(result)

def list_rosters(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('rosters')
    for result in results:
        print(result)

# SHOULD
def delete_user(DB_CONN):
    pass

def delete_users_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('users')

def delete_task(DB_CONN):
    pass

def delete_tasks_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('tasks')

def delete_want(DB_CONN):
    pass

def delete_wants_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('wants')

def delete_break(DB_CONN):
    pass

def delete_breaks_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('breaks')


def delete_classes_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('classes')

def delete_assignments_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('assignments')

def delete_rosters_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('rosters')


def create_dialog(DB_CONN):

    print("Creating a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks\n5) classes\n6) assignments\n7) rosters")
    input = raw_input()

    if input == str(1) or input == 'users':
        try:
            create_users_db(DB_CONN)
        except:
            print('Error. Users db probably already exists')

    elif input == str(2) or input == 'tasks':
        try:
            create_tasks_db(DB_CONN)
        except:
            print('Error. Tasks db probably already exists')

    elif input == str(3) or input == 'wants':
        try:
            create_wants_db(DB_CONN)
        except:
            print('Error. Wants db probably already exists')

    elif input == str(4) or input == 'breaks':
        try:
            create_breaks_db(DB_CONN)
        except:
            print('Error. Breaks db probably already exists')

    elif input == str(5) or input == 'classes':
        try:
            create_classes_db(DB_CONN)
        except:
            print('Error. Classes db probably already exists')

    elif input == str(6) or input == 'assignments':
        try:
            create_assignments_db(DB_CONN)
        except:
            print('Error. Assignments db probably already exists')
     
    elif input == str(7) or input == 'rosters':
        try:
            create_rosters_db(DB_CONN)
        except:
            print('Error. Classes db probably already exists')
    
    else:
        print("Not implemented yet")


def insert_dialog(DB_CONN):

    print("Insert into db contents of a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks\n5) classes\n6) assignments\n7) rosters")

    input = raw_input()

    if input == str(1) or input == 'users':

        print("Username?")
        username = raw_input()

        print("Password?")
        password = raw_input()

        insert_user(DB_CONN, username, password)

    elif input == str(2) or input == 'tasks':

        print("User ID?")
        user_id = raw_input()

        print("Class ID?")
        class_id = raw_input()

        print("Task description?")
        description = raw_input()

        print("Task Due Date? (YYYYMMDD)")
        due_date = raw_input()

        print("Task Type? (Exam, Homework, Paper, Project, Task)")
        type = raw_input()

        insert_task(DB_CONN, user_id, class_id, description, due_date, type)

    elif input == str(3) or input == 'wants':

        print("User?")
        user = raw_input()

        print("Want Description?")
        description = raw_input()

        print("Want Category?")
        category = raw_input()

        insert_want(DB_CONN, user, description, category)

    elif input == str(4) or input == 'breaks':

        print("User?")
        user = raw_input()

        print("Break description?")
        description = raw_input()

        print("Url?")
        url = raw_input()

        insert_break(DB_CONN, user, description, url)
     
    elif input == str(5) or input == 'classes':

        print("Class name?")
        class_name = raw_input()

        print("Homework frequency?")
        homework_frequency = raw_input()

        insert_class(DB_CONN, class_name, homework_frequency)
    
    elif input == str(6) or input == 'assignments':

        print("Task ID?")
        task_id = raw_input()

        print("User ID?")
        user_id = raw_input()

        insert_assignment(DB_CONN, task_id, user_id)
    
    elif input == str(7) or input == 'rosters':

        print("Class ID?")
        class_id = raw_input()

        print("User ID?")
        user_id = raw_input()

        insert_roster(DB_CONN, class_id, user_id)
    
    
    else:
        print("Not a valid choice")


def list_dialog(DB_CONN):

    print("Listing contents of a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks\n5) classes\n6) assignments\n7) rosters")
    
    input = raw_input()

    if input == str(1) or input == 'users':
        list_users(DB_CONN)

    elif input == str(2) or input == 'tasks':
        list_tasks(DB_CONN)

    elif input == str(3) or input == 'wants':
        list_wants(DB_CONN)

    elif input == str(4) or input == 'breaks':
        list_breaks(DB_CONN)

    elif input == str(5) or input == 'classes':
        list_classes(DB_CONN)
     
    elif input == str(6) or input == 'assignments':
        list_assignments(DB_CONN)
    
    elif input == str(7) or input == 'rosters':
        list_rosters(DB_CONN)
    else:
        print("Not a valid choice")


def delete_dialog(DB_CONN):

    print("Deleting a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks\n5) classes\n6) assignments\n7) rosters")
    
    input = raw_input()

    if input == str(1) or input == 'users':
        try:
            delete_users_db(DB_CONN)
        except:
            print('Error. Users db probably does not exist')

    elif input == str(2) or input == 'tasks':
        try:
            delete_tasks_db(DB_CONN)
        except:
            print('Error. Tasks db probably does not exist')

    elif input == str(3) or input == 'wants':
        try:
            delete_wants_db(DB_CONN)
        except:
            print('Error. Wants db probably does not exist')

    elif input == str(4) or input == 'breaks':
        try:
            delete_breaks_db(DB_CONN)
        except:
            print('Error. Breaks db probably does not exist')
    
    
    elif input == str(5) or input == 'classes':
        try:
            delete_classes_db(DB_CONN)
        except:
            print('Error. Classes db probably does not exist')
    
    elif input == str(6) or input == 'assignments':
        try:
            delete_assignments_db(DB_CONN)
        except:
            print('Error. Assignments db probably does not exist')
    

    elif input == str(7) or input == 'rosters':
        try:
            delete_rosters_db(DB_CONN)
        except:
            print('Error. Rosters db probably does not exist')
    
    else:
        print("Not a valid choice")



def main():

    print("Connecting to %s" % DB_PATH)


    DB_CONN = sqlite3.connect(DB_PATH)
    print("Connection Successful")


    session_over = False

    while not session_over:

        print("1) create\n2) insert\n3) list\n4) delete")

        input = raw_input()

        if input == str(1) or input == 'create':
            create_dialog(DB_CONN)
        elif input == str(2) or input == 'insert':
            insert_dialog(DB_CONN)
        elif input == str(3) or input == 'list':
            list_dialog(DB_CONN)
        elif input == str(4) or input == 'delete':
            delete_dialog(DB_CONN)
        else:
            print("Please enter a number or command")
            session_over = not session_over




main()


