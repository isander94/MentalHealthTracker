from tkinter import *
from tkinter.ttk import *
import main
import sign_up_window



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
        log = main
        LoginButton = Button(self, text="Login", command=self.openMenu)
        LoginButton.place(x=350, y=340)
        LoginButton.bind("<Button>", lambda e:log.Main(self))

        signUp = sign_up_window
        createAccountButton = Button(self, text="Create account")
        createAccountButton.place(x=350,y=400)
        createAccountButton.bind("<Button>", lambda e: signUp.LoginSystem(self) )

    def openMenu(self):
        self.withdraw()


LoginWindow()