import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QFrame, QScrollArea, QSizePolicy,
                           QGridLayout, QTabWidget, QProgressBar, QSpacerItem)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QFont, QLinearGradient, QGradient
from gui.main_page_components.sidebar_page import Sidebar_Widget


class Main_Page(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.setup_main_page()

    def setup_main_page(self):
        # Layout principale per la pagina principale
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Menu laterale sinistro
        sidebar = Sidebar_Widget()
        
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
        
        
        header_layout.addWidget(overview_title)
        header_layout.addStretch()
        header_layout.addWidget(search_bar)
        header_layout.addStretch()
        
        # Griglia di contenuto
        content_grid = QGridLayout()
        content_grid.setContentsMargins(0, 0, 0, 0)
        content_grid.setSpacing(15)
        
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
        
        
        # Assemblaggio layout
        password_section_layout.addWidget(password_header)
        password_section_layout.addLayout(password_grid)
        
        main_content_layout.addWidget(header_widget)
        main_content_layout.addLayout(content_grid)
        main_content_layout.addWidget(password_section)
        
        # Aggiungi i widget al layout principale
        main_layout.addWidget(sidebar)
        main_layout.addWidget(main_content, 1)


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

    def create_strength_meter(parent_layout):
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

    def create_notifications_section(parent_layout):
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

    def create_settings_section(parent_layout):
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