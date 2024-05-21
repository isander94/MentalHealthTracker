"""Module for main window."""
from tkinter import *
from tkinter.ttk import *
from daily_journal import DailyJournal
from previous_notes import Previous_notes
from db_connector import DatabaseManager
import matplotlib.pyplot as pyplot
from datetime import datetime

def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)

class Main(Toplevel):
    """Main class."""

    def __init__(self, root = None):
        """Manin class initialization."""
        super().__init__(root)
        self.title("Menu")
        self.geometry("900x900")
        self.user_db = DatabaseManager()
        self.message_label = None
        bg_color = rgb_to_hex((135, 190, 128))
        self.message_label = Label(self, text="", foreground="red", background=bg_color)
        self.message_label.pack()
        self.configure(background=bg_color)

        # wellcome message label
        label_font = ("Helvetica", 16, "bold")
        label = Label(self, text=f"Welcome! \nWhat do you want to do today?",
             foreground="white", font=label_font, background=bg_color, anchor="center")
        label.pack(pady=20)

        # Main buttons
        notes = Button(self, text="Daily journal", width=20, command=self.Daily_journal_window)
        stats = Button(self, text="This weeks statistics", width=20, command=self.Statistic_window)
        previous_notes = Button(self, text="View notes", width=20,  command=self.Previous_notes_window)
        quit_button = Button(self, text="Quit program", width=20, command=self.on_close)
        log_out = Button(self, text="Log out", width=15, command=self.go_back)

        # Centering buttons vertically and horizontally
        button_y_positions = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

        # Buttons placering
        notes.place(relx=0.5, rely=button_y_positions[2], anchor=CENTER)
        stats.place(relx=0.5, rely=button_y_positions[3], anchor=CENTER)
        previous_notes.place(relx=0.5, rely=button_y_positions[4], anchor=CENTER)
        quit_button.place(relx=0.5, rely=button_y_positions[5], anchor=CENTER)
        log_out.place(relx=0.9, rely=button_y_positions[0], anchor=CENTER)

    def on_close(self):
        """Function for closing windows"""
        self.destroy()
        self.master.destroy()

    def Daily_journal_window(self):
        """Function for dialy journal window initialization"""
        journal_window = DailyJournal(self)
        journal_window.grab_set()
        self.withdraw()

    def Previous_notes_window(self):
        """Function for dialy  initialization"""
        previous_notes = Previous_notes(self)
        previous_notes.grab_set()
        self.withdraw()

    def Statistic_window(self):
        """Fetch notes and moods"""
        moods = self.user_db.get_mood(self.user_db.email)

        if len(moods) >= 7:
            mood_dict = {}
            for date, mood in moods:
                date_string = date.strftime("%m-%d")
                mood_dict[date_string] = mood  # This will keep the last mood for each date
            print(mood_dict)
            # Convert the dictionary back to lists
            dates_list = list(mood_dict.keys())
            moods_list = list(mood_dict.values())

            # Sort the dates_list to maintain chronological order
            sorted_dates = sorted(dates_list)
            sorted_moods = [mood_dict[date] for date in sorted_dates]


            # Take the last 7 dates and moods
            sorted_dates = dates_list[-7:]
            sorted_moods = moods_list[-7:]

            # Create a graph
            pyplot.title("Mood statistics")
            pyplot.xlabel("Date")
            pyplot.ylabel("Mood")
            pyplot.plot(sorted_dates, sorted_moods)
            pyplot.show()
            pyplot.close()
        else:
            # If there is't atleast 7 entries, the graph will not be displayed
            self.message_label.config(text="Not enough data")


    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify()