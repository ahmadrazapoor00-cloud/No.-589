"""
Custom Title Bar Widget
Premium frameless window title bar with custom controls
"""

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class TitleBar(QWidget):
    """Custom title bar for frameless window"""
    
    minimize_clicked = Signal()
    maximize_clicked = Signal()
    close_clicked = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("titleBar")
        self.setFixedHeight(48)
        self._setup_ui()
        self._drag_pos = None
    
    def _setup_ui(self):
        """Setup title bar UI"""
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 0, 12, 0)
        layout.setSpacing(0)
        
        # Logo and title section
        title_layout = QHBoxLayout()
        title_layout.setSpacing(12)
        
        # Logo placeholder (can be replaced with actual logo)
        self.logo_label = QLabel("◈")
        self.logo_label.setStyleSheet("""
            font-size: 20px;
            color: #FF6B35;
            font-weight: bold;
        """)
        title_layout.addWidget(self.logo_label)
        
        # Title
        self.title_label = QLabel("NELA LAUNCHER")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 600;
            color: #FFFFFF;
            letter-spacing: 1px;
        """)
        title_layout.addWidget(self.title_label)
        
        layout.addLayout(title_layout)
        
        # Spacer
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer)
        
        # Window controls
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(8)
        controls_layout.setObjectName("windowControls")
        
        # Minimize button
        self.minimize_btn = QPushButton("─")
        self.minimize_btn.setFixedSize(40, 40)
        self.minimize_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #A0A0A0;
                font-size: 18px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1F1F1F;
                color: #FFFFFF;
            }
        """)
        self.minimize_btn.clicked.connect(self._on_minimize)
        controls_layout.addWidget(self.minimize_btn)
        
        # Maximize/Restore button
        self.maximize_btn = QPushButton("□")
        self.maximize_btn.setFixedSize(40, 40)
        self.maximize_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #A0A0A0;
                font-size: 14px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1F1F1F;
                color: #FFFFFF;
            }
        """)
        self.maximize_btn.clicked.connect(self._on_maximize)
        controls_layout.addWidget(self.maximize_btn)
        
        # Close button
        self.close_btn = QPushButton("✕")
        self.close_btn.setFixedSize(40, 40)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #A0A0A0;
                font-size: 16px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #E81123;
                color: #FFFFFF;
            }
        """)
        self.close_btn.clicked.connect(self._on_close)
        controls_layout.addWidget(self.close_btn)
        
        layout.addLayout(controls_layout)
    
    def _on_minimize(self):
        """Handle minimize button click"""
        if self.parentWindow():
            self.parentWindow().showMinimized()
        self.minimize_clicked.emit()
    
    def _on_maximize(self):
        """Handle maximize button click"""
        if self.parentWindow():
            if self.parentWindow().isMaximized():
                self.parentWindow().showNormal()
                self.maximize_btn.setText("□")
            else:
                self.parentWindow().showMaximized()
                self.maximize_btn.setText("❐")
        self.maximize_clicked.emit()
    
    def _on_close(self):
        """Handle close button click"""
        if self.parentWindow():
            self.parentWindow().close()
        self.close_clicked.emit()
    
    def mousePressEvent(self, event):
        """Handle mouse press for dragging"""
        if event.button() == Qt.LeftButton:
            if self.parentWindow() and not self.parentWindow().isMaximized():
                self._drag_pos = event.globalPosition().toPoint() - self.parentWindow().frameGeometry().topLeft()
                event.accept()
    
    def mouseMoveEvent(self, event):
        """Handle mouse move for dragging"""
        if event.buttons() == Qt.LeftButton and self._drag_pos and self.parentWindow():
            if not self.parentWindow().isMaximized():
                self.parentWindow().move(event.globalPosition().toPoint() - self._drag_pos)
                event.accept()
