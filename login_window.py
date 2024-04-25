from tkinter import *
import main
import sign_up_window

root = Tk()
root.geometry("900x900")
root.title("Log In")

usernameLabel = Label(root, text="Username", fg ="blue", bg="lightblue")
usernameLabel.place(x=350, y=250)

userEntry = Entry(root)
userEntry.place(x=350,y=270)
username = userEntry.get()

passwordLabel = Label(root, text="Password", fg="blue", bg="lightblue")
passwordLabel.place(x=350,y=300)

passwordEntry = Entry(root)
passwordEntry.place(x=350, y=320)
password = passwordEntry.get()

login = main.Main.menu()
LoginButton = Button(root, text="Login", fg="black", bg="grey", command=login)
LoginButton.place(x=350, y=340)

signUp = sign_up_window
createAccountButton = Button(root, text="Create account", fg="black", bg="grey", command=signUp)
createAccountButton.place(x=350, y=400)

root.mainloop()