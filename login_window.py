from tkinter import *
from tkinter.ttk import *
import main
from sign_up_window import LoginSystem
from db_connector import DatabaseManager

class LoginWindow():
    def __init__(self, root, user_db):
        self.email_label = None
        self.email_entry = None
        self.password_label = None
        self.password_entry = None
        self.message_label = None
        self.root = root
        self.user_db = user_db
        root.title("Log in")
        root.geometry("900x900")

        self.window()

        self.root.mainloop()

    def window(self):
        emailLabel = Label(self.root, text="Email")
        emailLabel.place(x=350, y=250)

        emailEntry = Entry(self.root)
        emailEntry.place(x=350,y=270)
        email = emailEntry.get()

        passwordLabel = Label(self.root, text="Password")
        passwordLabel.place(x=350,y=300)

        passwordEntry = Entry(self.root)
        passwordEntry.place(x=350, y=320)
        password = passwordEntry.get()
        #user_db.user_credentials(email, password)
         
        #login = main.Main.menu(root)
        #log = main
        LoginButton = Button(self.root, text="Login", command=lambda: self.check_login_details(email, password))
        LoginButton.place(x=350, y=340)
        
       # LoginButton.bind("<Button>", lambda e:log.Main(self))

        #signUp = sign_up_window
        createAccountButton = Button(self.root, text="Create account", command=self.openSignUp)
        createAccountButton.place(x=350,y=400)
        #createAccountButton.bind("<Button>", lambda e: signUp.LoginSystem(self) )

    def openMenu(self):
        main.Main(self)
        root.withdraw()
    
    def check_login_details(self, email, password):
        if self.user_db.user_credentials(email, password):
            self.openMenu()
            root.withdraw()
        else:
            pass
            
    def openSignUp(self):
        print("In openSignUp")
        login = LoginSystem(self.root, DatabaseManager())
        login.sign_up_fields()
        #self.withdraw()
        
        print("Closing openSign")

# Initializing the tkinter module 
root = Tk()
# user_db gets access to all methods that connect to database
# see db_connector.py for functions
user_db = DatabaseManager()
# Calling the constructor of the class (Running the program)
LoginWindow(root, user_db)