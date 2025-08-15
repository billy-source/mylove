import tkinter as tk
from tkinter import messagebox

class LoveMessageApp:
    def __init__(self, master):
        self.master = master
        master.title("A Message For You")
        master.geometry("400x250")
        master.configure(bg="#ffe4e1") # Soft pink background

        # Hide the main window and show a single message box
        self.show_initial_message()

    def show_initial_message(self):
        """Shows the first message box with a yes/no question."""
        self.master.withdraw() # Hide the main window
        response = messagebox.askyesno(
            "Question",
            "I have something special for you. Do you want to see it?"
        )
        if response:
            self.show_message_window()
        else:
            messagebox.showinfo(
                "Aww...",
                "Okay, maybe later. My love will be here waiting for you!"
            )
            self.master.destroy()

    def show_message_window(self):
        """Shows the main window with messages and a button."""
        self.master.deiconify() # Show the main window
        self.master.lift()
        self.master.attributes('-topmost', True) # Keep window on top
        self.master.after_idle(self.master.attributes, '-topmost', False)

        self.messages = [
            "Just wanted to remind you how much you mean to me.",
            "You bring so much light and joy into my life.",
            "Every moment with you is a gift I cherish.",
            "Thank you for being you, for everything you are.",
            "I love you more than words can say."
        ]
        self.current_message_index = 0

        # Message label
        self.label = tk.Label(
            self.master,
            text=self.messages[self.current_message_index],
            font=("Helvetica", 16, "italic"),
            bg="#ffe4e1",
            fg="#d32f2f", # Dark red text
            wraplength=350,
            justify="center"
        )
        self.label.pack(pady=40, padx=20)

        # Button
        self.button = tk.Button(
            self.master,
            text="Click for another message",
            command=self.next_message,
            font=("Helvetica", 12),
            bg="#ff6347", # Coral red button
            fg="white",
            relief="raised",
            padx=10,
            pady=5,
            bd=3
        )
        self.button.pack()

    def next_message(self):
        """Updates the label with the next message in the list."""
        self.current_message_index += 1
        if self.current_message_index < len(self.messages):
            self.label.config(text=self.messages[self.current_message_index])
        else:
            # When all messages are shown
            self.button.config(text="That's all for now!", state=tk.DISABLED)
            self.label.config(text="...but my love for you never ends. ❤️")


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Create an instance of the app
    app = LoveMessageApp(root)
    # Start the Tkinter event loop
    root.mainloop()

