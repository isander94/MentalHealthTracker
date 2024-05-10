import mysql.connector
class DatabaseManager():
    def __init__(self):
        '''Establishing a connection to the MySQL database'''
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
<<<<<<< HEAD
            password="Sahra123",
            database="mentalHealthTrackerDB"
        )
=======
            password="team16",
            database="mentalhealthtrackerdb"
        )
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        
>>>>>>> 9637c6093efcdec6d29509fcef5f197f31b64d25


    def user_credentials(self, email, password):
        '''Function to handle user login'''
        cursor = self.db_connection.cursor()

        '''Check if email and password match a record in the database'''
<<<<<<< HEAD
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
=======
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s ORDER BY email, password", (email, password,))
        #cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)
        #for user in users:
        #    if user[3] == email and user[4] == password:
        #        print("Login successful")
        #        print(f"{user[3]} {user[4]}")
        #        cursor.close()
        #        #self.db_connection.close()
        #        return True
        #return False

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
        print("Here")
        cursor = self.db_connection.cursor()

        self.first_name = first_name 
        self.last_name = last_name
        self.email = email
        self.password = password

        
        ''' Check if email already exists in the database'''
        cursor.execute("SELECT * FROM users WHERE email = %s;", (email,))
        existing_user = cursor.fetchall()

        if existing_user:
            print("Email already exists")
            cursor.close()            
            #self.db_connection.close()
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
            #self.db_connection.close()
            return True
            
>>>>>>> 9637c6093efcdec6d29509fcef5f197f31b64d25
