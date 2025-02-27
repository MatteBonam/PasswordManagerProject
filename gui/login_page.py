import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QLineEdit, QPushButton, QFrame, QScrollArea, QSizePolicy,
                           QGridLayout, QTabWidget, QProgressBar, QSpacerItem)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPalette, QFont, QLinearGradient, QGradient

class Login_Page(QWidget):

    login_successful = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__()
        self.setup_login_page()

    def setup_login_page(self):
        # Layout principale per la pagina di login
        login_layout = QHBoxLayout(self)
        
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
        password_input.setPlaceholderText("Enter your password")
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
        unlock_button.clicked.connect(self.authenticate)

    def authenticate(self):
        # Per ora, emettiamo semplicemente il segnale di autenticazione riuscita
        self.login_successful.emit(True)