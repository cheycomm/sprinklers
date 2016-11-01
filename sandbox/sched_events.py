#! python
import sched, time
s = sched.scheduler(time.time, time.sleep)
def print_time(a="default"):
  print("From print_time", time.time(), a)

def print_some_times():
  print(time.time())
  s.enter(60, 1, print_time)
  s.enter(30, 2, print_time, argument=('positionnal',))
  s.enter(30, 1, print_time, kwargs={'a': 'keyword'})
  s.run()  
  print(time.time())

print_some_times()

