"""
Welcome Page
Onboarding and welcome screen
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QFrame, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, Signal


class WelcomePage(QWidget):
    """Premium welcome/onboarding page"""
    
    get_started_clicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget {
                background-color: #0A0A0A;
            }
        """)
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup welcome page UI"""
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(80, 60, 80, 60)
        main_layout.setSpacing(40)
        
        # Top section - Welcome message
        top_section = QFrame()
        top_layout = QVBoxLayout(top_section)
        top_layout.setAlignment(Qt.AlignCenter)
        top_layout.setSpacing(20)
        
        # Heading
        heading_label = QLabel("Welcome to Nela")
        heading_label.setObjectName("heading")
        heading_label.setStyleSheet("""
            font-size: 56px;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 1px;
        """)
        heading_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(heading_label)
        
        # Subtitle
        subtitle_label = QLabel("Minimal outside. Powerful inside.")
        subtitle_label.setStyleSheet("""
            font-size: 20px;
            color: #A0A0A0;
            font-weight: 400;
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(subtitle_label)
        
        main_layout.addWidget(top_section)
        
        # Middle section - Feature highlights
        features_section = QFrame()
        features_layout = QHBoxLayout(features_section)
        features_layout.setSpacing(24)
        
        feature_cards = [
            {
                "icon": "⚡",
                "title": "Built for Fabric",
                "desc": "Optimized exclusively for Minecraft 1.16.5 Fabric"
            },
            {
                "icon": "◫",
                "title": "Curated Mods",
                "desc": "30+ premium mods for performance and quality of life"
            },
            {
                "icon": "☺",
                "title": "Skin Studio",
                "desc": "Preview and customize your Minecraft skin in 3D"
            },
            {
                "icon": "🎯",
                "title": "Performance",
                "desc": "Advanced optimization tools and presets"
            }
        ]
        
        for feature in feature_cards:
            card = self._create_feature_card(feature)
            features_layout.addWidget(card)
        
        main_layout.addWidget(features_section)
        
        # Spacer
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)
        
        # Bottom section - CTA buttons
        bottom_section = QFrame()
        bottom_layout = QHBoxLayout(bottom_section)
        bottom_layout.setAlignment(Qt.AlignCenter)
        bottom_layout.setSpacing(20)
        
        # Get Started button (primary)
        self.get_started_btn = QPushButton("Get Started")
        self.get_started_btn.setObjectName("primaryButton")
        self.get_started_btn.setMinimumSize(200, 56)
        self.get_started_btn.setStyleSheet("""
            QPushButton#primaryButton {
                background-color: #FF6B35;
                color: #FFFFFF;
                border: none;
                border-radius: 12px;
                font-size: 16px;
                font-weight: 600;
                letter-spacing: 0.5px;
            }
            QPushButton#primaryButton:hover {
                background-color: #FF7B4D;
            }
            QPushButton#primaryButton:pressed {
                background-color: #E55A2B;
            }
        """)
        self.get_started_btn.clicked.connect(self._on_get_started)
        bottom_layout.addWidget(self.get_started_btn)
        
        # Learn More button (secondary)
        learn_more_btn = QPushButton("Learn More")
        learn_more_btn.setObjectName("secondaryButton")
        learn_more_btn.setMinimumSize(200, 56)
        learn_more_btn.setStyleSheet("""
            QPushButton#secondaryButton {
                background-color: transparent;
                border: 1px solid #FF6B35;
                color: #FF6B35;
                border-radius: 12px;
                font-size: 16px;
                font-weight: 600;
                letter-spacing: 0.5px;
            }
            QPushButton#secondaryButton:hover {
                background-color: rgba(255, 107, 53, 0.1);
            }
        """)
        bottom_layout.addWidget(learn_more_btn)
        
        main_layout.addWidget(bottom_section)
    
    def _create_feature_card(self, feature: dict) -> QFrame:
        """Create a feature highlight card"""
        
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumWidth(240)
        card.setMaximumWidth(280)
        card.setStyleSheet("""
            QFrame#card {
                background-color: #111111;
                border: 1px solid #1F1F1F;
                border-radius: 16px;
                padding: 32px 24px;
            }
            QFrame#card:hover {
                border-color: #2A2A2A;
                background-color: #141414;
            }
        """)
        
        layout = QVBoxLayout(card)
        layout.setSpacing(16)
        layout.setAlignment(Qt.AlignCenter)
        
        # Icon
        icon_label = QLabel(feature["icon"])
        icon_label.setStyleSheet("""
            font-size: 48px;
            background-color: transparent;
        """)
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)
        
        # Title
        title_label = QLabel(feature["title"])
        title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #FFFFFF;
            background-color: transparent;
        """)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Description
        desc_label = QLabel(feature["desc"])
        desc_label.setStyleSheet("""
            font-size: 14px;
            color: #888888;
            background-color: transparent;
        """)
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)
        
        return card
    
    def _on_get_started(self):
        """Handle get started button click"""
        self.get_started_clicked.emit()
