"""
Nela Launcher Stylesheet
Premium Nothing OS-inspired styling system
"""


def get_main_stylesheet():
    """Return the main application stylesheet"""
    
    return """
    /* ============================================
       NELLA LAUNCHER - PREMIUM STYLESHEET
       Nothing OS Inspired Industrial Minimalism
       ============================================ */
    
    /* --- Global Variables --- */
    QWidget {
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
        font-size: 14px;
        color: #E8E8E8;
        background-color: #0A0A0A;
    }
    
    /* --- Main Window --- */
    QMainWindow {
        background-color: #0A0A0A;
    }
    
    /* --- Title Bar --- */
    #titleBar {
        background-color: #111111;
        border-bottom: 1px solid #1F1F1F;
        min-height: 48px;
        max-height: 48px;
    }
    
    #titleLabel {
        font-size: 16px;
        font-weight: 600;
        color: #FFFFFF;
        letter-spacing: 0.5px;
    }
    
    #windowControls {
        spacing: 8px;
    }
    
    /* --- Buttons --- */
    QPushButton {
        background-color: #1F1F1F;
        color: #FFFFFF;
        border: 1px solid #2A2A2A;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 500;
        font-size: 14px;
        min-height: 44px;
    }
    
    QPushButton:hover {
        background-color: #2A2A2A;
        border-color: #3A3A3A;
    }
    
    QPushButton:pressed {
        background-color: #1A1A1A;
    }
    
    QPushButton:disabled {
        background-color: #151515;
        color: #666666;
        border-color: #1F1F1F;
    }
    
    /* Primary Button */
    QPushButton#primaryButton {
        background-color: #FF6B35;
        color: #FFFFFF;
        border: none;
        font-weight: 600;
    }
    
    QPushButton#primaryButton:hover {
        background-color: #FF7B4D;
    }
    
    QPushButton#primaryButton:pressed {
        background-color: #E55A2B;
    }
    
    /* Secondary Button */
    QPushButton#secondaryButton {
        background-color: transparent;
        border: 1px solid #FF6B35;
        color: #FF6B35;
    }
    
    QPushButton#secondaryButton:hover {
        background-color: rgba(255, 107, 53, 0.1);
    }
    
    /* Play Button */
    QPushButton#playButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #FF6B35, stop:1 #FF8C5A);
        border: none;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
        min-height: 64px;
        letter-spacing: 1px;
    }
    
    QPushButton#playButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #FF7B4D, stop:1 #FF9C6A);
    }
    
    QPushButton#playButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #E55A2B, stop:1 #E57A4A);
    }
    
    /* --- Sidebar --- */
    #sidebar {
        background-color: #0F0F0F;
        border-right: 1px solid #1F1F1F;
        min-width: 260px;
        max-width: 260px;
    }
    
    #sidebarTop {
        background-color: #0F0F0F;
        border-bottom: 1px solid #1F1F1F;
        min-height: 80px;
        max-height: 80px;
    }
    
    #sidebarNav {
        background-color: #0F0F0F;
        spacing: 4px;
    }
    
    #sidebarBottom {
        background-color: #0F0F0F;
        border-top: 1px solid #1F1F1F;
        min-height: 100px;
        max-height: 100px;
    }
    
    /* Navigation Buttons */
    QPushButton#navButton {
        background-color: transparent;
        border: none;
        border-radius: 8px;
        padding: 14px 20px;
        text-align: left;
        font-weight: 500;
        color: #A0A0A0;
        min-height: 52px;
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
    
    QPushButton#navButton::indicator {
        width: 0px;
    }
    
    /* --- Cards --- */
    QFrame#card {
        background-color: #111111;
        border: 1px solid #1F1F1F;
        border-radius: 12px;
        padding: 20px;
    }
    
    QFrame#card:hover {
        border-color: #2A2A2A;
        background-color: #141414;
    }
    
    QFrame#highlightCard {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #111111, stop:1 #161616);
        border: 1px solid #2A2A2A;
        border-radius: 12px;
        padding: 24px;
    }
    
    /* --- Labels --- */
    QLabel {
        color: #E8E8E8;
        background-color: transparent;
    }
    
    QLabel#heading {
        font-size: 28px;
        font-weight: 700;
        color: #FFFFFF;
        letter-spacing: 0.5px;
    }
    
    QLabel#subheading {
        font-size: 18px;
        font-weight: 600;
        color: #FFFFFF;
    }
    
    QLabel#body {
        font-size: 14px;
        color: #A0A0A0;
    }
    
    QLabel#caption {
        font-size: 12px;
        color: #666666;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    QLabel#accent {
        color: #FF6B35;
        font-weight: 600;
    }
    
    /* --- Input Fields --- */
    QLineEdit {
        background-color: #111111;
        border: 1px solid #2A2A2A;
        border-radius: 8px;
        padding: 12px 16px;
        color: #FFFFFF;
        selection-background-color: #FF6B35;
        selection-color: #FFFFFF;
    }
    
    QLineEdit:hover {
        border-color: #3A3A3A;
    }
    
    QLineEdit:focus {
        border-color: #FF6B35;
    }
    
    QLineEdit:disabled {
        background-color: #0D0D0D;
        color: #666666;
    }
    
    /* --- Text Edit --- */
    QTextEdit {
        background-color: #111111;
        border: 1px solid #2A2A2A;
        border-radius: 8px;
        padding: 12px;
        color: #E8E8E8;
        selection-background-color: #FF6B35;
        selection-color: #FFFFFF;
    }
    
    QTextEdit:hover {
        border-color: #3A3A3A;
    }
    
    QTextEdit:focus {
        border-color: #FF6B35;
    }
    
    /* --- Scroll Area --- */
    QScrollArea {
        border: none;
        background-color: transparent;
    }
    
    QScrollBar:vertical {
        background-color: #0A0A0A;
        width: 8px;
        border-radius: 4px;
        margin: 0;
    }
    
    QScrollBar::handle:vertical {
        background-color: #2A2A2A;
        border-radius: 4px;
        min-height: 30px;
    }
    
    QScrollBar::handle:vertical:hover {
        background-color: #3A3A3A;
    }
    
    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        height: 0px;
    }
    
    QScrollBar::add-page:vertical,
    QScrollBar::sub-page:vertical {
        background: none;
    }
    
    QScrollBar:horizontal {
        background-color: #0A0A0A;
        height: 8px;
        border-radius: 4px;
        margin: 0;
    }
    
    QScrollBar::handle:horizontal {
        background-color: #2A2A2A;
        border-radius: 4px;
        min-width: 30px;
    }
    
    QScrollBar::handle:horizontal:hover {
        background-color: #3A3A3A;
    }
    
    QScrollBar::add-line:horizontal,
    QScrollBar::sub-line:horizontal {
        width: 0px;
    }
    
    /* --- Combo Box --- */
    QComboBox {
        background-color: #111111;
        border: 1px solid #2A2A2A;
        border-radius: 8px;
        padding: 12px 16px;
        color: #FFFFFF;
        min-height: 44px;
    }
    
    QComboBox:hover {
        border-color: #3A3A3A;
    }
    
    QComboBox:focus {
        border-color: #FF6B35;
    }
    
    QComboBox::drop-down {
        border: none;
        width: 24px;
        padding-right: 8px;
    }
    
    QComboBox::down-arrow {
        image: none;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 6px solid #A0A0A0;
        margin-right: 8px;
    }
    
    QComboBox QAbstractItemView {
        background-color: #111111;
        border: 1px solid #2A2A2A;
        border-radius: 8px;
        selection-background-color: #1F1F1F;
        selection-color: #FFFFFF;
        outline: none;
        padding: 8px;
    }
    
    QComboBox QAbstractItemView::item {
        min-height: 40px;
        padding: 8px;
        border-radius: 6px;
    }
    
    QComboBox QAbstractItemView::item:hover {
        background-color: #1F1F1F;
    }
    
    QComboBox QAbstractItemView::item:selected {
        background-color: #2A2A2A;
    }
    
    /* --- Slider --- */
    QSlider::groove:horizontal {
        background-color: #1F1F1F;
        height: 6px;
        border-radius: 3px;
    }
    
    QSlider::handle:horizontal {
        background-color: #FF6B35;
        width: 18px;
        height: 18px;
        margin: -6px 0;
        border-radius: 9px;
    }
    
    QSlider::handle:horizontal:hover {
        background-color: #FF7B4D;
    }
    
    QSlider::sub-page:horizontal {
        background-color: #FF6B35;
        border-radius: 3px;
    }
    
    QSlider::add-page:horizontal {
        background-color: #1F1F1F;
        border-radius: 3px;
    }
    
    /* --- Checkbox --- */
    QCheckBox {
        color: #E8E8E8;
        spacing: 12px;
    }
    
    QCheckBox::indicator {
        width: 22px;
        height: 22px;
        border-radius: 6px;
        border: 1px solid #2A2A2A;
        background-color: #111111;
    }
    
    QCheckBox::indicator:hover {
        border-color: #3A3A3A;
    }
    
    QCheckBox::indicator:checked {
        background-color: #FF6B35;
        border-color: #FF6B35;
    }
    
    /* --- Tab Widget --- */
    QTabWidget::pane {
        background-color: #0A0A0A;
        border: none;
        border-radius: 12px;
    }
    
    QTabBar::tab {
        background-color: #111111;
        border: 1px solid #1F1F1F;
        border-bottom: none;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        padding: 12px 24px;
        color: #A0A0A0;
        margin-right: 4px;
    }
    
    QTabBar::tab:hover {
        background-color: #1A1A1A;
        color: #FFFFFF;
    }
    
    QTabBar::tab:selected {
        background-color: #1F1F1F;
        color: #FF6B35;
        border-color: #2A2A2A;
    }
    
    /* --- Progress Bar --- */
    QProgressBar {
        background-color: #1F1F1F;
        border-radius: 8px;
        height: 8px;
        text-align: center;
        border: none;
    }
    
    QProgressBar::chunk {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #FF6B35, stop:1 #FF8C5A);
        border-radius: 8px;
    }
    
    /* --- List Widget --- */
    QListWidget {
        background-color: transparent;
        border: none;
        outline: none;
    }
    
    QListWidget::item {
        background-color: transparent;
        border-radius: 8px;
        padding: 12px;
        margin: 2px 0;
    }
    
    QListWidget::item:hover {
        background-color: #1A1A1A;
    }
    
    QListWidget::item:selected {
        background-color: #1F1F1F;
        border-left: 3px solid #FF6B35;
    }
    
    /* --- Table Widget --- */
    QTableWidget {
        background-color: #111111;
        border: 1px solid #1F1F1F;
        border-radius: 12px;
        gridline-color: #1F1F1F;
        selection-background-color: #1F1F1F;
        selection-color: #FFFFFF;
    }
    
    QTableWidget::item {
        padding: 12px;
    }
    
    QTableWidget::item:hover {
        background-color: #1A1A1A;
    }
    
    QHeaderView::section {
        background-color: #0F0F0F;
        border: none;
        border-bottom: 1px solid #1F1F1F;
        padding: 12px;
        color: #666666;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* --- Group Box --- */
    QGroupBox {
        background-color: #111111;
        border: 1px solid #1F1F1F;
        border-radius: 12px;
        margin-top: 12px;
        padding-top: 20px;
        font-weight: 600;
        color: #FFFFFF;
    }
    
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        left: 20px;
        padding: 0 12px;
        color: #FF6B35;
    }
    
    /* --- Tool Tip --- */
    QToolTip {
        background-color: #1F1F1F;
        color: #FFFFFF;
        border: 1px solid #2A2A2A;
        border-radius: 6px;
        padding: 8px 12px;
        font-size: 13px;
    }
    
    /* --- Menu --- */
    QMenu {
        background-color: #111111;
        border: 1px solid #2A2A2A;
        border-radius: 8px;
        padding: 8px;
    }
    
    QMenu::item {
        padding: 10px 20px;
        border-radius: 6px;
        color: #E8E8E8;
    }
    
    QMenu::item:selected {
        background-color: #1F1F1F;
        color: #FF6B35;
    }
    
    QMenu::separator {
        height: 1px;
        background-color: #1F1F1F;
        margin: 8px 0;
    }
    
    /* --- Spin Box --- */
    QSpinBox {
        background-color: #111111;
        border: 1px solid #2A2A2A;
        border-radius: 8px;
        padding: 10px 12px;
        color: #FFFFFF;
        min-height: 40px;
    }
    
    QSpinBox:hover {
        border-color: #3A3A3A;
    }
    
    QSpinBox:focus {
        border-color: #FF6B35;
    }
    
    QSpinBox::up-button,
    QSpinBox::down-button {
        border: none;
        width: 20px;
        subcontrol-origin: border;
    }
    
    QSpinBox::up-button:hover,
    QSpinBox::down-button:hover {
        background-color: #1F1F1F;
    }
    
    /* --- Stack Widget --- */
    QStackedWidget {
        background-color: transparent;
    }
    
    /* --- Frame --- */
    QFrame {
        background-color: transparent;
    }
    
    QFrame#separator {
        background-color: #1F1F1F;
        min-height: 1px;
        max-height: 1px;
    }
    
    QFrame#dotGrid {
        background-color: transparent;
    }
    
    /* --- Status Indicators --- */
    QFrame#statusOnline {
        background-color: #10B981;
        border-radius: 6px;
        min-width: 8px;
        max-width: 8px;
        min-height: 8px;
        max-height: 8px;
    }
    
    QFrame#statusOffline {
        background-color: #EF4444;
        border-radius: 6px;
        min-width: 8px;
        max-width: 8px;
        min-height: 8px;
        max-height: 8px;
    }
    
    QFrame#statusWarning {
        background-color: #F59E0B;
        border-radius: 6px;
        min-width: 8px;
        max-width: 8px;
        min-height: 8px;
        max-height: 8px;
    }
    
    /* --- Badge --- */
    QLabel#badge {
        background-color: #1F1F1F;
        color: #A0A0A0;
        border-radius: 12px;
        padding: 4px 12px;
        font-size: 12px;
        font-weight: 600;
    }
    
    QLabel#badgeSuccess {
        background-color: rgba(16, 185, 129, 0.2);
        color: #10B981;
    }
    
    QLabel#badgeWarning {
        background-color: rgba(245, 158, 11, 0.2);
        color: #F59E0B;
    }
    
    QLabel#badgeError {
        background-color: rgba(239, 68, 68, 0.2);
        color: #EF4444;
    }
    
    QLabel#badgeAccent {
        background-color: rgba(255, 107, 53, 0.2);
        color: #FF6B35;
    }
    
    /* --- Animations hint (for reference) --- */
    /* Use QPropertyAnimation in Python for smooth transitions */
    """
