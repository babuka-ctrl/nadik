from flask import Flask, render_template, request, redirect, url_for
from db import DatabaseManager

app = Flask(__name__)

@app.route('/')
def redirect_to_home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('user.html')

@app.route('/buytick')
def buytick():
    return render_template('Online-Ticketing-System-main/buytick.html')

@app.route('/contact')
def contact():
    return render_template('Online-Ticketing-System-main/contact.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/read_form',methods=['POST'] )
def read_form():
    users = DatabaseManager('users.db')
    users.create_tables()
    data=request.form
    userEmail=data['userEmail']
    userNmae = data['name']
    userLastname = data['lastname']
    dictsend=(userEmail,userNmae,userLastname)
    users.query('''INSERT INTO Users VALUES (?,?,?)''',dictsend)
    return render_template('read_form.html')

@app.route('/show')
def show():
    try:
        users=DatabaseManager('Users.db')
        ltstuser=users.fetchall('''SELECT * FROM users''')
        print(ltstuser)
    except:
        ltstuser=[('в базе','нет','пользователей')]
    return render_template('show.html',ltstuser=ltstuser)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=5000,debug=True)