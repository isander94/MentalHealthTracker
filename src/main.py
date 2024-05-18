from tkinter import *
from tkinter.ttk import *
from daily_journal import DailyJournal
from previous_notes import Previous_notes
from statistic import Statistic
from db_connector import DatabaseManager
import matplotlib.pyplot as pyplot

def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)
class Main(Toplevel):

    def __init__(self, root = None):

        super().__init__(root)
        self.title("Menu")
        self.geometry("900x900")
        self.user_db = DatabaseManager()
        bg_color = rgb_to_hex((135, 190, 128))
        self.configure(background=bg_color)
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
        # statistic = Statistic(self)
        # statistic.grab_set()
        # self.withdraw()
        
            # Fetch notes and moods
        moods = self.user_db.get_mood(self.user_db.email)
        print("Contents 1:")
        print(moods)
        
            # Create lists where dates and lists will be stored
        dates_list = []
        moods_list = []
            # Extract the moods and dates from tuples and place in a list
        for x in range(len(moods)):
            dates_list.append(moods[x][3])
            moods_list.append(moods[x][1])
        print("Data added to lists")
        print("Contents:")
        print(dates_list)
        print(moods_list)

            # Take the last 7 dates and moods
        dates_list = dates_list[-7:]
        moods_list = dates_list[-7:]
        print("Last 7 extracted")

        pyplot.plot(dates_list, moods_list)
        pyplot.show()



    
    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #