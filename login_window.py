from tkinter import *
from tkinter.ttk import *
import main
import sign_up_window
import db_connector
class LoginWindow(Tk):
    """Initializes the login window"""
    def __init__(self):
        super().__init__()
        self.title("Log in")
        self.geometry("900x900")  # size of window
        self.user_db = db_connector.DatabaseManager()
        self.message_label = None
        self.window()

        self.mainloop()

    def window(self):
        """Shows the buttons and input fields on the window"""
        self.emailLabel = Label(self, text="email")  # email label
        self.emailLabel.place(x=350, y=250)

        self.emailEntry = Entry(self)  # input for email
        self.emailEntry.place(x=350,y=270)

        self.passwordLabel = Label(self, text="Password")  # password label
        self.passwordLabel.place(x=350,y=300)

        self.passwordEntry = Entry(self, show="*")  # input for password
        self.passwordEntry.place(x=350, y=320)

        LoginButton = Button(self, text="Login", command=self.check_login_info)  # button for login
        LoginButton.place(x=350, y=340)  # when pressed checks if given information exxists and is correct

        # displays if login was succesfull or not
        self.message_label = Label(self, text="", foreground="red")
        self.message_label.place(x=350, y=370)

        # When pressed goes to create account window
        createAccountButton = Button(self, text="Create account", command=self.openSignUp)
        createAccountButton.place(x=350,y=400)

    def openMenu(self):
        """Function when succesfully loging in, goes to menu and closes
        login window"""
        main.Main(self)  # opens menu
        self.withdraw()  # closes login window

    def check_login_info(self):
        """Checks if given email and password exists and is correct
        within the database"""
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        print(f"{email}")
        print(f"{password}")
        # Checks if the credentials exists and are correct
        # then displays message
        if self.user_db.user_credentials(email, password):
            self.message_label.config(text="Login successful")
            self.openMenu()
        else:
            self.message_label.config(text="Invalid email or password")
            self.emailEntry.forget()
            self.passwordEntry.forget()


    def openSignUp(self):
        """Function that opens up the create account window,
        and login window closes"""
        sign_up_window.LoginSystem(self)  # opens create account window
        self.withdraw()  # closes login window


LoginWindow()
