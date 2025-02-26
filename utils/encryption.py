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