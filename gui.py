import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.messagebox import showinfo
from gui_functions import (
    update_password,
    generate_new_password,
    on_slider_change,
    on_spinbox_change,
    sync_checkboxes,
    copy_to_clipboard,
    update_progress_bar,
)

# Root window
root = ttk.Window(themename="simplex")
root.title("Password Generator")

# Set the application icon
try:
    root.iconphoto(False, ttk.PhotoImage(file="./assets/icon.png"))
except Exception as e:
    print(f"Failed to set icon: {e}")

# Center the window on the screen
window_width = 660
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False, False)

# Password display box
password_var = ttk.StringVar(value="YourGeneratedPasswordHere")
password_display = ttk.Entry(root, textvariable=password_var, font=("Arial", 14), justify="center", state="readonly", width=35)
password_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Password strength progress bar
progress_bar = ttk.Progressbar(root, length=600, mode="determinate", bootstyle="info")
progress_bar.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
update_progress_bar(progress_bar, len(password_var.get()))

# Generate New Password Button
generate_btn = ttk.Button(root, text="Generate", command=lambda: generate_new_password(
    password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar
), bootstyle=PRIMARY)
generate_btn.grid(row=0, column=3, padx=5)

# Copy Button
copy_btn = ttk.Button(root, text="Copy", command=lambda: copy_to_clipboard(password_var.get(), root), bootstyle=SUCCESS)
copy_btn.grid(row=0, column=4, padx=5)

# Customization area
customization_frame = ttk.LabelFrame(root, text="Password Customization", padding=(10, 10))
customization_frame.grid(row=2, column=0, columnspan=6, padx=10, pady=10, sticky="ew")

# Password length slider
ttk.Label(customization_frame, text="Password Length:").grid(row=0, column=0, sticky="w")
password_length = ttk.IntVar(value=12)
length_slider = ttk.Scale(
    customization_frame,
    from_=1,
    to=35,
    variable=password_length,
    orient="horizontal",
    command=lambda value: on_slider_change(value, password_length, length_spinbox, password_var, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar),
    length=400
)
length_slider.grid(row=0, column=1, columnspan=3, sticky="ew", padx=5)

# Password length spinbox
length_spinbox = ttk.Spinbox(
    customization_frame,
    from_=1,
    to=35,
    textvariable=password_length,
    width=3,
    command=lambda: on_spinbox_change(password_length, length_slider, password_var, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar),
    increment=1  # Ensures integer increments
)
length_spinbox.grid(row=0, column=4, padx=5, pady=5, sticky="w")

# Mode radio buttons
mode_var = ttk.StringVar(value="all_characters")
ttk.Label(customization_frame, text="Mode:").grid(row=1, column=0, sticky="w")
modes = [("Easy to Say", "easy_to_say"), ("Easy to Read", "easy_to_read"), ("All Characters", "all_characters"), ("Custom", "custom")]
for i, (label, mode) in enumerate(modes):
    ttk.Radiobutton(
        customization_frame,
        text=label,
        variable=mode_var,
        value=mode,
        command=lambda: sync_checkboxes(mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, lowercase_check, uppercase_check, numbers_check, symbols_check, password_var, password_length, progress_bar)
    ).grid(row=1, column=i + 1, sticky="w", padx=5, pady=5)

# Checkbox options
lowercase_var = ttk.BooleanVar(value=True)
uppercase_var = ttk.BooleanVar(value=True)
numbers_var = ttk.BooleanVar(value=True)
symbols_var = ttk.BooleanVar(value=True)

lowercase_check = ttk.Checkbutton(customization_frame, text="Lowercase", variable=lowercase_var, command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar))
lowercase_check.grid(row=2, column=0, sticky="w", padx=5, pady=5)
uppercase_check = ttk.Checkbutton(customization_frame, text="Uppercase", variable=uppercase_var, command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar))
uppercase_check.grid(row=2, column=1, sticky="w", padx=5, pady=5)
numbers_check = ttk.Checkbutton(customization_frame, text="Numbers", variable=numbers_var, command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar))
numbers_check.grid(row=2, column=2, sticky="w", padx=5, pady=5)
symbols_check = ttk.Checkbutton(customization_frame, text="Symbols", variable=symbols_var, command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar))
symbols_check.grid(row=2, column=3, sticky="w", padx=5, pady=5)

# Initialize password and sync checkboxes on startup
sync_checkboxes(mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, lowercase_check, uppercase_check, numbers_check, symbols_check, password_var, password_length, progress_bar)

if __name__ == "__main__":
    root.mainloop()
