from fastapi import FastAPI
import mysql.connector

db_config={
    'host':'localhost',
    'user':"root",
    'password':"root@123",
    'database':'BOOK'
}

connection=mysql.connector.connect(**db_config)

app=FastAPI()

keys=['name','quantity', 'prce', 'roll_no']
list=[]

@app.get('/')
async def hello(start:int=0, end:int=10):
    # reading the data
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book1")
    data=cursor.fetchall()
    cursor.close()
    dict={}
    for i in data:
        k=0
        for j in keys:
            dict[j]=i[k]
            k=k+1
        list.append(dict)
        dict={}
    return list[start:end]