import tkinter as tk
from models.password import Password
from tkinter import ttk, messagebox, filedialog
from utils.import_parser import ImportParser

class ImportWindow:
    def __init__(self, parent, password_storage):
        self.window = tk.Toplevel(parent)
        self.window.title("Configura Importazione")
        self.window.geometry("600x500")
        self.password_storage = password_storage
        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.window)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Help frame
        self.setup_help_frame(main_frame)
        
        # Format frame
        self.setup_format_frame(main_frame)
        
        # Preview frame
        self.setup_preview_frame(main_frame)
        
        # Result frame
        self.setup_result_frame(main_frame)
        
        # File selection frame
        self.setup_file_frame(main_frame)

    def setup_help_frame(self, parent):
        help_frame = ttk.LabelFrame(parent, text="Guida al formato")
        help_frame.pack(fill='x', pady=10)
        
        help_text = """
Usa le seguenti variabili per definire il formato:
$password  - Importa la password
$username  - Importa il nome utente
$service   - Importa il nome del servizio

Puoi usare qualsiasi testo come separatore. Esempi:
• password $service "username:" $username "password:" $password
• $service; $username; $password
• $service | $password

Se non specifichi una variabile, verrà usato "IMPORTATO" come valore di default.
        """
        tk.Label(help_frame, text=help_text, justify='left').pack(padx=5, pady=5)

    def setup_format_frame(self, parent):
        format_frame = ttk.LabelFrame(parent, text="Formato di importazione")
        format_frame.pack(fill='x', pady=10)
        
        self.format_var = tk.StringVar(value='password $service "$username" "$password"')
        self.format_entry = ttk.Entry(format_frame, textvariable=self.format_var, width=60)
        self.format_entry.pack(padx=5, pady=5, fill='x')

    def setup_preview_frame(self, parent):
        preview_frame = ttk.LabelFrame(parent, text="Anteprima e Test")
        preview_frame.pack(fill='x', pady=10)
        
        test_text = 'password Gmail "john.doe" "mypass123"\npassword Facebook "jane.doe" "pass456"'
        self.preview_text = tk.Text(preview_frame, height=5, wrap=tk.WORD)
        self.preview_text.insert('1.0', test_text)
        self.preview_text.pack(fill='x', padx=5, pady=5)

    def setup_result_frame(self, parent):
        result_frame = ttk.LabelFrame(parent, text="Risultato parsing")
        result_frame.pack(fill='x', pady=10)
        
        self.result_text = tk.Text(result_frame, height=5, wrap=tk.WORD)
        self.result_text.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(parent, text="Testa Formato", command=self.test_parsing).pack(pady=5)

    def setup_file_frame(self, parent):
        file_frame = ttk.Frame(parent)
        file_frame.pack(fill='x', pady=10)
        
        self.file_path_var = tk.StringVar()
        file_path_entry = ttk.Entry(
            file_frame, 
            textvariable=self.file_path_var, 
            state='readonly'
        )
        file_path_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        ttk.Button(
            file_frame, 
            text="Seleziona File", 
            command=self.select_file
        ).pack(side='right')
        
        ttk.Button(
            parent, 
            text="Importa", 
            command=self.start_import
        ).pack(pady=10)

    def test_parsing(self):
        try:
            format_string = self.format_var.get()
            test_lines = self.preview_text.get('1.0', tk.END).strip().split('\n')
            result = ""
            
            for line in test_lines:
                parsed = ImportParser.parse_line(line, format_string)
                result += f"Servizio: {parsed['service']}, "
                result += f"Username: {parsed['username']}, "
                result += f"Password: {parsed['password']}\n"
            
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert('1.0', result)
        except Exception as e:
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert('1.0', f"Errore: {str(e)}")

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Seleziona file TXT",
            filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            self.file_path_var.set(file_path)

    def start_import(self):
        file_path = self.file_path_var.get()
        if not file_path:
            messagebox.showwarning("Avviso", "Seleziona un file da importare")
            return
        
        try:
            format_string = self.format_var.get()
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            passwords = self.password_storage.load_passwords()
            imported_count = 0
            skipped_count = 0
            
            for line in lines:
                try:
                    parsed = ImportParser.parse_line(line.strip(), format_string)
                    service_exists = any(p.service == parsed['service'] for p in passwords)
                    
                    if not service_exists:
                        passwords.append(Password(**parsed))
                        imported_count += 1
                    else:
                        skipped_count += 1
                except Exception as e:
                    print(f"Errore nel processare la linea: {line}")
                    skipped_count += 1
            
            self.password_storage.save_passwords(passwords)
            messagebox.showinfo(
                "Importazione completata", 
                f"Password importate: {imported_count}\n"
                f"Password saltate (già esistenti): {skipped_count}"
            )
            self.window.destroy()
            
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante l'importazione: {str(e)}")