from os import truncate
from module.database import sql_select, sql_write, sql_select_wright


def create_kitchen(kitchen):
    return sql_write('INSERT INTO kitchen_table (kitchen_name) VALUES (%s)', [kitchen])

def kitchen_id(kitchen):
    return sql_select_wright("SELECT kitchen_id FROM kitchen_table WHERE kitchen_name = %s", [kitchen])    

def create_user(email, name, password_hash, restaurant_id):

    return sql_write(
        "INSERT INTO users (email, name, password_hash, restaurant_id, admin) VALUES (%s, %s, %s, %s, true)",
        [email, name, password_hash, restaurant_id]
    )

def create_user_not_admin(email, name, password_hash, restaurant_id):

    return sql_write(
        "INSERT INTO users (email, name, password_hash, restaurant_id, admin) VALUES (%s, %s, %s, %s, false)",
        [email, name, password_hash, restaurant_id]
    )            

def get_password(email):

    return sql_select_wright('SELECT * FROM users WHERE email ILIKE %s;', [email])  

def get_menu(id):

    return sql_select_wright('SELECT * FROM menu WHERE kitchen_id = %s AND active = TRUE;', [id])

def input_dish(dish, allergies, image, id):
    
    return sql_write("INSERT INTO menu (dish, allergies, active, images, kitchen_id) VALUES (%s, %s, true, %s, %s);", [dish, allergies, image, id])

def get_kitchen_name(id):
    return sql_select_wright("SELECT * FROM kitchen_table WHERE kitchen_id = %s;", [id])[0][1]

def select_edit_food(id):
    return sql_select_wright('SELECT * FROM menu WHERE id = %s ;', [id])

def edit_food(dish, allergies, image, id):

    return sql_write('UPDATE menu SET dish = %s, allergies = %s, active = TRUE, images = %s WHERE id = %s;', [dish, allergies, image, id])


def change_new_password(new_password, id):

    return sql_write('UPDATE users SET password_hash = %s WHERE id = %s;', [new_password, id])
                              

def staff(id):

    return sql_select_wright('SELECT name FROM users WHERE restaurant_id = %s;', [id])


def change_admin(admin, name):

    return sql_write('UPDATE users SET admin = %s WHERE name = %s;', [admin, name])
    


