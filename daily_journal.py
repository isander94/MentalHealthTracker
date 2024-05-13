from tkinter import *
from tkinter.ttk import *
from db_connector import DatabaseManager
def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)

class DailyJournal(Toplevel):
    """Daily journal window."""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Daily Journal")
        self.geometry("900x900")
        # Background color
        bg_color = rgb_to_hex((120, 163, 156))
        self.configure(background=bg_color)
        self.user_db = DatabaseManager()
        # For message when pressing save
        self.message_label = None
        self.message_label = Label(self, text="", foreground="red")
        self.message_label.pack()
        
        # Frame and alignment for "Mood buttons"
        mood_frame = Frame(self)
        mood_frame.pack(pady=10)
        
        # Mood rating buttons
        self.mood_buttons = []
        for i in range(1, 11):
            btn = Button(mood_frame, text=str(i), width=2)
            btn.pack(side="left", padx=5)
            self.mood_buttons.append(btn)

         # Label for journal entry section
        Label(self, text="Daily journal text").pack(pady=10)
        
        # Label for writing area
        self.text_area = Text(self, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)
        
        #Button to save the journal
        save_button = Button(self, text="Save", command=self.save) #,command=self.save)
        save_button.pack(pady=10)
        previous_notes_button = Button(self, text="Previous notes", command=self.previous_notes) #,command=self.save)
        previous_notes_button.pack(pady=20)
        #Quit button to exit the application
        quit_button = Button(self, text="quit", command=self.on_close)
        quit_button.pack(pady=5)
        
        go_back = Button(self, text="Go back", command=self.go_back)
        go_back.pack(pady=5)

    def save(self):
        """function to save journal"""
        text = self.text_area.get("1.0", "end-1c")
        if self.user_db.add_note(text):
            self.message_label.config(text="Note saved successfully")
        else:
            self.message_label.config(text="An error occured")
            
    def on_close(self):
        """Close the application."""
        self.destroy()
        self.master.destroy()
    
    def previous_notes(self):
        previous_notes = self.user_db.previous_notes()
        
    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #
