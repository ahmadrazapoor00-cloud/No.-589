"""
Splash Page
Premium animated splash screen with Nela logo
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont


class SplashPage(QWidget):
    """Premium splash screen with animated logo"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget {
                background-color: #0A0A0A;
            }
        """)
        self._setup_ui()
        self._start_animations()
    
    def _setup_ui(self):
        """Setup splash screen UI"""
        
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(40)
        
        # Logo container
        logo_container = QFrame()
        logo_container.setStyleSheet("background-color: transparent;")
        logo_layout = QVBoxLayout(logo_container)
        logo_layout.setAlignment(Qt.AlignCenter)
        logo_layout.setSpacing(20)
        
        # Main logo mark - stylized N
        self.logo_label = QLabel("◈")
        self.logo_label.setStyleSheet("""
            font-size: 120px;
            color: #FF6B35;
            font-weight: bold;
            background-color: transparent;
        """)
        self.logo_label.setAlignment(Qt.AlignCenter)
        logo_layout.addWidget(self.logo_label)
        
        # Brand name
        brand_label = QLabel("NELA")
        brand_label.setStyleSheet("""
            font-size: 48px;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 8px;
            background-color: transparent;
        """)
        brand_label.setAlignment(Qt.AlignCenter)
        logo_layout.addWidget(brand_label)
        
        # Tagline
        tagline_label = QLabel("LAUNCHER")
        tagline_label.setStyleSheet("""
            font-size: 16px;
            color: #666666;
            letter-spacing: 4px;
            text-transform: uppercase;
            background-color: transparent;
        """)
        tagline_label.setAlignment(Qt.AlignCenter)
        logo_layout.addWidget(tagline_label)
        
        layout.addWidget(logo_container)
        
        # Loading indicator
        loading_container = QFrame()
        loading_layout = QVBoxLayout(loading_container)
        loading_layout.setAlignment(Qt.AlignCenter)
        loading_layout.setSpacing(16)
        
        # Animated dots
        self.dots_label = QLabel("●   ●   ●")
        self.dots_label.setStyleSheet("""
            font-size: 24px;
            color: #FF6B35;
            background-color: transparent;
            letter-spacing: 8px;
        """)
        self.dots_label.setAlignment(Qt.AlignCenter)
        loading_layout.addWidget(self.dots_label)
        
        # Version info
        version_label = QLabel("v1.0.0")
        version_label.setStyleSheet("""
            font-size: 12px;
            color: #444444;
            background-color: transparent;
        """)
        version_label.setAlignment(Qt.AlignCenter)
        loading_layout.addWidget(version_label)
        
        layout.addWidget(loading_container)
    
    def _start_animations(self):
        """Start splash screen animations"""
        
        # Fade in animation for logo
        self.fade_animation = QPropertyAnimation(self.logo_label, b"opacity")
        self.fade_animation.setDuration(1500)
        self.fade_animation.setStartValue(0.0)
        self.fade_animation.setEndValue(1.0)
        self.fade_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.fade_animation.start()
        
        # Pulse animation for dots
        self.dot_timer = QTimer()
        self.dot_timer.timeout.connect(self._animate_dots)
        self.dot_timer.start(300)
        
        self._dot_phase = 0
    
    def _animate_dots(self):
        """Animate loading dots"""
        self._dot_phase = (self._dot_phase + 1) % 3
        
        dot_states = [
            "●   ○   ○",
            "○   ●   ○",
            "○   ○   ●"
        ]
        
        self.dots_label.setText(dot_states[self._dot_phase])
