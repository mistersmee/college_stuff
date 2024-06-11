import sqlite3

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

def insert_values_in_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (id, full_name, email, phone_number, department_name, prn) VALUES(?, ?, ?, ?, ?, ?)","(1,'Aseem Aniket Athale','athaleaseem@gmail.com','7887880897','AIML','2122000421')")
    cursor.execute("INSERT INTO User (id, full_name, email, phone_number, department_name, prn) VALUES(?, ?, ?, ?, ?, ?)","(2,'A','a@a.com','3232','DS','2')")
    cursor.execute("INSERT INTO User (id, full_name, email, phone_number, department_name, prn) VALUES(?, ?, ?, ?, ?, ?)","(3,'B','asas@asas.com','98989','ASA','3')")
    cursor.execute("INSERT INTO User (id, full_name, email, phone_number, department_name, prn) VALUES(?, ?, ?, ?, ?, ?)","(4,'C','asaasas@asas.com','99999','sdasda','323')")
    conn.commit()
    conn.close()

insert_values_in_table()
