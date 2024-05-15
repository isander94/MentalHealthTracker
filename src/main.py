from tkinter import *
from tkinter.ttk import *
from daily_journal import DailyJournal
from previous_notes import Previous_notes
from statistic import Statistic
class Main(Toplevel):

    def __init__(self, root = None):

        super().__init__(root)
        self.title("Menu")
        self.geometry("900x900")
        label = Label(self, text="Welcome to the menu\nWhat do you want to do today?")
        label.pack()
        
        notes = Button(self, text="Daily journal", command=self.Daily_journal_window)
        self.geometry("900x900")
        notes.pack()

        stats = Button(self, text="This weeks statistics", command=self.Statistic_window)
        stats.pack()
        
        previous_notes = Button(self, text="Previous notes", command=self.Previous_notes_window)
        previous_notes.pack()
        
        quit = Button(self, text="quit program", command=self.on_close)
        quit.pack()
        
        log_out = Button(self, text="Log out", command=self.go_back)
        log_out.pack()

    def on_close(self):
        self.destroy()
        self.master.destroy()
    
    def Daily_journal_window(self):
        journal_window = DailyJournal(self)
        journal_window.grab_set()
        self.withdraw()
    
    def Previous_notes_window(self):
        previous_notes = Previous_notes(self)
        previous_notes.grab_set()
        self.withdraw()

    def Statistic_window(self):
        statistic = Statistic(self)
        statistic.grab_set()
        self.withdraw()
    
    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #