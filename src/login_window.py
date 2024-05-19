"""Module for login windo."""
from tkinter import *
from tkinter.ttk import *
#from PIL import Image, ImageTK
import main
import sign_up_window
import db_connector
def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)
class LoginWindow(Tk):
    """Class the login window."""


    def __init__(self):
        """Initializing the class"""
        super().__init__()
        self.title("Log in")
        self.geometry("900x900")  # size of window
        bg_color = rgb_to_hex((135, 190, 128))
        self.configure(background=bg_color)
        self.message_label = None

        """ self.image = Image.open("image.png")
        self.photo = ImageTK.PhotoImage(self.image)
        self.image_label = Label(self, image=self.photo)
        self.image_label.image = self.photo
        self.image_label.place(x=350, y=50) """
        self.window()

        self.mainloop()

    def window(self):
        """Shows the buttons and input fields on the window"""
        self.emailLabel = Label(self, text="Email")  # email label
        self.emailLabel.place(x=350, y=320)

        self.emailEntry = Entry(self)  # input for email
        self.emailEntry.place(x=350,y=340)

        self.passwordLabel = Label(self, text="Password")  # password label
        self.passwordLabel.place(x=350,y=370)

        self.passwordEntry = Entry(self, show="*")  # input for password
        self.passwordEntry.place(x=350, y=390)

        LoginButton = Button(self, text="Login", command=self.check_login_info)  # button for login
        LoginButton.place(x=350, y=420)  # when pressed checks if given information exxists and is correct

        # displays if login was succesfull or not
        bg_color = rgb_to_hex((135, 190, 128))
        self.message_label = Label(self, text="", foreground="red", background=bg_color)
        self.message_label.place(x=350, y=450)

        # When pressed goes to create account window
        createAccountButton = Button(self, text="Create account", command=self.openSignUp)
        createAccountButton.place(x=350,y=500)

    def openMenu(self):
        """Function when succesfully loging in, goes to menu and closes
        login window"""
        main.Main(self)  # opens menu
        self.clear_message() # clear text
        self.withdraw()  # closes login window

    def check_login_info(self):
        """Checks if given email and password exists and is correct
        within the database"""
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        user_db = db_connector.DatabaseManager()
        print(f"{email}")
        print(f"{password}")
        # Checks if the credentials exists and are correct
        # then displays message
        if user_db.user_credentials(email, password):
            self.message_label.config(text="Login successful")
            self.openMenu()
            self.emailEntry.delete(0, 'end')
            self.passwordEntry.delete(0, 'end')
        else:
            self.message_label.config(text="Invalid email or password")
            self.emailEntry.delete(0, 'end')
            self.passwordEntry.delete(0, 'end')

    def openSignUp(self):
        """Function that opens up the create account window,
        and login window closes"""
        sign_up_window.LoginSystem(self)  # opens create account window
        self.clear_message() # clear text
        self.withdraw()  # closes login window

    def clear_message(self):
        """Functionf for clear text on the screen"""
        self.message_label.config(text="")

LoginWindow()
