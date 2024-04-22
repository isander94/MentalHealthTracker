from tkinter import *

root = Tk()
root.geometry("900x900")
root.title("Log In")

usernameLabel = Label(root, text="Username", fg ="blue", bg="lightblue")
usernameLabel.place(x=450, y=350)

entry = Entry(root)

entry.place(x=450,y=370)


root.mainloop()