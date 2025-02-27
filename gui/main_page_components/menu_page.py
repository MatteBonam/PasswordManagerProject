from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QFrame, QScrollArea, QSizePolicy,
                           QGridLayout, QTabWidget, QProgressBar, QSpacerItem)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QFont, QLinearGradient, QGradient

class Menu_Widget(QWidget):
    def __init__(self, parent = ..., flags = ...):
        super().__init__()
        menu_layout = QVBoxLayout(self)
        # Opzioni menu
        menu_items = [
            ("🔒 Overview", True),
            ("🔑 Categories", False),
            ("🔐 Shared Passwords", False),
            ("📊 Imported Passwords", False),
            ("🔄 Synchronization", False),
            ("📱 Customization", False)
        ]

        for text, selected in menu_items:
            menu_button = QPushButton(text)
            menu_button.setStyleSheet(
                f"text-align: left; padding: 10px; border-radius: 6px; "
                f"background-color: {'#424242' if selected else 'transparent'};"
            )
            menu_layout.addWidget(menu_button)