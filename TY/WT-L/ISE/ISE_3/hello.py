from logging import debug
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        deptname = request.form.get('deptname')
        prn = request.form.get('prn')

        print(f"{name} {email} {phone} {deptname} {prn}")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
