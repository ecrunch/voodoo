

import logging




from lib._flask.flask import Flask, render_template, url_for




#from src.scorer import Scorer
#from src.classes import Task
#from src.generator import TimeSlotGenerator



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()

