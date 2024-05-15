from tkinter import *
from tkinter.ttk import *
from db_connector import DatabaseManager

class Statistic(Toplevel):
    """Daily journal window."""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Statistics")
        self.geometry("900x900")
        # Background color
        go_back = Button(self, text="Go back", command=self.go_back)
        go_back.pack(pady=5)
        
    def go_back(self):
        """Function is used to go back to the login window"""
        self.destroy() # closes the sign up window
        self.master.deiconify() #
    
    def showChart():
        pass
