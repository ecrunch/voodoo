
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


@app.route('/all_tasks')
def get_all_tasks():

    dbconn = sqlite3.connect(DB_PATH)    
    task_adapter = TaskDbAdapter(dbconn)
    results = task_adapter.get_all_tasks()
    
    tasks = []
    for result in results:
        tasks.append({"name" : result[0], "due_date" : result[1], "category" : result[2]})


    return json.dumps(tasks)




if __name__ == '__main__':
    app.run()

