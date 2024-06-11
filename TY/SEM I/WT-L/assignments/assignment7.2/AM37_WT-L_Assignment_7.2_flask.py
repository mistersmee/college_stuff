from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'Full Name: %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = []
      user.append(request.form['fname'])
      user.append(request.form['mname'])
      user.append(request.form['lname'])
      fullname = str(user[0] + ' ' +  user[1] + user[2])
      return redirect(url_for('success',name = fullname))
   else:
      user = []
      user.append(request.args.get('fname'))
      user.append(request.args.get('mname'))
      user.append(request.args.get('lname'))
      fullname = str(user[0] + ' ' +  user[1] + user[2])
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
