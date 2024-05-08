from tkinter import *
from tkinter.ttk import *

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
        save_button = Button(self, text="Save") #,command=self.save)
        save_button.pack(pady=10)
        
        #Quit button to exit the application
        quit_button = Button(self, text="quit", command=self.on_close)
        quit_button.pack(pady=5)
        
        go_back = Button(self, text="Go back", command=self.go_back)
        go_back.pack(pady=5)

    def save():
        """function to save journal"""
        pass


    def on_close(self):
        """Close the application."""
        self.destroy()
        self.master.destroy()
    
    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #