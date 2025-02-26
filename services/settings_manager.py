import json
import hashlib

class SettingsManager:
    def __init__(self, encryption_manager):
        self.encryption_manager = encryption_manager
        self.filename = 'settings.json'
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_settings(self):
        with open(self.filename, 'w') as f:
            json.dump(self.settings, f)

    def set_master_password(self, password):
        self.settings['master_password_hash'] = hashlib.sha256(password.encode()).hexdigest()
        self.settings['key'] = self.encryption_manager.key.decode()
        self.save_settings()

    def verify_master_password(self, password):
        stored_hash = self.settings.get('master_password_hash')
        if not stored_hash:
            return False
        return hashlib.sha256(password.encode()).hexdigest() == stored_hash