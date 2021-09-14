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

def get_password(email):

    return sql_select_wright('SELECT * FROM users WHERE email ILIKE %s;', [email])  

def get_menu(id):

    return sql_select_wright('SELECT * FROM menu WHERE kitchen_id = %s AND active = TRUE;', [id])

def get_allergies(id):
    
    split_array = []
    food = sql_select_wright('SELECT allergies FROM menu WHERE kitchen_id = %s AND active = TRUE;', [id])
    for each in food:
       element = each[0].split(', ') 
       split_array.append(element)
    return split_array  


    


