from tkinter import *
from tkinter.ttk import *

class Main(Toplevel):

    def __init__(self, root = None):

        super().__init__(root)
        self.title("Menu")
        self.geometry("200x200")
        label = Label(self, text="Welcome to the menu")
        label.pack()

    def menu(root):
        pass