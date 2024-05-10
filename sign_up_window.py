'''GUI for sing up window'''
<<<<<<< HEAD
from tkinter import*
from db_connector import check_credentials, add_user
class LoginSystem:
    def __init__(self, root): #add as a parameter user_db 
        self.root = root
        self.email_label = None
        self.email_entry = None
        self.password_label = None
        self.password_entry = None
        self.last_name_label = None
        self.last_name_entry = None
        self.first_name_label = None
        self.first_name_entry = None
        #self.user_db = user_db
        

        self.create_login_ui()
        

    def login(self):
        email = self.email_entry.get() 
        password = self.password_entry.get()
        '''connect to datababe'''

        if self.user_db.user_credentials(email, password):
            self.message_label.config(text="Login successful")
        else:
            self.message_label.config(text="Invalid email or password")

        #print("Login successful")
        #print("Invalid email or password")

    
    def sign_up_fields(root):
        '''function for showing creating new account fields'''
        global email_entry, email_label, password_entry, password_label
        '''self.email_label.place_forget()
        self.email_entry.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()'''

        '''Create labels and entry fields'''
        self.first_name_label = Label(self.root, text="First name: ")
        self.first_name_label.grid(padx=10, pady=5)
        self.first_name_label.place(x=350, y=200)
        self.first_name_entry = Entry(self.root)
        self.first_name_entry.grid(padx=10, pady=5)
        self.first_name_entry.place(x=350, y=230)

        self.last_name_label = Label(self.root, text="Last name: ")
        self.last_name_label.grid(padx=10, pady=5)
        self.last_name_label.place(x=350, y=250)
        self.last_name_entry = Entry(self.root)
        self.last_name_entry.grid(padx=10, pady=5)
        self.last_name_entry.place(x=350, y=270)

        self.email_label = Label(self.root, text="Email name: ")
        self.email_label.grid(padx=10, pady=5)
        self.email_label.place(x=350, y=300)
        self.email_entry = Entry(self.root)
        self.email_entry.grid(padx=10, pady=5)
        self.email_entry.place(x=350, y=320)

        self.password_label = Label(self.root, text="Password name: ")
        self.password_label.grid(padx=10, pady=5)
        self.password_label.place(x=350, y=350)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(padx=10, pady=5)
        self.password_entry.place(x=350, y=370)

        '''Create account button'''
        '''root.create_account_button = Button(root, text="Create Account", command=root.sign_up_window)
        root.create_account_button.grid(columnspan=2, padx=10, pady=5)
        root.create_account_button.place(x=350, y=400)'''
        
        '''back to login button'''
        '''root.back_login_button = Button(root, text="Create Account", command=root.back_to_login)
        root.back_login_button.place(x=350, y=400)'''


    def sign_up_window(self):
        '''Function for creating a new account'''
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email.get()
        password = self.password.get()

        '''Connect to database'''
        if self.user_db.add_user(first_name, last_name, email, password):
            self.message_label.config(text="Account created successfully")
        else:
            self.message_label.config(text="Email already exists")

        #print("Account created successfully")
        #print("Email already exists")

    def create_login_ui(self):
        '''crating labels and entry fields for sign in'''

        self.email_label = Label(self.root, text="Email:")
        self.email_label.grid(padx=20, pady=5)
        self.email_label.place(x=350, y=230)
        self.email_entry = Entry(self.root)
        self.email_entry.grid(padx=20, pady=5)
        self.email_entry.place(x=350, y=250)

        self.password_label = Label(self.root, text="Password:")
        self.password_label.grid(padx=20, pady=5)
        self.password_label.place(x=350, y=270)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(padx=20, pady=5)
        self.password_entry.place(x=350, y=300)


        '''Creating login buttons'''

        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.grid(padx=10, pady=10)
        self.login_button.place(x=350, y=320)

        self.message_label = Label(self.root, text="", fg="red")
        self.message_label.place(x=350, y=350)
            
        self.create_account_button = Button(self.root, text="Create Account", command=self.sign_up_fields)
        self.create_account_button.grid(padx=10, pady=5)
        self.create_account_button.place(x=350, y=400)

    def back_to_login(self):
        '''Reset to login screen'''
        self.first_name_label.place_forget()
        self.first_name_entry.place_forget()
        self.last_name_label.place_forget()
        self.last_name_entry.place_forget()
        self.email_label.place_forget()
        self.email_entry.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()

        self.create_login_ui()

