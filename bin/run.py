

from sqlalchemy import create_engine
from src.scheduler import Scheduler
from optparse import OptionParser
from src.session_manager import SessionManager
from src.tasks import Task
from src.wants import Want
from src.breaks import Break


opt_parser = OptionParser()
opt_parser.add_option("--hours", dest="num_hours")
(options, args) = opt_parser.parse_args() 


engine = create_engine('sqlite:///db/data/sqlalchemy.db')
session = SessionManager(engine)




def main():

    
    tasks = session.get_all(Task)
    wants = session.get_all(Want)
    breaks = session.get_all(Break)


    if options.num_hours:
        try:
            hours = int(options.num_hours)
        except:
            print("Must enter a valid number of hours")
            return
    else:
        hours = 4

    scheduler = Scheduler(hours, tasks, wants, breaks)
    scheduler.print_schedule()


main()
