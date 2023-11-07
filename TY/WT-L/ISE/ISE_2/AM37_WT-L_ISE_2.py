from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('apple_lab.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        email TEXT,
        phone_number TEXT,
        department_name TEXT,
        prn TEXT
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
      email = request.form['email']
      phone = request.form['phone']
      department_name = request.form['dept']
      prn = request.form['prn']

      conn = sqlite3.connect('apple_lab.db')
      c = conn.cursor()
      c.execute('INSERT INTO User (full_name, email, phone_number, department_name, prn) VALUES (?, ?, ?, ?, ?)',
             (name, email, phone, department_name, prn))
      conn.commit()
      conn.close()

      conn = sqlite3.connect('apple_lab.db')
      c  = conn.cursor()
      c.execute('SELECT * FROM User')
      entries = c.fetchall()
      conn.commit()
      conn.close()

      return render_template('success.html', entries = entries)

if __name__ == '__main__':
   app.run(debug = True)
