from module.database import sql_select
from flask import Flask, render_template, request, redirect, session, flash
import os
import psycopg2
import bcrypt

from module.info import create_user, create_kitchen, kitchen_id, get_password, get_menu, get_allergies

DB_URL = os.environ.get("DATABASE_URL", "dbname=allie_db")

SECRET_KEY = os.environ.get("SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def create_signup():
    
    if session.get('user_name') == None:
        return redirect('/login')
    
    name = session.get('user_name')
    id = session.get('id')
    menu = get_menu(id)
    allie = get_allergies(id)
    
    
    return render_template('home.jinja', name=name, menu=menu, allie=allie)

@app.route('/login')
def login():

    return render_template('login.jinja')    

@app.route('/sign_up')
def create():
    
    return render_template('sign_up.jinja')    


@app.route('/login_action', methods=['POST'])
def login_action():
    email = request.form.get('email')
    password = request.form.get('password')
    info = get_password(email)
    password_hash = info[0][3]
    valid = bcrypt.checkpw(password.encode(), password_hash.encode())
    
    if valid == False:
        flash("Wrong Password")
        return redirect('/login')
    
    session['id'] = info[0][4]
    session['user_name'] = info[0][1]
    return redirect('/')

@app.route('/logout')
def logout():
    session['user_name'] = None
    session['id'] = None
    return redirect('/')

@app.route('/create_acount', methods=['POST'])
def create_acount():
    email = request.form.get('email')
    name = request.form.get('user_name')
    password = request.form.get('password')
    kitchen = request.form.get('kitchen')
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    
    create_kitchen(kitchen)
    id = kitchen_id(kitchen)
    create_user(email, name, password, id[0][0])
    
   
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)