from tkinter import *
from tkinter.ttk import *

class Main(Toplevel):

    def __init__(self, root = None):

        super().__init__(root)
        self.title("Menu")
        self.geometry("900x900")
        label = Label(self, text="Welcome to the menu\nWhat do you want to do today?")
        label.pack()
        
        notes = Button(self, text="Daily journal", command=self.daily_journal)
        self.geometry("900x900")
        notes.pack()

        stats = Button(self, text="This weeks statistics")
        stats.pack()

        quit = Button(self, text="quit program", command=self.on_close)
        quit.pack()

    def on_close(self):
        self.destroy()
        self.master.destroy()

    def daily_journal(self):
        journal_window = Toplevel(self)
        journal_window.title("Daily Journal")
        journal_window.geometry("900x900")

        Label(journal_window, text="Daily journal text").pack(pady=10)

        text_area = Text(journal_window, width=50, height=20)
        text_area.pack(padx=10, pady=10)
