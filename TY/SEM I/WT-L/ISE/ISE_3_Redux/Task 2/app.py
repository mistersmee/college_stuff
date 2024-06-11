from flask import Flask
from flask import render_template, request, redirect, url_for
import mysql.connector

df_config = {
    'host': 'localhost',
    'user': 'root',
    'password':'root@123',
    'database':'Book'
}

connection = mysql.connector.connect(**df_config)

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/newbook')
def NewStud():
    return render_template('new.html')

@app.route('/addbook', methods = ['POST'])
def add():
    cursor = connection.cursor()

    # get the data form the form
    name = request.form['name']
    quantity=request.form['quantity']
    price = request.form['price']
    roll_no = request.form['roll_no']

    query = 'INSERT INTO book1(name,quantity,price,roll_no) VALUES (%s, %s, %s, %s)'
    data = (name, quantity, price, roll_no)

    cursor.execute(query, data)
    connection.commit()
    cursor.close()

    return render_template('success.html')

@app.route('/displaybook')
def displayStudent():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM book1')
    data = cursor.fetchall()
    cursor.close()
    return render_template('displayData.html', data = data)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/searchbook', methods = ['POST'])
def searchStudent():
    cursor = connection.cursor()

    name = request.form['name']

    cursor.execute('SELECT * FROM book1 WHERE name = %s', [name])
    data = cursor.fetchall()
    cursor.close()
    return render_template('displaybook.html', data = data)


if(__name__ == '__main__'):
    app.run(debug=True)