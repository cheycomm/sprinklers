from flask import Flask, render_template

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

@app.route('/write')
def write():
  filename = "test.txt"
  f = open(filename, 'a')
  f.write("This is test data.\n")
  f.close()

  return render_template('index.html')

@app.route('/gpio/<gpio_port>/<onOff>')
def gpio(gpio_port, onOff):
  filename = "/home/pi/" + gpio_port + ".txt"
  f = open(filename, 'w')
  f.write(onOff + "\n")
  f.close()

  return render_template('index.html')
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
