from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('students.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        prn TEXT,
        student_class TEXT,
        email TEXT,
        phone_number TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/submit',methods = ['POST'])
def submit():
      name = request.form['name']
      prn = request.form['prn']
      sclass = request.form['class']
      email = request.form['email']
      phone = request.form['phone']

      conn = sqlite3.connect('students.db')
      c = conn.cursor()
      c.execute('INSERT INTO User (full_name, prn, student_class, email, phone_number) VALUES (?, ?, ?, ?, ?)',
             (name, prn, sclass, email, phone))
      conn.commit()
      conn.close()


      return render_template('success.html',name = name, prn = prn, sclass = sclass, email = email, phone = phone)

if __name__ == '__main__':
   app.run(debug = True)
