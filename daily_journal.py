from tkinter import *
from tkinter.ttk import *

class DailyJournal(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Daily Journal")
        self.geometry("900x900")
        
        bg_color = rgb_to_hex((120, 163, 156))
        self.configure(background=bg_color)
       
        mood_frame = Frame(self)
        mood_frame.pack(pady=10)
        
        self.mood_buttons = []
        for i in range(1, 11):
            btn = Button(mood_frame, text=str(i), width=2)
            btn.pack(side="left", padx=5)
            self.mood_buttons.append(btn)

        Label(self, text="Daily journal text").pack(pady=10)
        
        self.text_area = Text(self, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)
        
        save_button = Button(self, text="Save") #,command=self.save)
        save_button.pack(pady=10)
        
        quit_button = Button(self, text="quit", command=self.on_close)
        quit_button.pack(pady=5)

    def save():
        pass

    def on_close(self):
        self.destroy()
        self.master.destroy()

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)
