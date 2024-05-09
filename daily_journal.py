import customtkinter

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


class DailyJournal(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Daily Journal")
        self.geometry("1200x900")  # Window size
        
        bg_color = rgb_to_hex((120, 163, 156))  # Background color
        self.configure(bg_color=bg_color)  # Apply background color to the main window

        
        # Label with consistent background
        label = customtkinter.CTkLabel(self, text="Journal", text_color=bg_color)
        label.pack(pady=20)

        # Text area with the same background color as the window for consistency
        self.text_area = customtkinter.CTkTextbox(self, width=800, height=400, fg_color="light grey", text_color="black")
        self.text_area.pack(pady=10)

        # Frame for buttons with the same background color
        button_frame = customtkinter.CTkFrame(self, bg_color=bg_color)
        button_frame.pack(fill='x', padx=20, pady=12)

        # Save button
        save_button = customtkinter.CTkButton(button_frame, text="Save", command=self.save_entry, bg_color=bg_color, fg_color=bg_color, hover_color="#AAAAAA", text_color="black")
        save_button.pack(side="bottom", padx=1, pady=5)

        # Close button
        close_button = customtkinter.CTkButton(button_frame, text="Close", command=self.quit, bg_color=bg_color, fg_color=bg_color, hover_color="#AAAAAA", text_color="black")
        close_button.pack(side="bottom", padx=100, pady=5)

    def save_entry(self):
        # Placeholder function for saving the journal entry
        pass

# Create and run the application window
