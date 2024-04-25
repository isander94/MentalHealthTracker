from tkinter import *
from tkinter.ttk import *

class Main(Toplevel):

    def __init__(self, root = None):

        super().__init__(root)
        self.title("Menu")
        self.geometry("900x900")
        label = Label(self, text="Welcome to the menu\nWhat do you want to do today?")
        label.pack()
        
        notes = Button(self, text="Daily journal")
        notes.pack()

        stats = Button(self, text="This weeks statistics")
        stats.pack()

        quit = Button(self, text="quit program", command=self.on_close)
        quit.pack()

    def on_close(self):
        self.destroy()
        self.master.destroy()