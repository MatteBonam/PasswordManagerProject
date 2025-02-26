import string
import random

class PasswordGenerator:
    @staticmethod
    def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
        chars = string.ascii_lowercase
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_numbers:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation
        
        password = []
        if use_uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if use_numbers:
            password.append(random.choice(string.digits))
        if use_symbols:
            password.append(random.choice(string.punctuation))
        
        remaining_length = length - len(password)
        password.extend(random.choice(chars) for _ in range(remaining_length))
        random.shuffle(password)
        return ''.join(password)