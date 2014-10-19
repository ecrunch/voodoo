
from sqlalchemy import *

db = create_engine('sqlite:///db/data/tutorial.db')
db.echo = False


metadata = MetaData(db)

users = Table('users', metadata,
    Column('user_id', Integer, primary_key= True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String(40))
)

users.create()

i = users.insert()
i.execute(
    {
        'name' : 'Zack',
        'age' : 24
    },
    {
        
       'name' : 'Casey',
       'age' : 24
    }
)

s = users.select()
rs = s.execute()

row = rs.fetchone()
print('Id:', row[0]) 
print('Name:', row['name'])
print('Age:', row.age)
print('Password:', row[users.c.password])


for row in rs:
    print(row.name, 'is', row.age, 'years old')










