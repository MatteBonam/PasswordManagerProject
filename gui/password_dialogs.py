import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.password import Password

class AddPasswordDialog:
    def __init__(self, parent, password_manager, callback=None):
        self.parent = parent
        self.password_manager = password_manager
        self.callback = callback
        self.dialog = None
        self.create_dialog()
    
    def create_dialog(self):
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("Aggiungi Password")
        self.dialog.geometry("300x250")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Input fields
        tk.Label(self.dialog, text="Servizio:").pack(pady=(10, 0))
        self.service_entry = tk.Entry(self.dialog, width=30)
        self.service_entry.pack(pady=5)
        
        tk.Label(self.dialog, text="Username:").pack()
        self.username_entry = tk.Entry(self.dialog, width=30)
        self.username_entry.pack(pady=5)
        
        tk.Label(self.dialog, text="Password:").pack()
        self.password_entry = tk.Entry(self.dialog, width=30)
        self.password_entry.pack(pady=5)
        
        # Generate password button
        generate_button = ttk.Button(self.dialog, text="Genera", command=self.generate_password)
        generate_button.pack(pady=5)
        
        # Buttons
        buttons_frame = ttk.Frame(self.dialog)
        buttons_frame.pack(pady=10, fill='x')
        
        save_button = ttk.Button(buttons_frame, text="Salva", command=self.save_password)
        save_button.pack(side='right', padx=5)
        
        cancel_button = ttk.Button(buttons_frame, text="Annulla", command=self.dialog.destroy)
        cancel_button.pack(side='right', padx=5)
    
    def generate_password(self):
        from utils.password_generator import PasswordGenerator
        password = PasswordGenerator.generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
    
    def save_password(self):
        service = self.service_entry.get().strip()
        username = self.username_entry.get().strip()
        password_value = self.password_entry.get()
        
        if not service:
            tk.messagebox.showerror("Errore", "Il campo Servizio è obbligatorio")
            return
        
        password = Password(service, username, password_value)
        
        # Retrieve existing passwords
        storage = self.password_manager['storage']
        passwords = storage.load_passwords()
        
        # Check for duplicates
        for existing in passwords:
            if existing.service == service and existing.username == username:
                result = tk.messagebox.askyesno(
                    "Conferma", 
                    f"Esiste già una password per il servizio '{service}' e utente '{username}'. Vuoi sovrascriverla?"
                )
                if not result:
                    return
                passwords.remove(existing)
                break
        
        # Add new password and save
        passwords.append(password)
        storage.save_passwords(passwords)
        
        if self.callback:
            self.callback()
        
        self.dialog.destroy()

