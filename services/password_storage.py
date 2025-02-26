import json
import os
from models.password import Password

class PasswordStorage:
    def __init__(self, encryption_manager):
        self.encryption_manager = encryption_manager
        self.filename = 'passwords.json'

    def load_passwords(self):
        try:
            with open(self.filename, 'r') as f:
                encrypted_data = json.load(f)
                decrypted_data = json.loads(self.encryption_manager.decrypt(encrypted_data))
                return [Password.from_dict(data) for data in decrypted_data]
        except FileNotFoundError:
            return []

    def save_passwords(self, passwords):
        data = [p.to_dict() for p in passwords]
        encrypted_data = self.encryption_manager.encrypt(json.dumps(data))
        with open(self.filename, 'w') as f:
            json.dump(encrypted_data, f)