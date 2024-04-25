import mysql.connector

<<<<<<< HEAD
'''Establishing a connection to the MySQL database'''
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="team16",
    database="mentalHealthTrackerDB"
)
=======
class DatabaseManager:
    def __init__(self):
        '''Establishing a connection to the MySQL database'''
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
>>>>>>> 517b34822c8a719b1dc786e0ac130dda07238e59

    def check_credentials(self, email, password):
        '''Function to handle user login'''
        cursor = self.db_connection.cursor()

        '''Check if email and password match a record in the database'''
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            #print("Login successful")
            return True
        else:
            #print("Invalid email or password")
            return False

    def add_user(self):
        '''Function to handle user sign up'''
        cursor = self.db_connection.cursor()

        ''' Check if email already exists in the database'''
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

<<<<<<< HEAD
    ''' Check if email already exists in the database'''
    cursor.execute("SELECT * FROM users WHERE email = %s", (email))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Email already exists")
    else:
         '''Insert new user into the database'''
        cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, password))
        db_connection.commit()
        print("User created successfully")
=======
        if existing_user:
            #print("Email already exists")
            return False
        else:
            '''Insert new user into the database'''
            cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
                        (first_name, last_name, email, password))
            self.db_connection.commit()
            #print("User created successfully")
            return True
>>>>>>> 517b34822c8a719b1dc786e0ac130dda07238e59

