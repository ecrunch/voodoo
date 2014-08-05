
import sqlite3
import logging
import json



from lib._flask.flask import (
    Flask, 
    render_template, 
    url_for, 
    jsonify, 
    Response, 
    request
)


from src.scheduler import(
    Scheduler,
    JSONScheduler
)

from src.adapters import(
    DbAdapter,
    TaskDbAdapter,
    WantDbAdapter,
    BreakDbAdapter
)


DB_PATH = "db/data/data.db"

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')



@app.route('/get_schedule/<hours>')
def get_schedule(hours=4):
      
    hours = int(hours)
    scheduler = JSONScheduler(int(hours)) 
    return json.dumps(scheduler.schedule)


@app.route('/all_users')
def get_all_users():

    dbconn = sqlite3.connect(DB_PATH)    
    adapter = DbAdapter(dbconn)
    results = adapter.get_all('users')
    
    users = []
    for result in results:
        users.append({"name" : result[0], "password" : result[1]})


    return json.dumps(users)


# might want to forgo constructing the object here
# if we don't care about displaying the score
@app.route('/all_tasks')
def get_all_tasks():

    dbconn = sqlite3.connect(DB_PATH)
    task_adapter = TaskDbAdapter(dbconn)


    tasks = []

    #print (task_adapter.items)
    for item in task_adapter.items:
        tasks.append({
            "description" : item.name, 
            "due_date" : str(item.due_date), 
            "category" : str(type(item)),
            "score" : item.get_score()
        })


    return json.dumps(tasks)


@app.route('/all_wants')
def get_all_wants():

    dbconn = sqlite3.connect(DB_PATH)    
    want_adapter = WantDbAdapter(dbconn)
    return json.dumps(want_adapter.items)


@app.route('/all_breaks')
def get_all_breaks():

    dbconn = sqlite3.connect(DB_PATH)    
    break_adapter = BreakDbAdapter(dbconn)
    return json.dumps(break_adapter.items)


if __name__ == '__main__':
    app.run()

