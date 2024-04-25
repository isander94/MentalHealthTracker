from tkinter import *
from tkinter.ttk import *
import main
#import sign_up_window

root = Tk()
root.geometry("900x900")
root.title("Log In")

usernameLabel = Label(root, text="Username")
usernameLabel.place(x=350, y=250)

userEntry = Entry(root)
userEntry.place(x=350,y=270)
username = userEntry.get()

passwordLabel = Label(root, text="Password")
passwordLabel.place(x=350,y=300)

passwordEntry = Entry(root)
passwordEntry.place(x=350, y=320)
password = passwordEntry.get()

#login = main.Main.menu(root)
log = main
LoginButton = Button(root, text="Login")
LoginButton.place(x=350, y=340)
LoginButton.bind("<Button>", lambda e:log.Main(root) )

#signUp = sign_up_window
createAccountButton = Button(root, text="Create account")
createAccountButton.place(x=350, y=400)

root.mainloop()