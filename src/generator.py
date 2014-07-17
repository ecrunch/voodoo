

import random

class TimeSlotGenerator(object):

    def __init__(self, hours):
        self.hours = hours
        self.number_gen = {
            1 : 15,
            2 : 30,
            3 : 45,
            4 : 60,
        }


    def _get_time_slots(self, hours):
        


        in_minutes = hours*60
        quadrants = in_minutes/15
        total = 0
        slots = []
        
        while total <= in_minutes:
            
            if total == in_minutes:
                break

            
            to_add = random.randint(1,4)
            minute_section = self.number_gen[to_add]
            total = total + minute_section
            print ("adding %s : left to go %s" % (minute_section, in_minutes - total))
            slots.append(minute_section)

        
        if total > in_minutes:

            print ("oops. went over. total is %s" % total)            
            #get the last item in the list
            last_item = slots[-1]

            print ("removing %s minutes" % last_item)

            #subtract it from the total
            total = total - last_item

            #figure out the correct segment to add
            #to get us to the total

            # MAY : further subdivide later
            to_add = in_minutes - total
            print ("adding %s minutes" % to_add)

            #add it to the list
            if to_add != 0:
                slots[-1] = to_add
            else:
                slots = slots[:-1] 
            

        print (slots)
        return slots


gen = TimeSlotGenerator(4)
gen._get_time_slots(4)
