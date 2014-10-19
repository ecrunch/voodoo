
import logging
import json

from lib._flask.flask import (
    Flask, 
    render_template, 
    url_for, 
    jsonify, 
    Response, 
    request,
    make_response,
    send_file,
)

from sqlalchemy import create_engine

from src.scheduler import Scheduler

from src.session_manager import SessionManager

from src.classes import (
    User, Task, Want, Break, Class, Assignment
)

#global db shit
engine = create_engine('sqlite:///db/data/sqlalchemy.db')
session = SessionManager(engine)

app = Flask(__name__)

### templates
@app.route('/')
def index():
    
    #cached : 'prod'
    return send_file('templates/index.html')
        
    #uncached : dev
    #return make_response(open('templates/index.html').read())


@app.route('/confirm_login', methods= ['GET'])
def confirm_login():
    
    user_name = request.args.get('userName')
    password = request.args.get('password')
 
    users = session.get_all(User)
    
    for user in users:
        if user.name == user_name and user.password == password:
            print(user.id)
            return json.dumps(user.id)
    return json.dumps(0)


@app.route('/login', methods= ['POST'])
def login():
    pass

@app.route('/get_user_data/<id>')
def get_user_data(id=1):
    
    user_obj = session.get_one(User, id)

    user_data = {}
    user_data["classes"] = []
    user_data["tasks"] = []
    user_data["wants"] = []
    user_data["breaks"] = []

    user_data["name"] = user_obj.name

    for _class in user_obj.classes:
        user_data["classes"].append(_class.jsonify())

    for task in user_obj.tasks:
        user_data["tasks"].append(task.jsonify())

    for want in user_obj.wants:
        user_data["wants"].append(want.jsonify())

    for _break in user_obj.breaks:
        user_data["breaks"].append(_break.jsonify())

    return json.dumps(user_data)


@app.route('/add_class_to_db', methods= ['GET'])
def add_class_to_db():
 
    user_id = request.args.get('user_id')
    class_name = request.args.get('class_name')
    homework_freq = request.args.get('homework_freq')

    user_obj = session.get_one(User, user_id)
    class_obj = Class(class_name= class_name, homework_freq= homework_freq)

    class_obj.students.append(user_obj)

    session.add(class_obj, commit= True)

    return jsonify([])


@app.route('/add_task_to_db', methods= ['GET'])
def add_task_to_db():

    valid_task_types = ['Exam', 'Homework', 'Paper', 'Project']

    user_id = request.args.get('user_id')
    description = request.args.get('task_description')
    date_str = request.args.get('task_due_date')
    task_type = request.args.get('task_type')

    if task_type not in valid_task_types:
        task_type= 'Homework'


    user_obj = session.get_one(User, user_id)
    task_obj = Task(description= description, date_str= date_str, total_minutes= 0, task_type= task_type, user_id= user_id)
    
    user_obj.tasks.append(task_obj)

    session.add(user_obj, commit= True)
    return jsonify([])


@app.route('/add_want_to_db', methods= ['GET'])
def add_want_to_db():

    user_id = request.args.get('user_id')
    description = request.args.get('want_description')
    category = request.args.get('want_category')   

    user_obj = session.get_one(User, user_id)
    want_obj = Want(description= description, category= category, user_id= user_id)

    user_obj.wants.append(want_obj)

    session.add(user_obj, commit= True)
    return jsonify([])


@app.route('/add_break_to_db', methods= ['GET'])
def add_break_to_db():

    user_id = request.args.get('user_id')
    description = request.args.get('break_description')
    url = request.args.get('break_url')

    user_obj = session.get_one(User, user_id)
    break_obj = Break(description= description, url= url, user_id= user_id)

    user_obj.breaks.append(break_obj)

    session.add(user_obj, commit= True)
    return jsonify([])



@app.route('/get_schedule', methods= ['GET'])
def get_schedule():
      
    hours = int(request.args.get('hours'))
    user_id = request.args.get('user_id')

    tasks = session.get_all_with_user_id(Task, user_id)
    wants = session.get_all_with_user_id(Want, user_id)
    breaks = session.get_all_with_user_id(Break, user_id)

    print(tasks)


    scheduler = Scheduler(hours, tasks, wants, breaks) 

    return json.dumps(scheduler.jsonify())


@app.route('/delete_break_from_db/<bid>' )
def delete_break(bid=1):

    bid=int(bid)
    print(bid)
    break_obj = session.get_one(Break, bid)
    
    session.delete(break_obj, commit=True)
    
    return "Success" 


@app.route('/delete_class_from_db/<cid>' )
def delete_class(cid=1):

    cid=int(cid)
    print(cid)
    class_obj = session.get_one(Class, cid)

    session.delete(class_obj, commit=True)
    
    return "Success"

@app.route('/delete_want_from_db/<wid>' )
def delete_want(wid=1):
    
    wid=int(wid)
    print(wid)
    want_obj = session.get_one(Want, wid)

    session.delete(want_obj, commit=True)
    
    return "Success"


@app.route('/delete_task_from_db/<tid>' )
def delete_task(tid=1):

    tid=int(tid)
    print(tid)
    task_obj = session.get_one(Task, tid)
    
    session.delete(task_obj, commit=True)
    
    return "Success"



@app.route('/log_minutes', methods = ['GET'])
def add_minutes():
        
    id = request.args.get('id')
    minutes = request.args.get('minutes')
    
    print(id)
    print(minutes)
     
    obj = session.get_one(Task, id)
     
    total_minutes = obj.total_minutes 
    total_minutes = int(total_minutes) + int(minutes)

    session.update_one(Task, {'total_minutes':total_minutes}, id, commit=True)
    
    return json.dumps({"minutes": total_minutes})


@app.route('/reset_minutes', methods = ['GET'])
def reset_minutes():

    id = request.args.get('id')
    
    session.update_one(Task, {'total_minutes':0}, id, commit=True)
    
    return "ok" 


################# old shit

@app.route('/get_user_with_id/<id>')
def get_user_with_id(id=1):    
    id = int(id)
    user = session.get_one(User, id)
    print(user.jsonify())
    return json.dumps(user.jsonify())


@app.route('/all_users')
def get_all_users():

    results = session.get_all(User)
    users = []
    for obj in results:

        #come back and jsonify
        users.append({"id" : obj.id, "name" : obj.name, "password" : obj.password})


    return json.dumps(users)


# might want to forgo constructing the object here
# if we don't care about displaying the score
@app.route('/all_tasks')
def get_all_tasks():

    results = session.get_all(Task)

    tasks = []

    for obj in results:
        tasks.append(obj.jsonify())


    return json.dumps(tasks)


@app.route('/all_wants')
def get_all_wants():

    results = session.get_all(Want)

    wants = []
    for obj in results:
        wants.append(obj.jsonify())

    return json.dumps(wants)


@app.route('/all_breaks')
def get_all_breaks():

    results = session.get_all(Break)

    breaks = []
    for obj in results:
        breaks.append(obj.jsonify())

    return json.dumps(breaks)
 
     
         
if __name__ == '__main__':
    app.run()

