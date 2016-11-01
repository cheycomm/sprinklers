#!/usr/bin/python
import time;

# localtime = time.asctime( time.localtime(time.time()) )
# localtime = time.localtime(time.time())
# print "Local current time :", localtime

fmt = '%m/%d/%y %H:%M:%S'
fmt_time = time.strftime(fmt)
sched = time.mktime(time.strptime('10/29/16 10:00:00', fmt))


tdelta = int(sched - time.time())

print "Formatted time :", fmt_time

print "Unformatted time :", time.time()

print "08:54:00 :", sched

print "Delta :", tdelta