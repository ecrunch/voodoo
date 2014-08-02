


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


def insert_user(DB_CONN, username, password):

    db_adapter = DbAdapter(DB_CONN) 
    db_adapter.insert_row('users', [username, password])


def list_users(DB_CONN):
    db_adapter = DbAdapter(DB_CONN)
    results = db_adapter.get_all('users')
    for result in results:
        print(result)



# SHOULD 
def delete_user(DB_CONN):
    pass

def delete_users_db(DB_CONN):
    
    db_adapter = DbAdapter(DB_CONN)
    db_adapter.delete_table('users')



def create_dialog(DB_CONN):
    
    print("Creating a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks")
    input = raw_input()

    if input == str(1) or input == 'users':
        try:
            create_users_db(DB_CONN)
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
    else:
        print("not implemented yet")

def list_dialog(DB_CONN):

    print("Listing contents of a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks")

    input = raw_input()

    if input == str(1) or input == 'users':
        list_users(DB_CONN)
    else:
        print("not implemented yet")


def delete_dialog(DB_CONN):
    
    print("Deleting a db")
    print("1) users\n2) tasks\n3) wants\n4) breaks")

    input = raw_input()

    if input == str(1) or input == 'users':
        try:
            delete_users_db(DB_CONN)
        except:
            print('Error. Users db probably does not exist')
    else:
        print("not implemented yet")



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


