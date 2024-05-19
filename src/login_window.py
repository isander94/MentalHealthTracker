from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import main
import sign_up_window

import db_connector
def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)
class LoginWindow(Tk):
    """Initializes the login window"""
    def __init__(self):
        super().__init__()
        self.title("Log in")
        self.geometry("900x900")  # size of window
        bg_color = rgb_to_hex((135, 190, 128))
        self.configure(background=bg_color)
        self.message_label = None
        
        # Load and process the image to make white background transparent
        self.image = Image.open("image.png")
        self.image = self.image.convert("RGBA")
        datas = self.image.getdata()

        new_data = []
        for item in datas:
            # Change all white (also shades of whites)
            # (r, g, b, a) to (r, g, b, 0)
            if item[:3] == (255, 255, 255):
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
                
        self.image.putdata(new_data)

        self.image = self.image.resize((221, 221))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self, image=self.photo, background=rgb_to_hex((135, 190, 128)))
        self.image_label.pack(pady=30)
        
        self.window()
        self.mainloop()

    def window(self):
        """Shows the buttons and input fields on the window"""
        #Backround color
        bg_color = rgb_to_hex((135, 190, 128))

        self.emailLabel = Label(self, text="Email", foreground="white", background=bg_color, font=("Helvetica", 8, "bold"))  # email label
        self.emailLabel.pack(pady=5)

        self.emailEntry = Entry(self)  # input for email
        self.emailEntry.pack(pady=5)

        self.passwordLabel = Label(self, text="Password",foreground="white", background=bg_color,font=("Helvetica", 8, "bold"))  # password label
        self.passwordLabel.pack(pady=5)

        self.passwordEntry = Entry(self, show="*")  # input for password
        self.passwordEntry.pack(pady=5)

        LoginButton = Button(self, text="Login", command=self.check_login_info)  # button for login
        LoginButton.pack(pady=5)  # when pressed checks if given information exxists and is correct

        # displays if login was succesfull or not
        bg_color = rgb_to_hex((135, 190, 128))
        self.message_label = Label(self, text="", foreground="red", background=bg_color)
        self.message_label.pack(pady=5)

        # When pressed goes to create account window
        createAccountButton = Button(self, text="Create account", command=self.openSignUp)
        createAccountButton.pack(pady=5)

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
