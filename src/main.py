from tkinter import *
from tkinter.ttk import *
from daily_journal import DailyJournal
from previous_notes import Previous_notes
from statistic import Statistic
from db_connector import DatabaseManager
import matplotlib.pyplot as pyplot
from datetime import datetime

def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)
    
class Main(Toplevel):

    def __init__(self, root = None):

        super().__init__(root)
        self.title("Menu")
        self.geometry("900x900")
        self.user_db = DatabaseManager()
        self.message_label = None
        bg_color = rgb_to_hex((135, 190, 128))
        self.message_label = Label(self, text="", foreground="red", background=bg_color)
        self.message_label.pack()
        self.configure(background=bg_color)
        label_font = ("Helvetica", 16, "bold")
        label = Label(self, text="      Welcome to the menu\nWhat do you want to do today?",
             foreground="brown", font=label_font, background=bg_color)
        label.pack(pady=20)

        button_width = 20

        notes = Button(self, text="Daily journal", width=button_width, command=self.Daily_journal_window)
        stats = Button(self, text="This weeks statistics", width=button_width, command=self.Statistic_window)
        previous_notes = Button(self, text="Previous notes", width=button_width,  command=self.Previous_notes_window)
        quit_button = Button(self, text="Quit program", width=button_width, command=self.on_close)
        log_out = Button(self, text="Log out", width=button_width, command=self.go_back)

        # Centering buttons vertically and horizontally
        button_y_positions = [0.3, 0.4, 0.5, 0.6, 0.7]

        notes.place(relx=0.5, rely=button_y_positions[0], anchor=CENTER)
        stats.place(relx=0.5, rely=button_y_positions[1], anchor=CENTER)
        previous_notes.place(relx=0.5, rely=button_y_positions[2], anchor=CENTER)
        quit_button.place(relx=0.5, rely=button_y_positions[3], anchor=CENTER)
        log_out.place(relx=0.5, rely=button_y_positions[4], anchor=CENTER)
    
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
        # Fetch notes and moods
        moods = self.user_db.get_mood(self.user_db.email)

    
        if len(moods) >= 7:
            # Create lists where dates and lists will be stored
            dates_list = []
            moods_list = []
            # Extract the moods and dates from tuples and place in a list
            for x in range(len(moods)):
                moods_list.append(moods[x][0])
                dates_list.append(moods[x][1])

            for x in range (len(dates_list)):
                date_string = dates_list[x].strftime("%m-%d")
                dates_list[x] = date_string
                
            # Take the last 7 dates and moods
            dates_list = dates_list[-7:]
            moods_list = moods_list[-7:]
            

            pyplot.title("Mood statistics")
            pyplot.xlabel("Date")
            pyplot.ylabel("Mood")
            pyplot.plot(dates_list, moods_list)
            pyplot.show()
        else:
            self.message_label.config(text="Not enough data")


    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #