import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QFrame, QScrollArea, QSizePolicy,
                           QGridLayout, QTabWidget, QProgressBar, QSpacerItem)
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QFont, QLinearGradient, QGradient
from gui.login_page import Login_Page
from gui.main_page import Main_Page

class PasswordManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Master")
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
        self.login_page = Login_Page()
        
        self.login_page.login_successful.connect(self.authorized)
        # Pagina principale
        self.main_page = Main_Page()
        
        # Aggiungi lo stack al layout principale
        self.main_layout.addWidget(self.login_page)
        
    def authorized(self, message):
        if message :
            self.main_layout.removeWidget(self.login_page)
            self.login_page.setParent(None)
            self.login_page.deleteLater()
            self.main_layout.addWidget(self.main_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec())