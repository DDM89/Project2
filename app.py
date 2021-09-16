from module.database import sql_select
from flask import Flask, render_template, request, redirect, session, flash
import os
import psycopg2
import bcrypt

from module.info import create_user, create_kitchen, kitchen_id, get_password, get_menu, input_dish, create_user_not_admin, edit_food, select_edit_food, change_new_password, staff

DB_URL = os.environ.get("DATABASE_URL", "dbname=allie_db")

SECRET_KEY = os.environ.get("SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    
    if session.get('user_name') == None:
        return redirect('/login')
    
    admin = session.get('admin')
    name = session.get('user_name')
    id = session.get('id')
    menu = get_menu(id)
    
    
    return render_template('home.jinja', name=name, menu=menu, admin=admin)

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
    if info == []:
        flash("Wrong Email")
        return redirect('/login')
    password_hash = info[0][3]
    valid = bcrypt.checkpw(password.encode(), password_hash.encode())
    
    if valid == False:
        flash("Wrong Password")
        return redirect('/login')
    
    session['id'] = info[0][4]
    session['user_name'] = info[0][1]
    session['admin'] = info[0][5]
    

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

@app.route('/create_dish')
def create_dish():
    

    return render_template('create_dish.jinja')

@app.route('/create_dish_action', methods=['POST'])
def create_dish_action():
    id = session.get('id')
    dish = request.form.get('dish')
    allergies = request.form.get('allergies')
    image = request.form.get('image')
    input_dish(dish, allergies, image, id)

    return redirect('/create_dish') 

@app.route('/add_user')
def add_user():
    # admin = session.get('admin')
    
    
    return render_template('add_user.jinja')


@app.route('/add_user_action', methods=['POST'])
def add_user_action():
    # admin = session.get('admin')
    email = request.form.get('email')
    name = request.form.get('user_name')
    password = request.form.get('password')
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
    id = session.get('id')
    create_user_not_admin(email, name, password, id)
    
    return redirect('/add_user')

@app.route('/settings')
def setting():
    id = session.get('id')
    names = staff(id)
    print(names)

    return render_template('setting.jinja', names=names)


@app.route('/change_password', methods=['POST'])
def change_password():
    email = request.form.get('email')
    password = request.form.get('password')
    new_password = request.form.get('new_password')
    new_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
    info = get_password(email)
    if info == []:
        flash("Wrong Email")
        return redirect('/login')
    password_hash = info[0][3]
    valid = bcrypt.checkpw(password.encode(), password_hash.encode())
    
    if valid == False:
        flash("Wrong Password")
        return redirect('/login')
    
    change_new_password(new_password, info[0][0])
    flash("Password Change Successful!")

    return redirect('/settings')


@app.route('/make_admin', methods=['POST'])
def make_admin():
    name = request.form.get('name')
    admin = request.form.get('admin')
   


    return redirect('/settings')


@app.route('/edit_food/')
def edit_food_page():
    food_id = request.args.get('id')
    menu = select_edit_food(food_id)
    return render_template('edit_food.jinja', dish=menu) 


@app.route('/edit_dish_action', methods=['POST'])
def edit_food_action():
    dish = request.form.get('dish')
    allergies = request.form.get('allergies')
    image = request.form.get('image')
    id = request.form.get('id')
    edit_food(dish, allergies, image, id)
    return redirect('/')                  

if __name__ == "__main__":
    app.run(debug=True)