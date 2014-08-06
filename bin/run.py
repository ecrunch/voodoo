

from src.scheduler import Scheduler, JSONScheduler
from optparse import OptionParser

opt_parser = OptionParser()
opt_parser.add_option("--hours", dest="num_hours")
(options, args) = opt_parser.parse_args() 




def main():

    if options.num_hours:
        try:
            hours = int(options.num_hours)
        except:
            print("Must enter a valid number of hours")
            return
    else:
        hours = 4

    scheduler = JSONScheduler(hours)
    scheduler.print_schedule()


main()
