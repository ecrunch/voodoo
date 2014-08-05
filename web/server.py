
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

@app.route('/all_tasks')
def get_all_tasks():

    dbconn = sqlite3.connect(DB_PATH)    
    task_adapter = TaskDbAdapter(dbconn)
    results = task_adapter.get_all_tasks()
    
    tasks = []
    for result in results:
        tasks.append({"name" : result[0], "due_date" : result[1], "category" : result[2]})


    return json.dumps(tasks)


@app.route('/all_wants')
def get_all_wants():


    print("Getting wants")

    dbconn = sqlite3.connect(DB_PATH)    
    want_adapter = WantDbAdapter(dbconn)
    results = want_adapter.get_all_wants()
    
    wants = []
    for result in results:
        wants.append({"name" : result[0], "category" : result[1]})


    return json.dumps(wants)


@app.route('/all_breaks')
def get_all_breaks():


    print("Getting Breaks")
    
    dbconn = sqlite3.connect(DB_PATH)    
    break_adapter = BreakDbAdapter(dbconn)
    
    print("before results")
    results = break_adapter.get_all_breaks()
 
    breaks = []
    for result in results:
        breaks.append({"name" : result[0], "url" : result[1]})


    return json.dumps(breaks)


if __name__ == '__main__':
    app.run()

