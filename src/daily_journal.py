"""Module for daily journal window."""
from tkinter import *
from tkinter.ttk import *
from db_connector import DatabaseManager
def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)

class DailyJournal(Toplevel):
    """Class for Daily journal window."""


    def __init__(self, parent):
        """Initialazing the calss."""
        super().__init__(parent)
        self.title("Daily Journal")
        self.geometry("900x900")
        # Background color
        bg_color = rgb_to_hex((135, 190, 128))
        self.configure(background=bg_color)
        self.user_db = DatabaseManager()
        # For message when pressing save
        self.message_label = None
        self.message_label = Label(self, text="", foreground="red", background=bg_color)
        self.message_label.pack()

         # Label for journal entry section
        title_label = Label(self, text="Daily Journal", font=("Helvetica", 28, "bold"), foreground="white", background=bg_color)
        title_label.pack(pady=5)

        # To be able to save mood rating
        Label(self, text="How do you feel from 1-10?", font=("Helvetica", 12, "bold"), foreground="white", background=bg_color).pack(pady=10)
        self.mood_text_area = Text(self, width=5, height=2)
        self.mood_text_area.pack(padx=10, pady=10, anchor="center")


        # Label for writing area
        self.text_area = Text(self, width=50, height=20)
        self.text_area.pack(padx=10, pady=5)

        #Button to save the journal
        save_button = Button(self, text="Save note", command=self.save_entry)
        save_button.pack(pady=5)

        #Button to go back to main window
        go_back = Button(self, text="Go back", command=self.go_back)
        go_back.pack(pady=5)

        #Quit button to exit the application
        quit_button = Button(self, text="Quit", command=self.on_close)
        quit_button.pack(pady=5)

    def save_note(self):
        """function to save journal"""
        text = self.text_area.get("1.0", "end-1c")
        if (0 == len(text)) or (len(text) > 100):
            self.message_label.config(text="Please enter a note bellow or equal to 100 characters")
            return False
        else:
            if self.user_db.add_note(text, self.user_db.email):
                self.message_label.config(text="Note saved successfully")
                return True
            else:
                self.message_label.config(text="An error occured")
                return False
    
    def save_entry(self):
        """Saves an entry consisting of a note and a mood"""
        if self.save_note() or self.save_mood():
            self.go_back()
             

    def on_close(self):
        """Close the application."""
        self.destroy()
        self.master.destroy()

    def save_mood(self):
        """Save a mood rating"""
        mood = self.mood_text_area.get("1.0", "end-1c")
        if len(mood) == 0:
            self.message_label.config(text="Empty input")
        else:
            try:
                if isinstance(mood, str):
                    mood_rating_int = int(mood)
                if 1 <= mood_rating_int <= 10:
                    if self.user_db.save_mood_rating(self.user_db.email, mood_rating_int):
                        self.message_label.config(text="Mood saved successfully")
                        return True
                    else:
                        self.message_label.config(text="An error has occurred")
                        return False
                else:
                    self.message_label.config(text="Please input a valid number from 1-10")
                    return False
            except:
                self.message_label.config(text="Please input a valid number from 1-10")
                return False

    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #
