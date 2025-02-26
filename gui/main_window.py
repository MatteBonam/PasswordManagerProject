import tkinter as tk
from tkinter import ttk, messagebox
from gui.password_generator_window import PasswordGeneratorWindow
from gui.import_window import ImportWindow
from gui.backup_window import BackupWindow

class MainWindow:
    def __init__(self, master, password_manager):
        self.master = master
        self.password_manager = password_manager
        self.setup_ui()

    def setup_ui(self):
        # Setup main interface layout and components
        main_frame = ttk.Frame(self.master)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Password list
        self.setup_password_list(main_frame)
        
        # Buttons
        self.setup_buttons(main_frame)

    def setup_password_list(self, parent):
        list_frame = ttk.Frame(parent)
        list_frame.pack(side='left', fill='both', expand=True)
        
        tk.Label(list_frame, text="Le tue password", font=('Arial', 12)).pack()
        
        self.password_list = ttk.Treeview(list_frame, columns=('Servizio', 'Username'), show='headings')
        self.password_list.heading('Servizio', text='Servizio')
        self.password_list.heading('Username', text='Username')
        self.password_list.pack(pady=5, fill='both', expand=True)
        self.refresh_password_list()

    def setup_buttons(self, parent):
        button_frame = ttk.Frame(parent)
        button_frame.pack(side='right', padx=10)
        
        buttons = [
            ("Aggiungi", self.show_add_password),
            ("Modifica", self.show_edit_password),
            ("Elimina", self.delete_password),
            ("Visualizza", self.show_password),
            ("Importa da TXT", self.show_import_window),
            ("Backup/Ripristino", self.show_backup_manager)
        ]
        
        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command).pack(pady=5)

    def show_add_password(self):
        from gui.password_dialogs import AddPasswordDialog
        AddPasswordDialog(self.master, self.password_manager, self.refresh_password_list)

    def show_edit_password(self):
        selected = self.password_list.selection()
        if not selected:
            messagebox.showwarning("Avviso", "Seleziona una password da modificare")
            return

        selected_item = self.password_list.item(selected[0])
        selected_service = selected_item['values'][0]
        selected_username = selected_item['values'][1]

        # Find the password object
        passwords = self.password_manager['storage'].load_passwords()
        selected_password = next((p for p in passwords if p.service == selected_service and p.username == selected_username), None)

        if not selected_password:
            messagebox.showerror("Errore", "Password non trovata")
            return

        from gui.password_dialogs import EditPasswordDialog
        EditPasswordDialog(self.master, self.password_manager, selected_password, self.refresh_password_list)

    def show_password(self):
        selected = self.password_list.selection()
        if not selected:
            messagebox.showwarning("Avviso", "Seleziona una password da visualizzare")
            return

        selected_item = self.password_list.item(selected[0])
        selected_service = selected_item['values'][0]
        selected_username = selected_item['values'][1]

        # Find the password object
        passwords = self.password_manager['storage'].load_passwords()
        selected_password = next((p for p in passwords if p.service == selected_service and p.username == selected_username), None)

        if not selected_password:
            messagebox.showerror("Errore", "Password non trovata")
            return

        from gui.password_dialogs import ViewPasswordDialog
        ViewPasswordDialog(self.master, selected_password)

    def delete_password(self):
        selected = self.password_list.selection()
        if not selected:
            messagebox.showwarning("Avviso", "Seleziona una password da eliminare")
            return

        selected_item = self.password_list.item(selected[0])
        selected_service = selected_item['values'][0]
        selected_username = selected_item['values'][1]

        if messagebox.askyesno("Conferma", "Sei sicuro di voler eliminare questa password?"):
            passwords = self.password_manager['storage'].load_passwords()
            passwords = [p for p in passwords if p.service != selected_service or p.username != selected_username]
            self.password_manager['storage'].save_passwords(passwords)
            self.refresh_password_list()

    def refresh_password_list(self):
        # Clear existing items
        for item in self.password_list.get_children():
            self.password_list.delete(item)

        # Load and display passwords
        passwords = self.password_manager['storage'].load_passwords()
        for password in passwords:
            self.password_list.insert('', 'end', values=(password.service, password.username))

    def show_import_window(self):
        from gui.import_window import ImportWindow
        ImportWindow(self.master, self.password_manager['storage'])
    def show_backup_manager():
        pass