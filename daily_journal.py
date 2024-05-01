from tkinter import *
from tkinter.ttk import *

class DailyJournal(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Daily Journal")
        self.geometry("900x900")
        
        Label(self, text="Daily journal text").pack(pady=10)
        
        self.text_area = Text(self, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)
        
        save_button = Button(self, text="Save") ,#command=self.save)
        save_button.pack(pady=10)
        
    def save():
        pass