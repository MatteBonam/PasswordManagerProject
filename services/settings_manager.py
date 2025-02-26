import json
import hashlib

class SettingsManager:
    def __init__(self):
        self.filename = 'settings.json'
        self.encryption_manager = None
        self.master_password_hash = None
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open('settings.json', 'r') as f:
                settings = json.load(f)
                self.master_password_hash = settings.get('master_password_hash')
                stored_key = settings.get('key')
                if stored_key:
                    self.encryption_manager = EncryptionManager(stored_key.encode())
        except FileNotFoundError:
            self.encryption_manager = EncryptionManager()
            self.save_settings()

    def save_settings(self):
        settings = {
            'master_password_hash': self.master_password_hash,
            'key': self.encryption_manager.key.decode()
        }
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
    

import base64
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def encrypt(self, data):
        return self.cipher_suite.encrypt(data.encode()).decode()
    
    def decrypt(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()