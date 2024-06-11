from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
   return 'Use `/flask`, `/python`, `/pbl`, `/miniproject` url routes.'

@app.route('/flask/')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

@app.route('/pbl/')
def hello_pbl():
   return 'Hello PBL'

@app.route('/miniproject/')
def hello_miniproject():
   return 'Hello Miniproject'

if __name__ == '__main__':
   app.run()
