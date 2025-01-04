from password_generator_function import generate_password
from tkinter.messagebox import showinfo

# Track the last length and mode
last_selected_mode = None
last_length = None

def update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar, force_update=False):
    """Update the password whenever a setting changes."""
    global last_length
    length = password_length.get()

    # Skip update if the length hasn't changed and force_update is False
    if not force_update and length == last_length:
        return

    last_length = length  # Update last_length

    mode = mode_var.get()
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    new_password = generate_password(
        length=length,
        mode=mode,
        include_lowercase=include_lowercase,
        include_uppercase=include_uppercase,
        include_numbers=include_numbers,
        include_symbols=include_symbols
    )
    password_var.set(new_password)
    update_progress_bar(progress_bar, length)

def generate_new_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar):
    """Forcefully generate a new password."""
    update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar, force_update=True)

def on_slider_change(value, password_length, length_spinbox, password_var, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar):
    """Synchronize the spinbox when the slider value changes."""
    value = int(float(value))  # Force integer value
    password_length.set(value)
    length_spinbox.set(value)
    update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar)

def on_spinbox_change(password_length, length_slider, password_var, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar):
    """Synchronize the slider when the spinbox value changes."""
    value = int(password_length.get())
    length_slider.set(value)
    update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar)

def update_progress_bar(progress_bar, password_length):
    """Update the progress bar based on the password length."""
    if password_length <= 2:
        progress_bar.configure(value=10, bootstyle="red")  # Red
    elif 3 <= password_length <= 4:
        progress_bar.configure(value=30, bootstyle="red")  # Yellow
    elif 5 <= password_length <= 6:
        progress_bar.configure(value=50, bootstyle="warning")  # Yellow
    elif 7 <= password_length <= 9:
        progress_bar.configure(value=75, bootstyle="success")  # Green
    elif password_length >= 10:
        progress_bar.configure(value=100, bootstyle="success")  # Green
    else:
        progress_bar.configure(value=0)  # Default empty

def sync_checkboxes(mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, lowercase_check, uppercase_check, numbers_check, symbols_check, password_var, password_length, progress_bar):
    """Sync checkboxes and generate a new password when a radio button or checkbox is pressed."""
    """Sync checkboxes and generate a new password when a radio button is pressed."""
    """Sync checkboxes based on the selected radio button."""
    global last_selected_mode
    mode = mode_var.get()

    # If the mode hasn't changed, do nothing
    if mode == last_selected_mode:
        return

    last_selected_mode = mode  # Update the last selected mode

    if mode == "easy_to_say":
        lowercase_var.set(True)
        uppercase_var.set(False)
        numbers_var.set(False)
        symbols_var.set(False)
        lowercase_check.config(state="disabled")
        uppercase_check.config(state="disabled")
        numbers_check.config(state="disabled")
        symbols_check.config(state="disabled")
    elif mode == "easy_to_read":
        lowercase_var.set(True)
        uppercase_var.set(True)
        numbers_var.set(True)
        symbols_var.set(False)
        lowercase_check.config(state="disabled")
        uppercase_check.config(state="disabled")
        numbers_check.config(state="disabled")
        symbols_check.config(state="disabled")
    elif mode == "all_characters":
        lowercase_var.set(True)
        uppercase_var.set(True)
        numbers_var.set(True)
        symbols_var.set(True)
        lowercase_check.config(state="disabled")
        uppercase_check.config(state="disabled")
        numbers_check.config(state="disabled")
        symbols_check.config(state="disabled")
    elif mode == "custom":
        lowercase_check.config(state="normal", command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar, force_update=True))
        uppercase_check.config(state="normal", command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar, force_update=True))
        numbers_check.config(state="normal", command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar, force_update=True))
        symbols_check.config(state="normal", command=lambda: update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar, force_update=True))

    update_password(password_var, password_length, mode_var, lowercase_var, uppercase_var, numbers_var, symbols_var, progress_bar, force_update=True)

def copy_to_clipboard(password, root):
    """Copy the generated password to clipboard."""
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        showinfo("Copied", "Password copied to clipboard!")
