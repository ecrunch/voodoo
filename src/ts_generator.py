import random

time_avaible=4
time_slots=(time_avaible*4)
time_slots_filled=0
last_time_used=0
time_schedule=[]
last_time=0
last_time2=0
time_taken=0
loop_condition=True

while loop_condition:
   if time_slots == time_slots_filled:
       if list_end==(len(time_schedule)-1)==1:
           if list_end==(len(time_schedule)-2)<4:
               del time_schedule[len(time_schedule)-1]
               time_schedule.insert(index(len(time_schedule)-2),index(len(time_schedule)-1)+1)
               break
           elif list_end==(len(time_schedule)-3)!=4:
               time_schedule.insert(index(len(time_schedule)-3),index(len(time_schedule)-3)+1)
               del time_schedule[-1]
               break
           elif list_end==(len(time_schedule)-4)!=4:
               del time_schedule[-1]
               time_schedule.insert(index(len(time_schedule)-4),index(len(time_schedule)-4)+1)
               del time_schedule[-1]
               break
       else:
           loop_condition=False
           print
           break
   elif time_slots < time_slots_filled:
   time_difference=time_slots_filled-time_slots	
   list_end=(len(time_schedule)-1)
   fixed_end_item=time_schedule[list_end]-time_difference
   time_schedule[list_end]=fixed_end_item
   loop_condition=False
   print time_schedule
   break
   
   elif len(time_schedule)>=2:

list_end=(len(time_schedule)-1)
list_end2=(list_end-1)
last_time=time_schedule[list_end]
last_time2=time_schedule[list_end2]
time_taken=last_time+last_time2

if last_time==1:
time_schedule.append(random.randint(2,4))
time_slots_filled=sum(time_schedule)
elif time_taken>=6:
time_schedule.append(1)
time_slots_filled=sum(time_schedule)
else:	
time_schedule.append(random.randint(1,4))
time_slots_filled=sum(time_schedule)

   else:	

time_schedule.append(random.randint(2,4))
time_slots_filled=sum(time_schedule)
print time_schedule
