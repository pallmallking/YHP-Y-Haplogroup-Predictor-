import tkinter as tk
from tkinter import messagebox

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YHP")
        self.geometry("400x300")  # Set the window size

        # Create a label as a placeholder for the main content
        label = tk.Label(self, text="Welcome to YHP")
        label.pack(pady=20)

        # Bind the close event
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
