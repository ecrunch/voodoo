from lib._flask.flask import Flask


#from src.scorer import Scorer
from src.classes import Task

from src.generator import TimeSlotGenerator



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()

