import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QFrame, QScrollArea, QSizePolicy,
                           QGridLayout, QTabWidget, QProgressBar, QSpacerItem)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QFont, QLinearGradient, QGradient

class PasswordManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.setMinimumSize(900, 600)
        self.setStyleSheet("""
            QMainWindow { background-color: #1e1e1e; color: white; }
            QLabel { color: white; }
            QLineEdit { 
                background-color: #323232; 
                color: white; 
                border-radius: 4px; 
                padding: 8px; 
                border: none;
            }
            QPushButton { 
                background-color: #323232; 
                color: white; 
                border-radius: 4px; 
                padding: 8px 16px; 
                border: none;
            }
            QPushButton:hover { background-color: #424242; }
            QPushButton#unlockButton { 
                background-color: #000000; 
                color: white; 
                border-radius: 4px; 
                padding: 10px; 
            }
            QPushButton#newButton { 
                background-color: #323232; 
                border-radius: 12px; 
                color: white; 
                padding: 4px 8px; 
            }
            QFrame#card { 
                background-color: #2d2d2d; 
                border-radius: 10px; 
                padding: 4px; 
            }
            QProgressBar {
                border: none;
                border-radius: 4px;
                background-color: #424242;
                height: 6px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4f9fee;
                border-radius: 4px;
            }
        """)

        # Inizializza l'interfaccia
        self.initUI()

    def initUI(self):
        # Crea un widget stack per gestire le diverse pagine
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Layout principale
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Pagina di login
        self.login_page = QWidget()
        self.setup_login_page()
        
        # Pagina principale
        self.main_page = QWidget()
        self.setup_main_page()
        
        # Aggiungi lo stack al layout principale
        self.main_layout.addWidget(self.login_page)
        

    def setup_login_page(self):
        # Layout principale per la pagina di login
        login_layout = QHBoxLayout(self.login_page)
        
        # Layout sinistro (con l'icona del lucchetto)
        left_widget = QWidget()
        left_widget.setStyleSheet("background-color: #3a3a3a; border-radius: 10px;")
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Icona del lucchetto
        lock_label = QLabel()
        lock_pixmap = QPixmap("lock_icon.png")  # Sostituisci con il percorso dell'icona
        if lock_pixmap.isNull():
            # Se l'icona non è disponibile, mostra solo testo
            lock_label = QLabel("🔒")
            lock_label.setStyleSheet("font-size: 48px; color: gold;")
        else:
            lock_label.setPixmap(lock_pixmap.scaled(128, 128, Qt.AspectRatioMode.KeepAspectRatio))
        
        # Label per "PassManager"
        title_label = QLabel("Password Master")
        title_label.setStyleSheet("color: white; font-size: 16px; margin-top: 10px;")
        
        # Aggiungi elementi al layout sinistro
        left_layout.addWidget(lock_label, 0, Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(title_label, 0, Qt.AlignmentFlag.AlignCenter)
        
        # Layout destro (form di login)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.setContentsMargins(50, 50, 50, 50)
        
        # Titolo "Log in"
        login_title = QLabel("Log in")
        login_title.setStyleSheet("font-size: 24px; color: white; margin-bottom: 20px;")
        
        # Form di login
        master_label = QLabel("Username")
        master_label.setStyleSheet("font-size: 14px; color: #aaaaaa; margin-bottom: 8px;")
        
        master_input = QLineEdit()
        master_input.setPlaceholderText("Enter your username")
        master_input.setFixedHeight(40)
        master_input.setContentsMargins(10, 0, 10, 0)
        
        password_label = QLabel("Password")
        password_label.setStyleSheet("font-size: 14px; color: #aaaaaa; margin-top: 15px; margin-bottom: 8px;")
        
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setFixedHeight(40)
        password_input.setContentsMargins(10, 0, 10, 0)
        
        # Pulsante di sblocco
        unlock_button = QPushButton("Login")
        unlock_button.setObjectName("loginButton")
        unlock_button.setStyleSheet("margin-top: 20px;")
        
        # Aggiungi elementi al layout destro
        right_layout.addStretch()
        right_layout.addWidget(login_title, 0, Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(master_label)
        right_layout.addWidget(master_input)
        right_layout.addWidget(password_label)
        right_layout.addWidget(password_input)
        right_layout.addWidget(unlock_button)
        right_layout.addStretch()
        
        # Aggiungi widget al layout principale della pagina di login
        login_layout.addWidget(left_widget, 1)
        login_layout.addWidget(right_widget, 2)
        
        # Connetti pulsante di sblocco per passare alla pagina principale
        unlock_button.clicked.connect(lambda: self.stack_widget.setCurrentIndex(1))

    def setup_main_page(self):
        # Layout principale per la pagina principale
        main_layout = QHBoxLayout(self.main_page)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Menu laterale sinistro
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #1e1e1e;")
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        sidebar_layout.setSpacing(10)
        
        # Profilo utente
        profile_widget = QWidget()
        profile_layout = QHBoxLayout(profile_widget)
        profile_layout.setContentsMargins(0, 0, 0, 0)
        
        profile_pic = QLabel()
        profile_pic.setFixedSize(32, 32)
        profile_pic.setStyleSheet("background-color: #4f9fee; border-radius: 16px;")
        
        profile_label = QLabel("PasswordManager")
        profile_label.setStyleSheet("color: white; font-size: 12px;")
        
        profile_layout.addWidget(profile_pic)
        profile_layout.addWidget(profile_label)
        profile_layout.addStretch()
        
        # Opzioni menu
        menu_items = [
            ("🔒 Overview", True),
            ("🔑 Categories", False),
            ("🔐 Shared Passwords", False),
            ("📊 Imported Passwords", False),
            ("🔄 Synchronization", False),
            ("📱 Customization", False)
        ]
        
        # Aggiungi elementi menu
        sidebar_layout.addWidget(profile_widget)
        sidebar_layout.addSpacing(20)
        
        for text, selected in menu_items:
            menu_button = QPushButton(text)
            menu_button.setStyleSheet(
                f"text-align: left; padding: 10px; border-radius: 6px; "
                f"background-color: {'#424242' if selected else 'transparent'};"
            )
            sidebar_layout.addWidget(menu_button)
        
        sidebar_layout.addStretch()
        
        # Menu di importazione/esportazione
        import_export_items = [
            "🔼 Import Passwords",
            "🔽 Export Passwords"
        ]
        
        for text in import_export_items:
            menu_button = QPushButton(text)
            menu_button.setStyleSheet("text-align: left; padding: 10px; border-radius: 6px; background-color: transparent;")
            sidebar_layout.addWidget(menu_button)
        
        # Area contenuto principale
        main_content = QWidget()
        main_content_layout = QVBoxLayout(main_content)
        main_content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 10)
        
        overview_title = QLabel("Overview")
        overview_title.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("🔍 Search Password...")
        search_bar.setFixedWidth(200)
        
        password_details = QLabel("Password Details")
        password_details.setStyleSheet("font-size: 16px; font-weight: bold;")
        
        header_layout.addWidget(overview_title)
        header_layout.addStretch()
        header_layout.addWidget(search_bar)
        header_layout.addStretch()
        header_layout.addWidget(password_details)
        
        # Griglia di contenuto
        content_grid = QGridLayout()
        content_grid.setContentsMargins(0, 0, 0, 0)
        content_grid.setSpacing(15)
        
        # Crea le card per la dashboard
        self.create_card(content_grid, 0, 0, "Password Basics", "Get started with your credentials", "🔑", progress=67)
        self.create_card(content_grid, 0, 1, "Password Security", "Check password strength", "🔒", toggle=True)
        self.create_security_trends_card(content_grid, 1, 0)
        self.create_data_import_card(content_grid, 1, 1)
        
        # Aggiungi la sezione Password sotto
        password_section = QWidget()
        password_section_layout = QVBoxLayout(password_section)
        password_section_layout.setContentsMargins(0, 20, 0, 0)
        
        password_header = QWidget()
        password_header_layout = QHBoxLayout(password_header)
        password_header_layout.setContentsMargins(0, 0, 0, 10)
        
        password_title = QLabel("Password")
        password_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        add_password_btn = QPushButton("+ Create Password")
        add_password_btn.setStyleSheet("background-color: #424242;")
        
        password_header_layout.addWidget(password_title)
        password_header_layout.addStretch()
        password_header_layout.addWidget(add_password_btn)
        
        # Griglia delle password
        password_grid = QGridLayout()
        password_grid.setContentsMargins(0, 0, 0, 0)
        password_grid.setSpacing(10)
        
        # Intestazione griglia
        headers = ["", "Name", "Username", "Category", "Strength", "Created"]
        for i, header in enumerate(headers):
            label = QLabel(header)
            label.setStyleSheet("color: #aaaaaa; font-size: 12px;")
            password_grid.addWidget(label, 0, i)
        
        # Aggiungi alcune righe di esempio
        self.add_password_row(password_grid, 1, "Gmail", "user@gmail.com", "Email", 85)
        self.add_password_row(password_grid, 2, "Twitter", "username", "Social", 65)
        
        # Sezione dettagli password (terza colonna)
        details_widget = QWidget()
        details_widget.setFixedWidth(280)
        details_layout = QVBoxLayout(details_widget)
        
        # Sezione grafico forza password
        self.create_strength_meter(details_layout)
        
        # Sezione notifiche
        self.create_notifications_section(details_layout)
        
        # Sezione impostazioni
        self.create_settings_section(details_layout)
        
        # Assemblaggio layout
        password_section_layout.addWidget(password_header)
        password_section_layout.addLayout(password_grid)
        
        main_content_layout.addWidget(header_widget)
        main_content_layout.addLayout(content_grid)
        main_content_layout.addWidget(password_section)
        
        # Aggiungi i widget al layout principale
        main_layout.addWidget(sidebar)
        main_layout.addWidget(main_content, 1)
        main_layout.addWidget(details_widget)

    def create_card(self, parent_layout, row, col, title, subtitle, icon="", progress=None, toggle=False):
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(120)
        
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(15, 15, 15, 15)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 5)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 20px;")
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(icon_label)
        
        # Sottotitolo
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        # Aggiungi elementi al layout della card
        card_layout.addWidget(header)
        card_layout.addWidget(subtitle_label)
        card_layout.addStretch()
        
        # Aggiungi barra di progresso o toggle se necessario
        if progress is not None:
            progress_widget = QWidget()
            progress_layout = QHBoxLayout(progress_widget)
            progress_layout.setContentsMargins(0, 5, 0, 0)
            
            progress_bar = QProgressBar()
            progress_bar.setValue(progress)
            progress_bar.setTextVisible(False)
            
            progress_text = QLabel(f"Progress: {progress}%")
            progress_text.setStyleSheet("color: #aaaaaa; font-size: 12px;")
            
            progress_layout.addWidget(progress_bar)
            progress_layout.addWidget(progress_text)
            
            card_layout.addWidget(progress_widget)
        
        if toggle:
            toggle_widget = QWidget()
            toggle_layout = QHBoxLayout(toggle_widget)
            toggle_layout.setContentsMargins(0, 5, 0, 0)
            
            toggle_btn = QPushButton("On")
            toggle_btn.setFixedSize(40, 20)
            toggle_btn.setStyleSheet("background-color: #4f9fee; border-radius: 10px; font-size: 10px;")
            
            toggle_layout.addStretch()
            toggle_layout.addWidget(toggle_btn)
            
            card_layout.addWidget(toggle_widget)
        
        parent_layout.addWidget(card, row, col)

    def create_security_trends_card(self, parent_layout, row, col):
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(120)
        
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(15, 15, 15, 15)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 5)
        
        title_label = QLabel("Security Trends")
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        new_label = QPushButton("New")
        new_label.setObjectName("newButton")
        new_label.setFixedSize(50, 24)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(new_label)
        
        # Info sulla sicurezza
        security_text = QLabel("Last Check: Oct. 13, 23:16\nPassword issues found: 2")
        security_text.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        # Footer
        footer = QWidget()
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(0, 10, 0, 0)
        
        usage_label = QLabel("Storage usage:")
        usage_label.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        progress_bar = QProgressBar()
        progress_bar.setValue(65)
        progress_bar.setTextVisible(False)
        progress_bar.setFixedWidth(100)
        
        footer_layout.addWidget(usage_label)
        footer_layout.addWidget(progress_bar)
        footer_layout.addStretch()
        
        # Aggiungi elementi al layout della card
        card_layout.addWidget(header)
        card_layout.addWidget(security_text)
        card_layout.addStretch()
        card_layout.addWidget(footer)
        
        parent_layout.addWidget(card, row, col)

    def create_data_import_card(self, parent_layout, row, col):
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(120)
        
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(15, 15, 15, 15)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 5)
        
        title_label = QLabel("Data Import")
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        new_label = QPushButton("Import")
        new_label.setObjectName("newButton")
        new_label.setFixedSize(60, 24)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(new_label)
        
        # Info sull'importazione dati
        import_text = QLabel("Imported in Oct. 05, 13:48\nPasswords missing: 0")
        import_text.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        # Footer
        footer = QWidget()
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(0, 10, 0, 0)
        
        footer_text = QLabel("Last import:")
        footer_text.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        footer_layout.addWidget(footer_text)
        footer_layout.addStretch()
        
        # Aggiungi elementi al layout della card
        card_layout.addWidget(header)
        card_layout.addWidget(import_text)
        card_layout.addStretch()
        card_layout.addWidget(footer)
        
        parent_layout.addWidget(card, row, col)

    def add_password_row(self, grid, row, name, username, category, strength):
        # Checkbox
        # grid.addWidget(QCheckBox(), row, 0)
        
        # Nome
        name_label = QLabel(name)
        name_label.setStyleSheet("font-weight: bold;")
        grid.addWidget(name_label, row, 1)
        
        # Username
        username_label = QLabel(username)
        grid.addWidget(username_label, row, 2)
        
        # Categoria
        category_btn = QPushButton(category)
        category_btn.setStyleSheet("background-color: #424242; padding: 4px 8px; border-radius: 10px;")
        category_btn.setFixedSize(80, 25)
        grid.addWidget(category_btn, row, 3)
        
        # Forza
        strength_widget = QWidget()
        strength_layout = QHBoxLayout(strength_widget)
        strength_layout.setContentsMargins(0, 0, 0, 0)
        
        strength_bar = QProgressBar()
        strength_bar.setValue(strength)
        strength_bar.setTextVisible(False)
        strength_bar.setFixedWidth(80)
        
        strength_layout.addWidget(strength_bar)
        grid.addWidget(strength_widget, row, 4)
        
        # Data creazione
        date_label = QLabel("Oct 10, 2024")
        grid.addWidget(date_label, row, 5)

    def create_strength_meter(self, parent_layout):
        # Titolo sezione
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 10)
        
        title = QLabel("Password Strength")
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        lock_icon = QPushButton("📊")
        lock_icon.setStyleSheet("background-color: transparent; font-size: 16px;")
        lock_icon.setFixedSize(30, 30)
        
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(lock_icon)
        
        # Gradienti di colore per il grafico di forza
        gradient_widget = QWidget()
        gradient_widget.setFixedHeight(40)
        gradient_widget.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ff0000, stop:0.5 #ffff00, stop:1 #00ff00); border-radius: 4px;")
        
        # Label per le valutazioni
        labels_widget = QWidget()
        labels_layout = QHBoxLayout(labels_widget)
        labels_layout.setContentsMargins(0, 5, 0, 0)
        
        weak_label = QLabel("Weak")
        weak_label.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        strong_label = QLabel("Strong")
        strong_label.setStyleSheet("color: #aaaaaa; font-size: 12px;")
        
        labels_layout.addWidget(weak_label)
        labels_layout.addStretch()
        labels_layout.addWidget(strong_label)
        
        # Aggiungi al layout principale
        parent_layout.addWidget(header)
        parent_layout.addWidget(gradient_widget)
        parent_layout.addWidget(labels_widget)
        parent_layout.addSpacing(20)

    def create_notifications_section(self, parent_layout):
        # Titolo sezione
        title = QLabel("Notifications")
        title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        
        # Notifiche
        notifications = [
            ("Password Expiry", "New"),
            ("Password Change", "Reset")
        ]
        
        notification_widget = QWidget()
        notification_layout = QVBoxLayout(notification_widget)
        notification_layout.setContentsMargins(0, 0, 0, 0)
        notification_layout.setSpacing(10)
        
        for text, status in notifications:
            notif = QWidget()
            notif_layout = QHBoxLayout(notif)
            notif_layout.setContentsMargins(0, 0, 0, 0)
            
            icon = QLabel("🔔")
            icon.setFixedSize(24, 24)
            icon.setStyleSheet("background-color: #323232; border-radius: 12px; font-size: 14px;")
            
            notif_text = QLabel(text)
            notif_text.setStyleSheet("font-size: 14px;")
            
            status_label = QLabel(status)
            status_label.setStyleSheet("color: #aaaaaa; font-size: 12px;")
            
            notif_layout.addWidget(icon)
            notif_layout.addWidget(notif_text)
            notif_layout.addStretch()
            notif_layout.addWidget(status_label)
            
            notification_layout.addWidget(notif)
        
        # Aggiungi al layout principale
        parent_layout.addWidget(title)
        parent_layout.addWidget(notification_widget)
        parent_layout.addSpacing(20)

    def create_settings_section(self, parent_layout):
        # Titolo sezione
        title = QLabel("Settings")
        title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        
        # Impostazioni
        settings_widget = QWidget()
        settings_layout = QVBoxLayout(settings_widget)
        settings_layout.setContentsMargins(0, 0, 0, 0)
        settings_layout.setSpacing(15)
        
        # Opzione di personalizzazione
        customize_widget = QWidget()
        customize_layout = QHBoxLayout(customize_widget)
        customize_layout.setContentsMargins(0, 0, 0, 0)
        
        customize_text = QLabel("Customize Your Password\nManager Experience")
        customize_text.setStyleSheet("font-size: 14px;")
        
        toggle_btn = QPushButton("")
        toggle_btn.setFixedSize(30, 30)
        toggle_btn.setStyleSheet("background-color: #323232; border-radius: 15px;")
        
        customize_layout.addWidget(customize_text)
        customize_layout.addStretch()
        customize_layout.addWidget(toggle_btn)
        
        # Aggiungi la sezione delle impostazioni al layout principale
        settings_layout.addWidget(customize_widget)
        
        parent_layout.addWidget(title)
        parent_layout.addWidget(settings_widget)
        parent_layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec())