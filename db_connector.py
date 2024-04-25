import mysql.connector
class DatabaseManager():
    def __init__(self):
        '''Establishing a connection to the MySQL database'''
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sahra123",
            database="mentalHealthTrackerDB"
        )


    def user_credentials(self, email, password):
        '''Function to handle user login'''
        cursor = self.db_connection.cursor()

        '''Check if email and password match a record in the database'''
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s ORDER BY email, password", (email, password))
        user = cursor.fetchall()
        #for user in users:
            #print(user)

        if user:
            #print("Login successful")
            return True
        else:
            #print("Invalid email or password")
            return False


    def add_user(self):
        '''Function to handle user sign up'''
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        cursor = self.db_connection.cursor()

        ''' Check if email already exists in the database'''
        cursor.execute("SELECT * FROM users WHERE email = %s", (email))
        existing_user = cursor.fetchone()

        if existing_user:
            return False
            #print("Email already exists")
        else:
            '''Insert new user into the database'''
            cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (first_name, last_name, email, password))

            db_connection.commit()
            #print("User created successfully")
