import mysql.connector
class DatabaseManager():
    def __init__(self):
        '''Establishing a connection to the MySQL database'''
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="team16",
            database="mentalhealthtrackerdb"
        )
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        


    def user_credentials(self, email, password):
        '''Function to handle user login'''
        cursor = self.db_connection.cursor()
        self.email = email
        self.password = password
        '''Check if email and password match a record in the database'''
        sql_query = "SELECT * FROM users WHERE email = %s AND password = %s;"
        data = (self.email, self.password,)
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
            