class EditPasswordDialog:
    def __init__(self, parent, password_manager, password, callback=None):
        self.parent = parent
        self.password_manager = password_manager
        self.password = password
        self.callback = callback
        self.dialog = None
        self.create_dialog()
    
    def create_dialog(self):
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("Modifica Password")
        self.dialog.geometry("300x250")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Input fields
        tk.Label(self.dialog, text="Servizio:").pack(pady=(10, 0))
        self.service_entry = tk.Entry(self.dialog, width=30)
        self.service_entry.insert(0, self.password.service)
        self.service_entry.pack(pady=5)
        
        tk.Label(self.dialog, text="Username:").pack()
        self.username_entry = tk.Entry(self.dialog, width=30)
        self.username_entry.insert(0, self.password.username)
        self.username_entry.pack(pady=5)
        
        tk.Label(self.dialog, text="Password:").pack()
        self.password_entry = tk.Entry(self.dialog, width=30)
        self.password_entry.insert(0, self.password.password)
        self.password_entry.pack(pady=5)
        
        # Generate password button
        generate_button = ttk.Button(self.dialog, text="Genera Nuova", command=self.generate_password)
        generate_button.pack(pady=5)
        
        # Buttons
        buttons_frame = ttk.Frame(self.dialog)
        buttons_frame.pack(pady=10, fill='x')
        
        save_button = ttk.Button(buttons_frame, text="Aggiorna", command=self.update_password)
        save_button.pack(side='right', padx=5)
        
        cancel_button = ttk.Button(buttons_frame, text="Annulla", command=self.dialog.destroy)
        cancel_button.pack(side='right', padx=5)
    
    def generate_password(self):
        from utils.password_generator import PasswordGenerator
        password = PasswordGenerator.generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
    
    def update_password(self):
        service = self.service_entry.get().strip()
        username = self.username_entry.get().strip()
        password_value = self.password_entry.get()
        
        if not service or not username or not password_value:
            messagebox.showerror("Errore", "Riempire tutti i campi")
            return
        
        # Retrieve existing passwords
        storage = self.password_manager['storage']
        passwords = storage.load_passwords()
        
        # Remove old password
        for i, existing in enumerate(passwords):
            if existing.service == self.password.service and existing.username == self.password.username:
                passwords.pop(i)
                break
        
        # If service name changed, check for duplicates
        if service != self.password.service or username != self.password.username:
            for existing in passwords:
                if existing.service == service and existing.username == username:
                    result = messagebox.askyesno(
                        "Conferma", 
                        f"Esiste già una password per il servizio '{service}' e utente '{username}'. Vuoi sovrascriverla?"
                    )
                    if not result:
                        return
                    passwords.remove(existing)
                    break
        
        # Add updated password and save
        updated_password = Password(service, username, password_value)
        passwords.append(updated_password)
        storage.save_passwords(passwords)
        
        if self.callback:
            self.callback()
        
        self.dialog.destroy()

import tkinter as tk
from tkinter import ttk

class ViewPasswordDialog:
    def __init__(self, parent, password):
        self.parent = parent
        self.password = password
        self.dialog = None
        self.create_dialog()
    
    def create_dialog(self):
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("Visualizza Password")
        self.dialog.geometry("350x250")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Create frame for information
        info_frame = ttk.Frame(self.dialog, padding=20)
        info_frame.pack(fill='both', expand=True)
        
        # Service info
        ttk.Label(info_frame, text="Servizio:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        ttk.Label(info_frame, text=self.password.service).grid(row=0, column=1, sticky='w', pady=5)
        
        # Username info
        ttk.Label(info_frame, text="Username:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        ttk.Label(info_frame, text=self.password.username).grid(row=1, column=1, sticky='w', pady=5)
        
        # Password info with show/hide toggle
        ttk.Label(info_frame, text="Password:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
        
        password_frame = ttk.Frame(info_frame)
        password_frame.grid(row=2, column=1, sticky='w', pady=5)
        
        self.password_var = tk.StringVar(value="•" * len(self.password.password))
        self.show_password = False
        
        password_label = ttk.Label(password_frame, textvariable=self.password_var)
        password_label.pack(side='left')
        
        def toggle_password():
            self.show_password = not self.show_password
            if self.show_password:
                self.password_var.set(self.password.password)
                show_btn.config(text="Nascondi")
            else:
                self.password_var.set("•" * len(self.password.password))
                show_btn.config(text="Mostra")
        
        show_btn = ttk.Button(password_frame, text="Mostra", width=8, command=toggle_password)
        show_btn.pack(side='left', padx=5)
        
        def copy_to_clipboard():
            self.dialog.clipboard_clear()
            self.dialog.clipboard_append(self.password.password)
            ttk.Label(info_frame, text="Copiato!", foreground='green').grid(row=3, column=1, sticky='w', pady=5)
        
        # Copy and close buttons
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(pady=10, fill='x')
        
        copy_button = ttk.Button(button_frame, text="Copia Password", command=copy_to_clipboard)
        copy_button.pack(side='left', padx=5)
        
        close_button = ttk.Button(button_frame, text="Chiudi", command=self.dialog.destroy)
        close_button.pack(side='right', padx=5)