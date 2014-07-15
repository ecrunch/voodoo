

import sqlite3

conn = sqlite3.connect('db/example.db')

c = conn.cursor()

### TODO stuff in here


conn.close()


print("Look at this tutorial : https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection")
