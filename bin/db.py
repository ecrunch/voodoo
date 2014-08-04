import sqlite3

from src.adapters import DbAdapter


DB_PATH = "db/data/data.db"


def create_users_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'users',
        ['username', 'password'],
        ['text', 'text']
    )

def create_tasks_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'tasks',
        ['task', 'due_date', 'ttype'],
        ['text', 'text', 'text']
    )


def create_wants_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'wants',
        ['want', 'wtype'],
        ['text', 'text']
    )

def create_breaks_db(DB_CONN):

    db_adapter = DbAdapter(DB_CONN)

    db_adapter.make_table(
        'breaks',
        ['dbreak', 'link'],
        ['text', 'text']
    )

def insert_user(DB_CONN, username, password):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('users', [username, password])


def insert_task(DB_CONN, task, due_date, ttype):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('tasks', [task, due_date, ttype])

def insert_want(DB_CONN, want, wtype):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('wants', [want, wtype])

def insert_break(DB_CONN, dbreak, link):

    db_adapter = DbAdapter(DB_CONN)
    db_adapter.insert_row('breaks', [dbreak, link])


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


def create_dialog(DB_CONN):

    print("Creating a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks")
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
            print('Error. Users db probably already exists')

    elif input == str(3) or input == 'wants':
        try:
            create_wants_db(DB_CONN)
        except:
            print('Error. Users db probably already exists')

    elif input == str(4) or input == 'breaks':
        try:
            create_breaks_db(DB_CONN)
        except:
            print('Error. Users db probably already exists')

    else:
        print("Not implemented yet")


def insert_dialog(DB_CONN):

    print("Insert into db contents of a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks")

    input = raw_input()

    if input == str(1) or input == 'users':

        print("username?")
        username = raw_input()

        print("password")
        password = raw_input()

        insert_user(DB_CONN, username, password)

    elif input == str(2) or input == 'tasks':

        print("Task?")
        task = raw_input()

        print("Due Date mmddyyy?")
        due_date = raw_input()

        print("Genre?")
        ttype = raw_input()

        insert_task(DB_CONN, task, due_date, ttype)

    elif input == str(3) or input == 'wants':

        print("want?")
        want = raw_input()

        print("wtype")
        wtype = raw_input()

        insert_want(DB_CONN, want, wtype)

    elif input == str(4) or input == 'breaks':

        print("break?")
        dbreak = raw_input()

        print("link")
        link = raw_input()

        insert_break(DB_CONN, dbreak, link)
    else:
        print("Not a valid choice")


def list_dialog(DB_CONN):

    print("Listing contents of a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks")

    input = raw_input()

    if input == str(1) or input == 'users':
        list_users(DB_CONN)

    elif input == str(2) or input == 'tasks':
        list_tasks(DB_CONN)

    elif input == str(3) or input == 'wants':
        list_wants(DB_CONN)

    elif input == str(4) or input == 'breaks':
        list_breaks(DB_CONN)

    else:
        print("Not a valid choice")


def delete_dialog(DB_CONN):

    print("Deleting a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks")

    input = raw_input()

    if input == str(1) or input == 'users':
        try:
            delete_users_db(DB_CONN)
        except:
            print('Error. Users db probably does not exist')

    if input == str(2) or input == 'tasks':
        try:
            delete_tasks_db(DB_CONN)
        except:
            print('Error. Users db probably does not exist')

    if input == str(3) or input == 'wants':
        try:
            delete_wants_db(DB_CONN)
        except:
            print('Error. Users db probably does not exist')

    if input == str(4) or input == 'breaks':
        try:
            delete_breaks_db(DB_CONN)
        except:
            print('Error. Users db probably does not exist')
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


