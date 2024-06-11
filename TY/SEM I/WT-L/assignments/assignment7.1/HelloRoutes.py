from flask import Flask
app = Flask(__name__)

@app.route('/flask') #Add /flask/ URL results in 404 Not Found page
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()