

import logging




from lib._flask.flask import (
    Flask, render_template, url_for, jsonify
)



#from src.scorer import Scorer
#from src.classes import Task
#from src.generator import TimeSlotGenerator

from src.scheduler import Scheduler



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')



@app.route('/make_schedule')
def make_schedule():
    
    scheduler = Scheduler(4)
    

    #scheduler.print_schedule()
    
    print scheduler.schedule


    return jsonify(scheduler.schedule)





if __name__ == '__main__':
    app.run()

