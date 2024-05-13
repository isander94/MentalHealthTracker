import mysql.connector
from datetime import datetime
class DatabaseManager():
    first_name = None
    last_name = None
    email = None
    password = None
    user_id = None
        
    def __init__(self):
        '''Establishing a connection to the MySQL database'''
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="team16",
            database="mentalhealthtrackerdb"
        )
        


    def user_credentials(self, email, password):
        '''Function to handle user login'''
        cursor = self.db_connection.cursor()
        DatabaseManager.email = email
        self.password = password
        '''Check if email and password match a record in the database'''
        sql_query = "SELECT * FROM users WHERE email = %s AND password = %s;"
        data = (email, password,)
        data = (email, password,)
        cursor.execute(sql_query, data)
        users = cursor.fetchall()
        print(users)
        if users:
            print("Login successful")
            print(users)
            cursor.close()
            return True
        else:
           print("Invalid email or password")
           cursor.close()
           return False


    def add_user(self, first_name, last_name, email, password):
        '''Function to handle user sign up'''
        cursor = self.db_connection.cursor()

        self.first_name = first_name 
        self.last_name = last_name
        self.email = email
        self.password = password

        ''' Check if email already exists in the database'''
        cursor.execute("SELECT * FROM users WHERE email = %s;", (self.email,))
        existing_user = cursor.fetchall()

        if existing_user:
            print("Email already exists")
            cursor.close()            
            return False
        else:
            '''Insert new user into the database'''
            print("Creating new account")
            sql_query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s);"
            data = (self.first_name, self.last_name, self.email, self.password,)
            cursor.execute(sql_query, data)

            self.db_connection.commit()
            print("User created successfully")
            cursor.close()
            return True
        
    def delete_user(self, email):
        """Delete a user row from the database"""
        cursor = self.db_connection.cursor()
        query = "DELETE FROM users WHERE email = %s;"
        cursor.execute(query, (email,))
        self.db_connection.commit()
        cursor.close()
            
    def add_note(self, note, email):
        cursor = self.db_connection.cursor()
        query1 = "SELECT user_id FROM users WHERE email = %s;"
        data1 = (email,)
        print(DatabaseManager.email)
        cursor.execute(query1, data1)
        user_id = cursor.fetchone()
        if user_id:    
            query2 = "INSERT INTO notes (note, user_id, date_now) VALUES (%s, %s, %s);"
            data2 = (note, user_id[0], datetime.now())
            cursor.execute(query2, data2)
            self.db_connection.commit()
            cursor.close()
            return True
        else:
            print("User not found")
            cursor.close()
            return False
    
    def previous_notes(self):
        cursor = self.db_connection.cursor()
        query1 = "SELECT user_id FROM users WHERE email = %s;"
        data1 = (self.email,)
        cursor.execute(query1, data1)
        user_id = cursor.fetchone()
        if user_id:        
            query = "SELECT note from notes where user_id = %s"
            data = (user_id[0],)
            
            cursor.execute(query, data)
            print(cursor.fetchall())
            previous_notes = cursor.fetchall()
            self.db_connection.commit()
            return previous_notes
        else:
            print("Error")