from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QFrame, QScrollArea, QSizePolicy,
                           QGridLayout, QTabWidget, QProgressBar, QSpacerItem)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QFont, QLinearGradient, QGradient
from gui.main_page_components.user_page import Profile_Widget

class Sidebar_Widget(QWidget):
    def __init__(self, parent = ..., flags = ...):
        super().__init__()
        self.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(self)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        sidebar_layout.setSpacing(10)

        profile_widget = Profile_Widget()

        sidebar_layout.addWidget(profile_widget)
        sidebar_layout.addSpacing(20)
        # Opzioni menu
        menu_items = [
            ("🔒 Overview"),
            ("🔑 Categories"),
            ("🔐 Shared Passwords"),
            ("📊 Imported Passwords"),
            ("🔄 Synchronization"),
            ("📱 Customization")
        ]

        for text in menu_items:
            menu_button = QPushButton(text)
            menu_button.setStyleSheet(
                f"text-align: left; padding: 10px; border-radius: 6px; "
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