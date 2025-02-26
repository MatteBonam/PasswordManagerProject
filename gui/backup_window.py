import tkinter as tk
from tkinter import ttk, messagebox
import os
from datetime import datetime
from utils.backup_manager import BackupManager

class BackupWindow:
    def __init__(self, parent, password_manager, callback = None):
        self.callback = callback
        self.window = tk.Toplevel(parent)
        self.window.title("Gestione Backup")
        self.window.geometry("500x400")
        self.password_manager = password_manager
        self.setup_ui()

    def setup_ui(self):
        # Backup list frame
        list_frame = ttk.LabelFrame(self.window, text="Backup disponibili")
        list_frame.pack(fill='both', expand=True, padx=10, pady=5)

        # Treeview for backups
        self.backup_list = ttk.Treeview(
            list_frame, 
            columns=('Data', 'File'), 
            show='headings'
        )
        self.backup_list.heading('Data', text='Data')
        self.backup_list.heading('File', text='File')
        self.backup_list.pack(side='left', fill='both', expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            list_frame, 
            orient='vertical', 
            command=self.backup_list.yview
        )
        scrollbar.pack(side='right', fill='y')
        self.backup_list.configure(yscrollcommand=scrollbar.set)

        # Buttons
        button_frame = ttk.Frame(self.window)
        button_frame.pack(fill='x', padx=10, pady=5)

        ttk.Button(
            button_frame, 
            text="Nuovo Backup", 
            command=self.create_new_backup
        ).pack(side='left', padx=5)
        
        ttk.Button(
            button_frame, 
            text="Ripristina", 
            command=self.restore_selected_backup
        ).pack(side='left', padx=5)

        # Load initial backups
        self.load_backups()

    def load_backups(self):
        self.backup_list.delete(*self.backup_list.get_children())
        backup_dir = "backups"
        if os.path.exists(backup_dir):
            for file in os.listdir(backup_dir):
                if file.endswith('.json'):
                    try:
                        file_path = os.path.join(backup_dir, file)
                        mod_time = os.path.getmtime(file_path)
                        date = datetime.fromtimestamp(mod_time).strftime("%d/%m/%Y %H:%M:%S")
                        self.backup_list.insert('', 'end', values=(date, file))
                    except:
                        self.backup_list.insert('', 'end', values=("N/A", file))

    def create_new_backup(self):
        try:
            backup_files = BackupManager.create_backup(self.password_manager)
            self.load_backups()
            messagebox.showinfo("Backup", "Backup creato con successo")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante il backup: {str(e)}")

    def restore_selected_backup(self):
        selected = self.backup_list.selection()
        if selected:
            if messagebox.askyesno(
                "Conferma", 
                "Ripristinare il backup selezionato? I dati attuali verranno sovrascritti."
            ):
                try:
                    backup_file = self.backup_list.item(selected[0])['values'][1]
                    backup_path = os.path.join("backups", backup_file)
                    BackupManager.restore_backup(self.password_manager, [backup_path])
                    messagebox.showinfo("Ripristino", "Backup ripristinato con successo")
                    if self.callback:
                        self.callback()
                    self.window.destroy()
                except Exception as e:
                    messagebox.showerror("Errore", f"Errore durante il ripristino: {str(e)}")