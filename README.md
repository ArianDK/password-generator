# Password Generator
A Python-based password generator with an intuitive GUI that allows users to create secure and customizable passwords. Built with flexibility in mind, the tool offers predefined modes and a custom mode for full user control.


## Features
- Predefined modes and a custom mode.
- Password Length Customization: Adjust password length using a slider (1–50 characters).
- Clipboard Copy: Copy the generated password with a single click.
- Modern UI: Clean, user-friendly interface with centralized window positioning.


## Modes Overview

### Easy to Say
- Purpose: Generates passwords that are easier to pronounce by alternating consonants and vowels.
- Behavior: Passwords are composed only of letters (no numbers or symbols). Alternates between consonants and vowels for better readability.
Example: gunevatalo

### Easy to Read
- Purpose: Generates passwords that are less ambiguous by avoiding confusing characters (e.g., 1, l, 0, O).
- Behavior: Passwords avoid ambiguous characters such as I, l, 0, O, 1. Includes a mix of uppercase, lowercase, and numbers but excludes symbols.
Example: Trembing7ace
All Characters
Purpose: Generates passwords with maximum randomness using all available characters (letters, numbers, and symbols).
- Behavior: Passwords are generated using uppercase letters, lowercase letters, numbers, and symbols.
Example: 9~Tk?me^AxB

### All Characters
Purpose: Generates passwords with maximum randomness using all available characters (letters, numbers, and symbols).
Behavior:
Passwords are generated using: Uppercase letters, Lowercase letters, Numbers and Symbols.
Example: 9~Tk?me^AxB

### Custom
Purpose: Gives the user full control over the password generation by allowing them to customize the character set via checkboxes.
- Behavior: Passwords are generated based on the user-selected combination of character types. If no checkboxes are selected, no password is generated.
Example: R@H#Y^Q!, 384720192

## Instalation (Create Standalone Executable)
It is assumed that Python and pip are installed on your system.

Follow these steps to set up and run the **Password Generator** on your computer:

1. Download the repository as a zip file and unzip it.
2. Open your terminal or command prompt and navigate to the password generator directory by typing `cd path/to/your/directory/password-generator-main`.
3. In the command prompt now type `pip install -r requirements.txt` to download the required packages.
4. Now you should type `pyinstaller --onefile --noconsole --add-data "assets/icon.png;assets" --add-data "assets/icon.ico;assets" --hidden-import "ttkbootstrap" --icon "assets/icon.ico" --distpath . "Password Generator.py" & rmdir /s /q build & del "Password Generator.spec"` to install the Password Generator as a standalone executable.
4. Now the Password Generator.exe file should be in password-generator-main and you can run it.


## File Structure
- Password Generator.py: Entry point to run the application.
- gui.py: Defines the graphical user interface.
- gui_functions.py: Contains core logic for password generation and functionality.
- assets/: Directory for resources like the application icon.

## Troubleshooting
- **Add PyInstaller to PATH**: If you encounter the error `'pyinstaller' is not recognized as an internal or external command, operable program or batch file`, you need to add the PyInstaller directory to your system's PATH.
- **Missing Dependencies**: If the application fails due to missing dependencies, ensure all packages in `requirements.txt` are installed. Run `pip list` in the command prompt.
- **Windows antivirus**: If Windows antivirus blocks pyinstaller from turning the code into a standalone excecutable: Click the popup "Allow on device", then "Start action".
