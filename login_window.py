from tkinter import *
from tkinter.ttk import *
import main
import sign_up_window
import db_connector
class LoginWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Log in")
        self.geometry("900x900")
        self.user_db = db_connector.DatabaseManager()
        self.message_label = None
        self.window()

        self.mainloop()

    def window(self):
        emailLabel = Label(self, text="email")
        emailLabel.place(x=350, y=250)

        self.emailEntry = Entry(self)
        self.emailEntry.place(x=350,y=270)

        passwordLabel = Label(self, text="Password")
        passwordLabel.place(x=350,y=300)

        self.passwordEntry = Entry(self)
        self.passwordEntry.place(x=350, y=320)
        #login = main.Main.menu(root)
        #log = main
        LoginButton = Button(self, text="Login", command=self.check_login_info)
        LoginButton.place(x=350, y=340)
        self.message_label = Label(self, text="", foreground="red")
        self.message_label.place(x=350, y=370)
       # LoginButton.bind("<Button>", lambda e:log.Main(self))

        #signUp = sign_up_window
        createAccountButton = Button(self, text="Create account", command=self.openSignUp)
        createAccountButton.place(x=350,y=400)
        #createAccountButton.bind("<Button>", lambda e: signUp.LoginSystem(self) )

    def openMenu(self):
        main.Main(self)
        self.withdraw()

    def check_login_info(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        if self.user_db.user_credentials(email, password):
            #print("Login successfull")
            self.message_label.config(text="Login successful")
            self.openMenu()
        else:
            #print("Invalid email or password")
            self.message_label.config(text="Invalid email or password")
            

    
    def openSignUp(self):
        sign_up_window.LoginSystem(self, self.user_db)
        self.withdraw()


LoginWindow()