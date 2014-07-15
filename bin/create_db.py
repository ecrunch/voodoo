

import sqlite3

conn = sqlite3.connect('db/example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE tasks
             (date text, name text, type text)''')

# Insert a row of data
c.execute("INSERT INTO tasks VALUES ('2014-07-20', 'Science Test', 'Exam')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


print("Database Created")
