"""Module for previous notes window."""
from tkinter import *
from tkinter.ttk import *
from db_connector import DatabaseManager
from datetime import datetime

from db_connector import DatabaseManager
def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)

class Previous_notes(Toplevel):
    """Class for showing notes."""
    def __init__(self, parent):
        """Class initialization."""
        super().__init__(parent)
        self.title("Daily Journal")
        self.geometry("900x900")
        self.notes_label = None
        bg_color = rgb_to_hex((135, 190, 128))
        self.configure(background=bg_color)
        title_label = Label(self, text="Your Previous Notes", font=("Helvetica", 28, "bold"), foreground="white", background=bg_color)
        title_label.pack(pady=5)
        self.notes_label = Label(self, text="", foreground="white", background=bg_color, font=("Helvetica", 10, "bold"))
        self.notes_label.pack()
        self.user_db = DatabaseManager()
        go_back = Button(self, text="Go back", command=self.go_back)
        go_back.pack(pady=5)
        self.print_previous_notes()

    def print_previous_notes(self):
        """Prints the previous notes of the user."""
        email = self.user_db.email
        all_previous_notes = self.user_db.previous_notes(email)
        notes_text = ""
        for previous_note in all_previous_notes:
            date_string = previous_note[1].strftime("%Y-%m-%d")
            notes_text += date_string + "\t" + previous_note[0] + "\n"
        self.notes_label.config(text=notes_text)

    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() # Shows the parent window
