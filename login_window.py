from tkinter import *

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


root.mainloop()