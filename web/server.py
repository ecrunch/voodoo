
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
    JSONScheduler,
    DBScheduler
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
    #scheduler = JSONScheduler(int(hours)) 
    scheduler = DBScheduler(int(hours)) 
    return json.dumps(scheduler.schedule)


@app.route('/all_users')
def get_all_users():

    dbconn = sqlite3.connect(DB_PATH)    
    adapter = DbAdapter(dbconn)
    results = adapter.get_all('users')
    
    users = []
    for result in results:
        users.append({"id" : result[0], "name" : result[1], "password" : result[2]})


    return json.dumps(users)


# might want to forgo constructing the object here
# if we don't care about displaying the score
@app.route('/all_tasks')
def get_all_tasks():

    dbconn = sqlite3.connect(DB_PATH)
    task_adapter = TaskDbAdapter(dbconn)


    tasks = []

    for item in task_adapter.items:
        tasks.append({
            "class" : "Task",
            "id" : item.id,
            "description" : item.name, 
            "due_date" : str(item.due_date), 
            "category" : str(type(item)),
            "score" : item.get_score(),
            "total_minutes" : item.total_minutes
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


@app.route('/add_minutes', methods = ['GET'])
def add_minutes():
        
    id = request.args.get('id')
    minutes = request.args.get('time_slot')
    item_class = request.args.get('item_class')
    
     
    dbconn = sqlite3.connect(DB_PATH)    
    adapter = DbAdapter(dbconn)
  
    table_name = ""
    if item_class == "Task":
        table_name = "tasks"
    else:
        return "NA" 
   
    qry = "SELECT * FROM %s WHERE id = '%s'" % (table_name, id)
    print (qry)
    
    results = adapter._execute_qry(qry)
    

    total_minutes = results[0][5] 
    
    total_minutes = int(total_minutes) + int(minutes)

    qry = "UPDATE %s SET total_minutes = %s WHERE id = '%s'" % (table_name, total_minutes, id)
    adapter._execute_qry(qry)

    return json.dumps({"minutes": total_minutes})



@app.route('/reset_minutes', methods = ['GET'])
def reset_minutes():

    id = request.args.get('id')
    item_class = request.args.get('item_class')
    print(id, item_class)

    dbconn = sqlite3.connect(DB_PATH)    
    adapter = DbAdapter(dbconn)

    table_name = ""
    if item_class == "Task":
        table_name = "tasks"
    else:
        return "NA"
        
    qry = "UPDATE %s SET total_minutes = %s WHERE id = '%s'" % (table_name, 0, id)
    adapter._execute_qry(qry)
    
    return "ok" 
    
     
         
if __name__ == '__main__':
    app.run()

