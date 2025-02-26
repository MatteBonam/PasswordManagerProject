import tkinter as tk
from tkinter import ttk, messagebox
from utils.password_generator import PasswordGenerator

class PasswordGeneratorWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Generatore Password")
        self.window.geometry("400x300")
        self.setup_ui()

    def setup_ui(self):
        # Options frame
        options_frame = ttk.LabelFrame(self.window, text="Opzioni")
        options_frame.pack(padx=10, pady=5, fill='x')
        
        # Length option
        self.length_var = tk.IntVar(value=12)
        ttk.Label(options_frame, text="Lunghezza:").pack(side='left', padx=5)
        ttk.Spinbox(
            options_frame, 
            from_=8, 
            to=32, 
            textvariable=self.length_var, 
            width=5
        ).pack(side='left', padx=5)
        
        # Character type options
        self.uppercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(
            options_frame, 
            text="Maiuscole", 
            variable=self.uppercase_var
        ).pack(side='left', padx=5)
        ttk.Checkbutton(
            options_frame, 
            text="Numeri", 
            variable=self.numbers_var
        ).pack(side='left', padx=5)
        ttk.Checkbutton(
            options_frame, 
            text="Simboli", 
            variable=self.symbols_var
        ).pack(side='left', padx=5)
        
        # Result frame
        result_frame = ttk.LabelFrame(self.window, text="Password Generata")
        result_frame.pack(padx=10, pady=5, fill='x')
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            result_frame, 
            textvariable=self.password_var, 
            width=40
        )
        self.password_entry.pack(padx=5, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=10)
        
        ttk.Button(
            button_frame, 
            text="Genera", 
            command=self.generate_password
        ).pack(side='left', padx=5)
        ttk.Button(
            button_frame, 
            text="Copia", 
            command=self.copy_to_clipboard
        ).pack(side='left', padx=5)
        
        # Generate initial password
        self.generate_password()

    def generate_password(self):
        password = PasswordGenerator.generate_password(
            length=self.length_var.get(),
            use_uppercase=self.uppercase_var.get(),
            use_numbers=self.numbers_var.get(),
            use_symbols=self.symbols_var.get()
        )
        self.password_var.set(password)

    def copy_to_clipboard(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password_var.get())
        messagebox.showinfo("Info", "Password copiata negli appunti")