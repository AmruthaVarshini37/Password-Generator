import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
        random.choice(letters.upper())
    ]

   
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 4)

   
    random.shuffle(password)

    return ''.join(password)

print("Generated password:", generate_password(16))