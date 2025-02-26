from tkinter import Tk
from gui.main_window import MainWindow
from services.password_storage import PasswordStorage
from services.settings_manager import SettingsManager
from utils.auto_lock import AutoLock

def main():
    root = Tk()
    root.title("Password Manager")
    root.geometry("600x400")
    
    settings_manager = SettingsManager()
    encryption_manager = settings_manager.encryption_manager
    password_storage = PasswordStorage(encryption_manager)
    
    app = MainWindow(root, {
        'settings': settings_manager,
        'storage': password_storage,
        'encryption': encryption_manager,
        'auto_lock': AutoLock(root)
    })
    
    root.mainloop()

if __name__ == "__main__":
    main()