'''Creating the main window'''
'''root = Tk()
root.geometry("900x900")
root.title("Login")
user_db = DatabaseManager()

login_system = LoginSystem(root, user_db)
#login_system = LoginSystem(root)

#root.mainloop()
'''
=======
from tkinter import *
"""Importing re that will be used when handling conditions for entries"""
import re
"""Importing the DatabaseManager class from db_connector that will be used when connecting the code to database"""
from db_connector import DatabaseManager
class LoginSystem(Toplevel):
    """LoginSystem used to create and handle the signup window"""
    def __init__(self, root = None): #add as a parameter user_db 
        
        super().__init__(root)
        self.title("sign up") # Title of the windoe 
        self.geometry("900x900") # Geometry of the window
        self.message_label = None # Used later in the code for when an error message needs to be displayed
        self.first_name_label = Label(self, text="First name: ") # Text for the first name entry
        self.first_name_label.grid(padx=10, pady=5) # Amount of padding vertically and horizontally
        self.first_name_label.place(x=350, y=200) # Placement of text
        self.first_name_entry = Entry(self) # Creation of the input box
        self.first_name_entry.grid(padx=10, pady=5) # Padding for the input box vertically and horizontally
        self.first_name_entry.place(x=350, y=230) # Placement of input box

        self.last_name_label = Label(self, text="Last name: ") # Text for the last name entry
        self.last_name_label.grid(padx=10, pady=5) # Amount of padding vertically and horizontally
        self.last_name_label.place(x=350, y=250) # Placement of text
        self.last_name_entry = Entry(self) # Creation of the input box
        self.last_name_entry.grid(padx=10, pady=5) # Padding for the input box vertically and horizontally
        self.last_name_entry.place(x=350, y=270) # Placement of input box

        self.email_label = Label(self, text="Email name: ") # Text for the email entry
        self.email_label.grid(padx=10, pady=5) # Amount of padding vertically and horizontally
        self.email_label.place(x=350, y=300) # Placement of text
        self.email_entry = Entry(self) # Creation of the input box
        self.email_entry.grid(padx=10, pady=5) # Padding for the input box vertically and horizontally
        self.email_entry.place(x=350, y=320) # Placement of input box

        self.password_label = Label(self, text="Password name: ") # Text for the password entry
        self.password_label.grid(padx=10, pady=5) # Amount of padding vertically and horizontally
        self.password_label.place(x=350, y=350) # Placement of text
        self.password_entry = Entry(self, show="*") # Creation of the input box
        self.password_entry.grid(padx=10, pady=5) # Padding for the input box vertically and horizontally
        self.password_entry.place(x=350, y=370) # Placement of input box

        '''self.create_login_ui()'''
        # Creation of button with text "Create account" that will execute add_user() 
        goBack = Button(self, text="Create account", command=self.add_user)
        goBack.place(x=350, y=410) # Placement of button
        
        self.message_label = Label(self, text="", foreground="red") # Creation of the error message
        self.message_label.place(x=350, y=390) # Placement of error message
        
        # Creation of button with text "quit program" that will execute on_close() 
        quit = Button(self, text="quit program", command=self.on_close)
        quit.place(x=350, y=450) # Placement of button
    
    def add_user(self):
        """Function is used to add a user to the database if certain values return True"""
        first_name = self.first_name_entry.get() # Return the first name of the user
        last_name = self.last_name_entry.get() # Return the last name of the user
        email = self.email_entry.get() # Return the email of the user
        password = self.password_entry.get() # Return the password of the user
        
        user_db = DatabaseManager() # Creation of an instance of the DatabaseManager class 
        # Creation of pattern that will be used to check if all conditions of the password are met 
        reg_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&#])[A-Za-z\d@$!%?&#]{8,20}" 
        reg_name = "^[a-zA-Z]+$" # Creation of pattern that will be used to check that only big or small letters are used
        reg_email = "^(?=.*[@])[a-zA-Z@]" # Creation of pattern that will be used to check that @ is used and that big and small letters can be used 
        pattern_email = re.compile(reg_email) # Compiling the reg_email pattern into an object 
        pattern_name = re.compile(reg_name)# Compiling the reg_name pattern into an object
        pattern_password = re.compile(reg_password) # Compiling the reg_password pattern into an object 
        match_password = re.search(pattern_password, password) # Searching for a match of the pattern pattern_password in the string password  
        match_first_name = re.search(pattern_name, first_name) # Searching for a match of the pattern pattern_name in the string first_name
        match_last_name = re.search(pattern_name, last_name) # Searching for a match of the pattern pattern_name in the string last_name
        match_email = re.search(pattern_email, email) # Searching for a match of the pattern pattern_email in the string email
        
        if match_password: # If the pattern from the object pattern_password is inside the string password
            if match_first_name and match_last_name: # If the pattern from the object pattern_name is inside the string first_name and lat_name
                if match_email: # If the pattern from the object pattern_email is inside the string email   
                    if user_db.add_user(first_name,last_name,email,password): # If the return value is True
                        self.message_label.config(text="Account created successfully") # Account is created successfully
                        self.go_back() # Function to go back to the login window
                    else: # If email is already in use
                        self.message_label.config(text="Email is already in use")
                else: # If the pattern was not inside the email 
                    self.message_label.config(text="Please input a valid email")
            else: # If the pattern was not inside the first and last name 
                self.message_label.config(text="Empty input in first och last name")
        else: # If the pattern was not inside the password
            self.message_label.config(text="""Password requirments: atleast 8 character, 1 big and small letter, special sign (@$!%?&#)""")
        

            
    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #
>>>>>>> 9637c6093efcdec6d29509fcef5f197f31b64d25

    def on_close(self):
        """Function used to """
        self.destroy()
        self.master.destroy()


