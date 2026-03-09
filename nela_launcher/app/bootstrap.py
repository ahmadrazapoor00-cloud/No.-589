"""
Nela Launcher Bootstrap
Main application window and initialization
"""

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QTimer, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QColor

from pages.splash_page import SplashPage
from pages.welcome_page import WelcomePage
from pages.login_page import LoginPage
from pages.home_dashboard import HomeDashboard
from widgets.title_bar import TitleBar
from widgets.sidebar import Sidebar
from styles.stylesheet import get_main_stylesheet


class NelaApplication(QMainWindow):
    """Main Nela Launcher Application Window"""
    
    page_changed = Signal(str)
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Nela Launcher")
        self.setMinimumSize(1200, 800)
        self.resize(1400, 900)
        
        # Remove default window frame for custom title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Setup UI
        self._setup_ui()
        self._apply_styles()
        self._setup_effects()
        
        # Start with splash screen
        self._show_splash()
    
    def _setup_ui(self):
        """Setup the main UI structure"""
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Title bar
        self.title_bar = TitleBar(self)
        main_layout.addWidget(self.title_bar)
        
        # Content container
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Page stack
        self.page_stack = QStackedWidget()
        self.page_stack.setContentsMargins(0, 0, 0, 0)
        
        # Initialize pages
        self.pages = {
            'splash': SplashPage(self),
            'welcome': WelcomePage(self),
            'login': LoginPage(self),
            'home': HomeDashboard(self),
        }
        
        # Add pages to stack
        for page_name, page_widget in self.pages.items():
            self.page_stack.addWidget(page_widget)
        
        content_layout.addWidget(self.page_stack)
        main_layout.addWidget(content_widget)
    
    def _apply_styles(self):
        """Apply main stylesheet"""
        self.setStyleSheet(get_main_stylesheet())
    
    def _setup_effects(self):
        """Setup visual effects"""
        
        # Drop shadow for window
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.graphicsEffect = shadow
    
    def _show_splash(self):
        """Show splash screen then transition to welcome"""
        self.page_stack.setCurrentWidget(self.pages['splash'])
        
        # Auto-transition after splash animation
        QTimer.singleShot(3000, self._show_welcome)
    
    def _show_welcome(self):
        """Transition to welcome page"""
        self.page_stack.setCurrentWidget(self.pages['welcome'])
    
    def navigate_to(self, page_name: str):
        """Navigate to a specific page"""
        if page_name in self.pages:
            self.page_stack.setCurrentWidget(self.pages[page_name])
            self.page_changed.emit(page_name)
    
    def go_home(self):
        """Navigate to home dashboard"""
        self.navigate_to('home')
    
    def closeEvent(self, event):
        """Handle window close"""
        # Save state before closing
        self._save_state()
        event.accept()
    
    def _save_state(self):
        """Save application state"""
        # TODO: Implement state saving
        pass
