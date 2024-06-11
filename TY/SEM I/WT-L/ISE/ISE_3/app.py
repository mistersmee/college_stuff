import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def create_user_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            department_name TEXT NOT NULL,
            prn TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_user_table()

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        deptname = request.form.get('deptname')
        prn = request.form.get('prn')
        if name and email:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (full_name, email, phone_number, department_name, prn) VALUES (?, ?)', (name, email, phone, deptname, prn))
            conn.commit()
            conn.close()
    return render_template('user.html')


if __name__ == '__main__':
    app.run(debug=True)
