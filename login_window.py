from tkinter import *
from tkinter.ttk import *
import main
import sign_up_window
from db_connector import DatabaseManager

class LoginWindow():

    def __init__(self, root, user_db):
        self.root = root
        self.user_db = user_db
        self.title("Log in")
        self.geometry("900x900")

        self.window()

        self.mainloop()

    def window(self):
        usernameLabel = Label(self.root, text="Username")
        usernameLabel.place(x=350, y=250)

        userEntry = Entry(self.root)
        userEntry.place(x=350,y=270)
        username = userEntry.get()

        passwordLabel = Label(self.root, text="Password")
        passwordLabel.place(x=350,y=300)

        passwordEntry = Entry(self.root)
        passwordEntry.place(x=350, y=320)
        password = passwordEntry.get()

        #login = main.Main.menu(root)
        #log = main
        LoginButton = Button(self.root, text="Login", command=self.openMenu)
        LoginButton.place(x=350, y=340)
       # LoginButton.bind("<Button>", lambda e:log.Main(self))

        #signUp = sign_up_window
        createAccountButton = Button(self.root, text="Create account", command=self.openSignUp)
        createAccountButton.place(x=350,y=400)
        #createAccountButton.bind("<Button>", lambda e: signUp.LoginSystem(self) )

    def openMenu(self):
        main.Main(self)
        self.withdraw()

    def openSignUp(self):
        print("In openSignUp")
        self.withdraw()
        sign_up_window.LoginSystem(self.root, DatabaseManager())
        print("Closing openSign")


LoginWindow()