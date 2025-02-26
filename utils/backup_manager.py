import os
import shutil
from datetime import datetime

class BackupManager:
    @staticmethod
    def create_backup(app):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = "backups"
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        files_to_backup = ['passwords.json', 'settings.json']
        backup_files = []
        
        for file in files_to_backup:
            if os.path.exists(file):
                backup_name = f"{file[:-5]}_{timestamp}.json"
                backup_path = os.path.join(backup_dir, backup_name)
                shutil.copy2(file, backup_path)
                backup_files.append(backup_path)
        
        return backup_files
    
    @staticmethod
    def restore_backup(app, backup_files):
        for backup_file in backup_files:
            original_name = os.path.basename(backup_file).split('_')[0] + '.json'
            shutil.copy2(backup_file, original_name)