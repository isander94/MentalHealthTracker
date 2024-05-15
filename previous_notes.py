from tkinter import *
from tkinter.ttk import *
from db_connector import DatabaseManager
from datetime import datetime

class Previous_notes(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Daily Journal")
        self.geometry("900x900")
        self.notes_label = None
        self.notes_label = Label(self, text="", foreground="green")
        self.notes_label.place(x=350, y=340)
        self.user_db = DatabaseManager()
        go_back = Button(self, text="Go back", command=self.go_back)
        go_back.pack(pady=5)
        self.print_previous_notes()
            
    def print_previous_notes(self):
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
        self.master.deiconify() #