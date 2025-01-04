import tkinter as tk

def clear_widgets(root, background_image_path):
    for widget in root.winfo_children():
        widget.destroy()

    # Add the background image
    background_photo = tk.PhotoImage(file=background_image_path)
    bg_label = tk.Label(root, image=background_photo)
    bg_label.image = background_photo  # Keep a reference to avoid garbage collection
    bg_label.place(relwidth=1, relheight=1)

def set_background(root, image_path):
    """Set a background image on the root window."""
    background_photo = tk.PhotoImage(file=image_path)
    bg_label = tk.Label(root, image=background_photo)
    bg_label.image = background_photo  # Prevent garbage collection
    bg_label.place(relwidth=1, relheight=1)

def center_window(root, width, height):
    """Center the window on the screen."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def add_button(root, text, command, x, y):
    """Add a custom button at specific coordinates."""
    button = tk.Button(root, text=text, command=command, font=("Arial", 12), bg="blue", fg="white")
    button.place(x=x, y=y)
    return button

def switch_frame(current_frame, new_frame):
    """Hide the current frame and show a new one."""
    current_frame.pack_forget()
    new_frame.pack(fill="both", expand=True)

def bind_resize_event(root, callback):
    """Bind a resize event to the root window."""
    root.bind("<Configure>", lambda event: callback(event.width, event.height))

def create_frame(root, bg_color):
    """Create a frame with a specific background color."""
    frame = tk.Frame(root, bg=bg_color)
    frame.pack(fill="both", expand=True)
    return frame

def add_text_entry(root, placeholder="", x=0, y=0):
    """Add a styled text entry field with a placeholder."""
    entry = tk.Entry(root, font=("Arial", 12))
    entry.insert(0, placeholder)
    entry.place(x=x, y=y)
    return entry

def load_string_from_file(file_path):
    """Load the string from the specified file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_image(root, image_path, x, y):
    """Display an image in the root window."""
    photo = tk.PhotoImage(file=image_path)
    label = tk.Label(root, image=photo)
    label.image = photo  # Prevent garbage collection
    label.place(x=x, y=y)

def animate_widget(widget, x_start, x_end, duration):
    """Animate a widget from x_start to x_end over a duration."""
    steps = 50
    step_duration = duration // steps
    delta = (x_end - x_start) / steps

    def move(step=0):
        if step < steps:
            widget.place(x=x_start + delta * step)
            widget.after(step_duration, move, step + 1)

    move()

def toggle_visibility(widget):
    """Show or hide a widget."""
    if widget.winfo_viewable():
        widget.place_forget()
    else:
        widget.place(x=widget.winfo_x(), y=widget.winfo_y())