'''import mysql.connector

conInfo = {"user": "Local instance 3306", "password": "Sahra143", "host": 
"localhost", "port": "3306", "database": "userDB", 
"raise_on_warnings": True}
myCon = mysql.connector.connect(**conInfo)

myCon.close()'''

import mysql.connector

'''Establishing a connection to the MySQL database'''
db_connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

def login(email, password):
    '''Function to handle user login'''
    cursor = db_connection.cursor()

    '''Check if email and password match a record in the database'''
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    if user:
        print("Login successful")
        return True
    else:
        print("Invalid email or password")
        return False

def sign_up():
    '''Function to handle user sign up'''
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    cursor = db_connection.cursor()

    ''' Check if email already exists in the database'''
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Email already exists")
    else:
         '''Insert new user into the database'''
        cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, password))
        db_connection.commit()
        print("User created successfully")

