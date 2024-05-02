'''GUI for sing up window'''
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
        pattern_name = re.compile(reg_name  )# Compiling the reg_name pattern into an object
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

    def on_close(self):
        """Function used to """
        self.destroy()
        self.master.destroy()


