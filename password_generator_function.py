import random
import string

def generate_password(length=12, mode="all_characters", include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    if length < 1:
        return ""
    
    # Define character pools
    all_characters = string.ascii_letters + string.digits + string.punctuation
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    easy_to_read = string.ascii_uppercase.replace("I", "").replace("O", "") + \
                   string.ascii_lowercase.replace("l", "").replace("o", "") + \
                   string.digits.replace("1", "").replace("0", "")
    
    if mode == "easy_to_say":
        # Generate alternating consonants and vowels in lowercase
        password = ""
        for i in range(length):
            if i % 2 == 0:  # Even index: consonant
                password += random.choice(consonants)
            else:  # Odd index: vowel
                password += random.choice(vowels)
        return password if include_lowercase else password.upper()
    
    elif mode == "easy_to_read":
        # Exclude ambiguous characters
        character_pool = easy_to_read
        password = ''.join(random.choices(character_pool, k=length))
        return password
    
    elif mode == "custom":
        # Use checkboxes to define character pool
        character_pool = ""
        if include_uppercase:
            character_pool += string.ascii_uppercase
        if include_lowercase:
            character_pool += string.ascii_lowercase
        if include_numbers:
            character_pool += string.digits
        if include_symbols:
            character_pool += string.punctuation

        if not character_pool:  # If no checkboxes selected, return an empty string
            return ""
        
        password = ''.join(random.choices(character_pool, k=length))
        return password

    # Adjust character pool for "All Characters" mode
    character_pool = all_characters
    if not include_uppercase:
        character_pool = character_pool.replace(string.ascii_uppercase, "")
    if not include_lowercase:
        character_pool = character_pool.replace(string.ascii_lowercase, "")
    if not include_numbers:
        character_pool = character_pool.replace(string.digits, "")
    if not include_symbols:
        character_pool = character_pool.replace(string.punctuation, "")

    # Generate password for "All Characters" mode
    password = ''.join(random.choices(character_pool, k=length))
    return password
