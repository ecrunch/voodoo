

import logging
import json



from lib._flask.flask import (
    Flask, render_template, url_for, 
    jsonify, Response, request
)



#from src.scorer import Scorer
#from src.classes import Task
#from src.generator import TimeSlotGenerator

from src.scheduler import Scheduler



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')



@app.route('/get_schedule/<hours>')
def get_schedule(hours=4):
   
   
   
    hours = int(hours)
    scheduler = Scheduler(int(hours))
     
    

    return json.dumps(scheduler.schedule)
    





if __name__ == '__main__':
    app.run()

