"""
Sidebar Navigation Widget
Premium sidebar with navigation buttons and user profile
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, Signal


class Sidebar(QWidget):
    """Premium sidebar navigation component"""
    
    navigation_requested = Signal(str)  # page_name
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("sidebar")
        self.setFixedWidth(260)
        self._setup_ui()
        self._current_page = "home"
    
    def _setup_ui(self):
        """Setup sidebar UI"""
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(8)
        
        # Top section - Logo and brand
        top_section = QFrame()
        top_section.setObjectName("sidebarTop")
        top_layout = QVBoxLayout(top_section)
        top_layout.setContentsMargins(12, 20, 12, 20)
        top_layout.setSpacing(8)
        
        # Logo mark
        logo_label = QLabel("◈")
        logo_label.setStyleSheet("""
            font-size: 32px;
            color: #FF6B35;
            font-weight: bold;
        """)
        logo_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(logo_label)
        
        # Brand name
        brand_label = QLabel("NELA")
        brand_label.setStyleSheet("""
            font-size: 20px;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 2px;
        """)
        brand_label.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(brand_label)
        
        main_layout.addWidget(top_section)
        
        # Navigation section
        nav_section = QFrame()
        nav_section.setObjectName("sidebarNav")
        nav_layout = QVBoxLayout(nav_section)
        nav_layout.setContentsMargins(8, 8, 8, 8)
        nav_layout.setSpacing(4)
        
        # Navigation buttons
        self.nav_buttons = {}
        
        nav_items = [
            ("home", "Home", "⌂"),
            ("play", "Play", "▶"),
            ("profiles", "Profiles", "▤"),
            ("mods", "Mods", "◫"),
            ("skins", "Skin Studio", "☺"),
            ("performance", "Performance", "⚡"),
            ("updates", "Updates", "↻"),
            ("settings", "Settings", "⚙"),
            ("logs", "Logs", "📋"),
            ("about", "About", "ℹ"),
        ]
        
        for page_id, label_text, icon in nav_items:
            btn = QPushButton(f"{icon}  {label_text}")
            btn.setObjectName("navButton")
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, pid=page_id: self._on_nav_clicked(pid))
            btn.setStyleSheet("""
                QPushButton#navButton {
                    background-color: transparent;
                    border: none;
                    border-radius: 8px;
                    padding: 14px 16px;
                    text-align: left;
                    font-weight: 500;
                    color: #A0A0A0;
                    min-height: 48px;
                    font-size: 14px;
                }
                QPushButton#navButton:hover {
                    background-color: #1A1A1A;
                    color: #FFFFFF;
                }
                QPushButton#navButton:checked {
                    background-color: #1F1F1F;
                    color: #FF6B35;
                    font-weight: 600;
                }
            """)
            
            nav_layout.addWidget(btn)
            self.nav_buttons[page_id] = btn
        
        # Add spacer to push bottom section down
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        nav_layout.addItem(spacer)
        
        main_layout.addWidget(nav_section)
        
        # Bottom section - User profile
        bottom_section = QFrame()
        bottom_section.setObjectName("sidebarBottom")
        bottom_layout = QVBoxLayout(bottom_section)
        bottom_layout.setContentsMargins(12, 12, 12, 12)
        bottom_layout.setSpacing(12)
        
        # Separator
        separator = QFrame()
        separator.setObjectName("separator")
        separator.setFixedHeight(1)
        bottom_layout.addWidget(separator)
        
        # User info
        user_label = QLabel("Not signed in")
        user_label.setStyleSheet("""
            font-size: 14px;
            font-weight: 600;
            color: #FFFFFF;
        """)
        bottom_layout.addWidget(user_label)
        
        status_label = QLabel("Sign in to access features")
        status_label.setStyleSheet("""
            font-size: 12px;
            color: #666666;
        """)
        bottom_layout.addWidget(status_label)
        
        main_layout.addWidget(bottom_section)
    
    def _on_nav_clicked(self, page_id: str):
        """Handle navigation button click"""
        self._set_active_page(page_id)
        self.navigation_requested.emit(page_id)
    
    def _set_active_page(self, page_id: str):
        """Set the active navigation page"""
        self._current_page = page_id
        
        # Update button states
        for pid, btn in self.nav_buttons.items():
            btn.setChecked(pid == page_id)
    
    def get_current_page(self) -> str:
        """Get current active page"""
        return self._current_page
    
    def set_user_info(self, username: str, is_logged_in: bool = True):
        """Update user info in sidebar"""
        # Find the bottom section and update labels
        # This is a simplified version - would need proper references in full implementation
        pass
