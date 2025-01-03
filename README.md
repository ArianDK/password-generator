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

### Custom
Purpose: Gives the user full control over the password generation by allowing them to customize the character set via checkboxes.
- Behavior: Passwords are generated based on the user-selected combination of character types. If no checkboxes are selected, no password is generated.
Example: R@H#Y^Q!, 384720192

