import tkinter as tk

from tkinter import ttk

from PIL import Image, ImageTk
from tkinter import Toplevel, messagebox
from src.spell_check import *
from src.mail_process import *
from src.init import *
import win32crypt

# Function to open the message dialog
def open_message_dialog():
    # Create a new dialog window
    dialog = Toplevel(root)
    dialog.title("Send a Message")
    dialog.geometry("400x300")

    # Add UI components for message dialog
    tk.Label(dialog, text="Recipient (Email):", font=("Arial", 14)).pack(pady=10)
    recipient_entry = tk.Entry(dialog, font=("Arial", 12))
    recipient_entry.pack(pady=5, fill="x", padx=10)

    tk.Label(dialog, text="Message:", font=("Arial", 14)).pack(pady=10)
    message_text = tk.Text(dialog, height=5, font=("Arial", 12))
    message_text.pack(pady=5, fill="x", padx=10)

    def send_dm():
        recipient = recipient_entry.get()
        message = message_text.get("1.0", tk.END).strip()

        # Validate email format
        if not recipient or not is_valid_email(recipient):
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            recipient_entry.focus_set()  # Keep the focus on the email input field
            return
        if not message:
            messagebox.showwarning("Error", "Please fill out the message field.")
            message_text.focus_set()  # Keep the focus on the message field
            return

        # Replace this with your actual sending logic
        messagebox.showinfo("Success", f"Message sent to {recipient}:\n\n{message}")

        # Call clear_widgets to only show the background image
        background_image_path = "background.jpg"
        clear_widgets(root, background_image_path)
        dialog.destroy()

    tk.Button(dialog, text="Send", command=send_dm, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

###################################
clear_widget()
# Initialize the main Tkinter window

root = tk.Tk()
root.title("Merry Christmas 2025")
root.geometry("800x600")

# Set the background image
background_image = Image.open("background.jpg")  # Replace with your image path
background_photo = ImageTk.PhotoImage(background_image.resize((800, 600)))

bg_label = tk.Label(root, image=background_photo)
bg_label.place(relwidth=1, relheight=1)

# Create a style for the button
style = ttk.Style()
style.configure('Rounded.TButton', font=('Arial', 12), borderwidth=0, relief='flat',  foreground='black')

# Add a button on the background
open_dialog_button = ttk.Button(root, text="Send Message", style='Rounded.TButton', command=open_message_dialog)
open_dialog_button.place(relx=0.5, rely=0.9, anchor="center")

# Run the Tkinter event loop
root.mainloop()
