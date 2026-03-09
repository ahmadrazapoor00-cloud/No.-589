"""
Login Page
Microsoft authentication and sign-in flow
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QFrame, QLineEdit, QSpacerItem, QSizePolicy, QApplication
)
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QFont


class LoginPage(QWidget):
    """Premium login page with Microsoft authentication"""
    
    login_requested = Signal(str)  # auth_type
    skip_clicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget {
                background-color: #0A0A0A;
            }
        """)
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup login page UI"""
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(80, 60, 80, 60)
        main_layout.setSpacing(40)
        
        # Top section - Title
        top_section = QFrame()
        top_layout = QVBoxLayout(top_section)
        top_layout.setAlignment(Qt.AlignCenter)
        top_layout.setSpacing(16)
        
        # Heading
        heading_label = QLabel("Sign In")
        heading_label.setObjectName("heading")
        heading_label.setStyleSheet("""
            font-size: 48px;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 0.5px;
        """)
        heading_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(heading_label)
        
        # Subtitle
        subtitle_label = QLabel("Sign in with your Microsoft account to access all features")
        subtitle_label.setStyleSheet("""
            font-size: 16px;
            color: #888888;
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(subtitle_label)
        
        main_layout.addWidget(top_section)
        
        # Middle section - Login options
        middle_section = QFrame()
        middle_layout = QVBoxLayout(middle_section)
        middle_layout.setSpacing(20)
        middle_layout.setAlignment(Qt.AlignCenter)
        
        # Microsoft login button
        self.microsoft_btn = QPushButton()
        self.microsoft_btn.setMinimumSize(400, 64)
        self.microsoft_btn.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF;
                color: #1A1A1A;
                border: none;
                border-radius: 12px;
                font-size: 16px;
                font-weight: 600;
                padding: 20px 32px;
            }
            QPushButton:hover {
                background-color: #F0F0F0;
            }
            QPushButton:pressed {
                background-color: #E0E0E0;
            }
        """)
        
        # Microsoft button content layout
        ms_layout = QHBoxLayout(self.microsoft_btn)
        ms_layout.setContentsMargins(20, 0, 20, 0)
        ms_layout.setSpacing(16)
        
        # Microsoft icon (simplified)
        ms_icon = QLabel("▣")
        ms_icon.setStyleSheet("""
            font-size: 28px;
            color: #00A4EF;
            background-color: transparent;
        """)
        ms_layout.addWidget(ms_icon)
        
        # Button text
        ms_text = QLabel("Sign in with Microsoft")
        ms_text.setStyleSheet("""
            font-size: 16px;
            font-weight: 600;
            color: #1A1A1A;
            background-color: transparent;
        """)
        ms_layout.addWidget(ms_text)
        
        ms_layout.addStretch()
        
        self.microsoft_btn.clicked.connect(lambda: self.login_requested.emit("microsoft"))
        middle_layout.addWidget(self.microsoft_btn)
        
        # Divider
        divider_frame = QFrame()
        divider_frame.setFixedHeight(40)
        divider_layout = QHBoxLayout(divider_frame)
        divider_layout.setAlignment(Qt.AlignCenter)
        
        line1 = QFrame()
        line1.setFixedHeight(1)
        line1.setStyleSheet("background-color: #1F1F1F;")
        divider_layout.addWidget(line1)
        
        or_label = QLabel("OR")
        or_label.setStyleSheet("""
            color: #666666;
            font-size: 12px;
            background-color: transparent;
            padding: 0 16px;
        """)
        divider_layout.addWidget(or_label)
        
        line2 = QFrame()
        line2.setFixedHeight(1)
        line2.setStyleSheet("background-color: #1F1F1F;")
        divider_layout.addWidget(line2)
        
        middle_layout.addWidget(divider_frame)
        
        # Offline mode button
        offline_btn = QPushButton("Continue Offline")
        offline_btn.setObjectName("secondaryButton")
        offline_btn.setMinimumSize(400, 56)
        offline_btn.setStyleSheet("""
            QPushButton#secondaryButton {
                background-color: transparent;
                border: 1px solid #2A2A2A;
                color: #A0A0A0;
                border-radius: 12px;
                font-size: 15px;
                font-weight: 500;
            }
            QPushButton#secondaryButton:hover {
                border-color: #3A3A3A;
                color: #FFFFFF;
            }
        """)
        offline_btn.clicked.connect(self.skip_clicked)
        middle_layout.addWidget(offline_btn)
        
        main_layout.addWidget(middle_section)
        
        # Spacer
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)
        
        # Bottom section - Info
        bottom_section = QFrame()
        bottom_layout = QVBoxLayout(bottom_section)
        bottom_layout.setAlignment(Qt.AlignCenter)
        bottom_layout.setSpacing(12)
        
        # Features list
        features_label = QLabel("Signing in unlocks:")
        features_label.setStyleSheet("""
            color: #666666;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        """)
        features_label.setAlignment(Qt.AlignCenter)
        bottom_layout.addWidget(features_label)
        
        feature_list = QLabel("• Skin synchronization\n• Cloud saves\n• Multiplayer access\n• Friend system")
        feature_list.setStyleSheet("""
            color: #888888;
            font-size: 14px;
            line-height: 28px;
        """)
        feature_list.setAlignment(Qt.AlignCenter)
        bottom_layout.addWidget(feature_list)
        
        main_layout.addWidget(bottom_section)
        
        # Status label (hidden by default)
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("""
            color: #FF6B35;
            font-size: 14px;
        """)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)
        main_layout.addWidget(self.status_label)
    
    def set_status(self, message: str, is_error: bool = False):
        """Set status message"""
        self.status_label.setText(message)
        if is_error:
            self.status_label.setStyleSheet("""
                color: #EF4444;
                font-size: 14px;
            """)
        else:
            self.status_label.setStyleSheet("""
                color: #10B981;
                font-size: 14px;
            """)
    
    def clear_status(self):
        """Clear status message"""
        self.status_label.setText("")
