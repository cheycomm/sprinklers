from flask import Flask, render_template
import sched, time

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cakes')
def cakes():
	return 'Yummy cakes!'

@app.route('/hello/<name>')
def hello(name):
  return render_template('page.html', name=name)

@app.route('/schedule')
def schedule():
  filename = "schedule.log"
  s = sched.scheduler(time.time, time.sleep)
  f = open(filename, 'w')
  
  def print_time(a="default"):
    f.write("From print_time" + str(time.time()) + a + "\n")

  def print_some_times():
    f.write(str(time.time()) + "\n")
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positionnal',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    f.write(str(time.time()) + "\n")

  print_some_times()
  return render_template('index.html')

@app.route('/write')
def write():
  filename = "test.txt"
  f = open(filename, 'a')
  f.write("This is test data.\n")
  f.close()

  return render_template('index.html')

@app.route('/gpio/<gpio_port>/<onOff>')
def gpio(gpio_port, onOff):
  filename = "/home/todd/" + gpio_port + ".txt"
  f = open(filename, 'w')
  f.write(onOff + "\n")
  f.close()

  return render_template('index.html')
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
