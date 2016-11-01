#!/usr/bin/python3
import time, sched

fmt = '%m/%d/%y %H:%M:%S'
fmt_time = time.strftime(fmt)
sched_time_str = '10/29/16 10:41:00'
sched_time = time.mktime(time.strptime(sched_time_str, fmt))
tdelta = int(sched_time - time.time())
scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name="default"):
  print('EVENT', time.strftime(fmt), name)

print( "Formatted time :", fmt_time)
print("Unformatted time :", time.time())
print("10/29/16 10:40:00 :", sched_time)
print("Delta :", tdelta)

print_event('Start')
scheduler.enter(tdelta, 1, print_event)

scheduler.run()
print_event('Complete')