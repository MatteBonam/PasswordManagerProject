from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QFrame, QScrollArea, QSizePolicy,
                           QGridLayout, QTabWidget, QProgressBar, QSpacerItem)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QFont, QLinearGradient, QGradient

class Profile_Widget(QWidget):
    def __init__(self, parent = None, flags = None):
        super().__init__()
        profile_layout = QHBoxLayout(self)
        profile_layout.setContentsMargins(0, 0, 0, 0)
    
        profile_pic = QLabel()
        profile_pic.setFixedSize(32, 32)
        profile_pic.setStyleSheet("background-color: #4f9fee; border-radius: 16px;")
    
        profile_label = QLabel("PasswordManager")
        profile_label.setStyleSheet("color: white; font-size: 12px;")
    
        profile_layout.addWidget(profile_pic)
        profile_layout.addWidget(profile_label)
        profile_layout.addStretch()