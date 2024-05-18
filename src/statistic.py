from tkinter import *
from tkinter.ttk import *
from db_connector import DatabaseManager
def rgb_to_hex(rgb):
    """Convert RGB color to HEX format"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)
class Statistic(Toplevel):
    """Daily journal window."""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Statistics")
        self.geometry("900x900")
        # Background color
        bg_color = rgb_to_hex((135, 190, 128))
        self.configure(background=bg_color)
        go_back = Button(self, text="Go back", command=self.go_back)
        go_back.pack(pady=5)
        
    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #
    
    def showChart():
        pass
