from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root@123',
    'database': 'stud'
}

def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        print(e)
        return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/add', methods=['POST'])
def add():
    conn = None
    msg = ""

    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            cgpi = float(request.form['cgpi'])

            conn = create_connection()
            if conn is not None:
                cursor = conn.cursor()
                insert_query = "INSERT INTO students (name, addr, city, pin) VALUES (%s, %s, %s, %s)"
                student_data = (nm, addr, city, pin)
                cursor.execute(insert_query, student_data)

                insert_cgpa_query = "INSERT INTO studentsmarks (name, CGPI) VALUES (%s, %s)"
                cgpa_data = (nm, cgpi)
                cursor.execute(insert_cgpa_query, cgpa_data)

                conn.commit()
                msg = "Record successfully added"
            else:
                msg = "Failed to connect to the database"

        except mysql.connector.Error as e:
            print(e)
            if conn:
                conn.rollback()
            msg = "Error in insert operation"
        finally:
            if conn:
                conn.close()

    return render_template("result.html", msg=msg)

@app.route('/list')
def list():
    conn = create_connection()
    students = []

    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT students.name, students.addr, students.city, students.pin, studentsmarks.CGPI FROM students LEFT JOIN studentsmarks ON students.name = studentsmarks.name")
            students = cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
        finally:
            conn.close()

    return render_template("list.html", students=students)

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        search_name = request.form['search_name']
        conn = create_connection()
        students = []

        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT students.name, students.addr, students.city, students.pin, studentsmarks.CGPI FROM students LEFT JOIN studentsmarks ON students.name = studentsmarks.name WHERE students.name LIKE %s", ('%' + search_name + '%',))
                students = cursor.fetchall()
            except mysql.connector.Error as e:
                print(e)
            finally:
                conn.close()

    return render_template("search.html", students=students)

if __name__ == '__main__':
    app.run(debug=True)

