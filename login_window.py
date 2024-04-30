from tkinter import *
from tkinter.ttk import *
import main
import sign_up_window
from db_connector import DatabaseManager

class LoginWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Log in")
        self.geometry("900x900")

        self.window()

        self.mainloop()

    def window(self):
        usernameLabel = Label(self, text="Username")
        usernameLabel.place(x=350, y=250)

        userEntry = Entry(self)
        userEntry.place(x=350,y=270)
        username = userEntry.get()

        passwordLabel = Label(self, text="Password")
        passwordLabel.place(x=350,y=300)

        passwordEntry = Entry(self)
        passwordEntry.place(x=350, y=320)
        password = passwordEntry.get()

        #login = main.Main.menu(root)
        #log = main
        LoginButton = Button(self, text="Login", command=self.openMenu)
        LoginButton.place(x=350, y=340)
       # LoginButton.bind("<Button>", lambda e:log.Main(self))

        #signUp = sign_up_window
        createAccountButton = Button(self, text="Create account", command=self.openSignUp)
        createAccountButton.place(x=350,y=400)
        #createAccountButton.bind("<Button>", lambda e: signUp.LoginSystem(self) )

    def openMenu(self):
        main.Main(self)
        self.withdraw()

    def openSignUp(self):
        user_db = DatabaseManager()
        sign_up_window.LoginSystem(self, user_db)
        self.withdraw()


LoginWindow()