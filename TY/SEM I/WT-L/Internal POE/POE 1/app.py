from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_connection():
    return sqlite3.connect('patients_data.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            patient_id TEXT NOT NULL,
            patient_admit_date DATE,
            room_no INT,
            discharge_date DATE,
            clerk TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        patient_id = request.form['patient_id']
        patient_admit_date = request.form['patient_admit_date']
        room_no = request.form['room_no']
        discharge_date = request.form['discharge_date']

        clerk = f"Aseem Athale"

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO patients (name, patient_id, patient_admit_date, room_no, discharge_date, clerk)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, patient_id, patient_admit_date, room_no, discharge_date, clerk))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template('add_patient.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_name = request.form['search_name']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE name LIKE ?', ('%' + search_name + '%',))
        patients = cursor.fetchall()
        conn.close()
        return render_template('search_patient.html', patients=patients)

    return render_template('search_patient.html')

@app.route('/list')
def list():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    conn.close()
    return render_template('list_patients.html', patients=patients)



if __name__ == '__main__':
    create_table()
    app.run(debug=True)
