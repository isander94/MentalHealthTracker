'''GUI for sing up window'''
from tkinter import*
from db_connector import DatabaseManager
class LoginSystem:
    def __init__(self, root, user_db): #add as a parameter user_db 
        self.root = root
        self.email_label = None
        self.email_entry = None
        self.password_label = None
        self.password_entry = None
        self.last_name_label = None
        self.last_name_entry = None
        self.first_name_label = None
        self.first_name_entry = None
        self.message_label = None
        self.user_db = user_db
        

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

    
    def sign_up_fields(self):
        '''function for showing creating new account fields'''
        global email_entry, email_label, password_entry, password_label
        self.email_label.place_forget()
        self.email_entry.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()

        '''Create labels and entry fields'''
        self.first_name_label = Label(self.root, text="First name: ")
        self.first_name_label.grid(padx=10, pady=5)
        self.first_name_label.place(x=350, y=200)
        self.first_name_entry = Entry(self.root)
        self.first_name_entry.grid(padx=15, pady=5)
        self.first_name_entry.place(x=350, y=230)

        self.last_name_label = Label(self.root, text="Last name: ")
        self.last_name_label.grid(padx=15, pady=5)
        self.last_name_label.place(x=350, y=250)
        self.last_name_entry = Entry(self.root)
        self.last_name_entry.grid(padx=15, pady=5)
        self.last_name_entry.place(x=350, y=270)

        self.email_label = Label(self.root, text="Email name: ")
        self.email_label.grid(padx=15, pady=5)
        self.email_label.place(x=350, y=300)
        self.email_entry = Entry(self.root)
        self.email_entry.grid(padx=15, pady=5)
        self.email_entry.place(x=350, y=320)

        self.password_label = Label(self.root, text="Password name: ")
        self.password_label.grid(padx=15, pady=5)
        self.password_label.place(x=350, y=350)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(padx=15, pady=5)
        self.password_entry.place(x=350, y=370)

        '''Create account button'''
        self.create_account_button = Button(self.root, text="Create Account", command=self.sign_up_window)
        self.create_account_button.grid(columnspan=2, padx=10, pady=5)
        self.create_account_button.place(x=350, y=400)
        
        '''back to login button'''
        self.back_login_button = Button(self.root, text="Create Account", command=self.back_to_login)
        self.back_login_button.place(x=350, y=400)


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
root = Tk()
root.geometry("900x900")
root.title("Login")
user_db = DatabaseManager()

login_system = LoginSystem(root, user_db)
#login_system = LoginSystem(root)

root.mainloop()




