"""
Home Dashboard
Main landing page with play button, profile info, and status
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QFrame, QScrollArea, QSpacerItem, QSizePolicy, QGridLayout
)
from PySide6.QtCore import Qt, Signal


class HomeDashboard(QWidget):
    """Premium home dashboard with play button and status cards"""
    
    play_clicked = Signal()
    profile_changed = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup home dashboard UI"""
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(24)
        
        # Create scroll area for content
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        
        # Content widget
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(24)
        
        # Header section
        header_section = self._create_header_section()
        content_layout.addWidget(header_section)
        
        # Main content grid
        main_grid = QGridLayout()
        main_grid.setSpacing(24)
        
        # Left column - Play section (wider)
        left_column = QVBoxLayout()
        left_column.setSpacing(24)
        
        # Hero play card
        play_card = self._create_play_card()
        left_column.addWidget(play_card)
        
        # Profile summary
        profile_card = self._create_profile_card()
        left_column.addWidget(profile_card)
        
        # Status indicators
        status_card = self._create_status_card()
        left_column.addWidget(status_card)
        
        left_container = QFrame()
        left_container.setLayout(left_column)
        main_grid.addLayout(left_column, 0, 0, 1, 2)  # Span 2 columns
        
        # Right column - Info cards
        right_column = QVBoxLayout()
        right_column.setSpacing(24)
        
        # News/Updates card
        news_card = self._create_news_card()
        right_column.addWidget(news_card)
        
        # Quick actions
        actions_card = self._create_quick_actions_card()
        right_column.addWidget(actions_card)
        
        # Performance summary
        perf_card = self._create_performance_card()
        right_column.addWidget(perf_card)
        
        right_container = QFrame()
        right_container.setLayout(right_column)
        main_grid.addLayout(right_column, 0, 2, 1, 1)
        
        # Set column stretch
        main_grid.setColumnStretch(0, 3)
        main_grid.setColumnStretch(1, 1)
        main_grid.setColumnStretch(2, 1)
        
        content_layout.addLayout(main_grid)
        
        # Add spacer at bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        content_layout.addItem(spacer)
        
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
    
    def _create_header_section(self) -> QFrame:
        """Create header section with greeting"""
        
        header = QFrame()
        header.setFixedHeight(80)
        layout = QHBoxLayout(header)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Greeting
        greeting_label = QLabel("Good to see you")
        greeting_label.setStyleSheet("""
            font-size: 36px;
            font-weight: 700;
            color: #FFFFFF;
            letter-spacing: 0.5px;
        """)
        layout.addWidget(greeting_label)
        
        layout.addStretch()
        
        # Version badge
        version_badge = QLabel("v1.16.5 • Fabric")
        version_badge.setObjectName("badgeAccent")
        version_badge.setStyleSheet("""
            QLabel#badgeAccent {
                background-color: rgba(255, 107, 53, 0.15);
                color: #FF6B35;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 600;
            }
        """)
        layout.addWidget(version_badge)
        
        return header
    
    def _create_play_card(self) -> QFrame:
        """Create the main play button card"""
        
        card = QFrame()
        card.setObjectName("highlightCard")
        card.setMinimumHeight(280)
        card.setStyleSheet("""
            QFrame#highlightCard {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #111111, stop:1 #161616);
                border: 1px solid #2A2A2A;
                border-radius: 20px;
                padding: 40px;
            }
        """)
        
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(24)
        
        # Profile name
        profile_label = QLabel("Default Profile")
        profile_label.setStyleSheet("""
            font-size: 18px;
            color: #A0A0A0;
            font-weight: 500;
        """)
        profile_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(profile_label)
        
        # Main PLAY button
        self.play_button = QPushButton("PLAY")
        self.play_button.setObjectName("playButton")
        self.play_button.setMinimumSize(320, 80)
        self.play_button.clicked.connect(self.play_clicked.emit)
        layout.addWidget(self.play_button, alignment=Qt.AlignCenter)
        
        # Status text
        status_label = QLabel("Ready to launch • All systems operational")
        status_label.setStyleSheet("""
            font-size: 14px;
            color: #666666;
        """)
        status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(status_label)
        
        return card
    
    def _create_profile_card(self) -> QFrame:
        """Create profile summary card"""
        
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(140)
        
        layout = QHBoxLayout(card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(24)
        
        # Profile icon placeholder
        icon_frame = QFrame()
        icon_frame.setFixedSize(80, 80)
        icon_frame.setStyleSheet("""
            background-color: #1F1F1F;
            border-radius: 12px;
            border: 1px solid #2A2A2A;
        """)
        layout.addWidget(icon_frame)
        
        # Profile info
        info_layout = QVBoxLayout()
        info_layout.setSpacing(8)
        
        title_label = QLabel("Current Profile")
        title_label.setStyleSheet("""
            font-size: 12px;
            color: #666666;
            text-transform: uppercase;
            letter-spacing: 1px;
        """)
        info_layout.addWidget(title_label)
        
        name_label = QLabel("Default")
        name_label.setStyleSheet("""
            font-size: 24px;
            color: #FFFFFF;
            font-weight: 600;
        """)
        info_layout.addWidget(name_label)
        
        details_label = QLabel("Fabric 1.16.5 • 4GB RAM • 28 mods enabled")
        details_label.setStyleSheet("""
            font-size: 14px;
            color: #888888;
        """)
        info_layout.addWidget(details_label)
        
        info_layout.addStretch()
        layout.addLayout(info_layout, 1)
        
        # Change button
        change_btn = QPushButton("Change")
        change_btn.setObjectName("secondaryButton")
        change_btn.setFixedSize(100, 40)
        change_btn.setStyleSheet("""
            QPushButton#secondaryButton {
                background-color: transparent;
                border: 1px solid #2A2A2A;
                color: #A0A0A0;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton#secondaryButton:hover {
                border-color: #FF6B35;
                color: #FF6B35;
            }
        """)
        layout.addWidget(change_btn)
        
        return card
    
    def _create_status_card(self) -> QFrame:
        """Create system status card"""
        
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(120)
        
        layout = QHBoxLayout(card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(24)
        
        # Status items
        status_items = [
            ("Java", "✓ Installed", "#10B981"),
            ("Fabric", "✓ Ready", "#10B981"),
            ("Mods", "28 loaded", "#FF6B35"),
            ("Assets", "✓ Complete", "#10B981"),
        ]
        
        for item in status_items:
            item_layout = QVBoxLayout()
            item_layout.setSpacing(4)
            
            label = QLabel(item[0])
            label.setStyleSheet("""
                font-size: 12px;
                color: #666666;
                text-transform: uppercase;
            """)
            item_layout.addWidget(label)
            
            value_label = QLabel(item[1])
            value_label.setStyleSheet(f"""
                font-size: 16px;
                color: {item[2]};
                font-weight: 600;
            """)
            item_layout.addWidget(value_label)
            
            layout.addLayout(item_layout)
            layout.addSpacing(20)
        
        layout.addStretch()
        
        return card
    
    def _create_news_card(self) -> QFrame:
        """Create news/updates card"""
        
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(200)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)
        
        # Title
        title_label = QLabel("Latest Updates")
        title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #FFFFFF;
        """)
        layout.addWidget(title_label)
        
        # News items
        news_items = [
            ("Performance improvements", "v1.0.0"),
            ("New modpack available", "Dec 15"),
            ("Bug fixes and stability", "Dec 10"),
        ]
        
        for news in news_items:
            news_layout = QHBoxLayout()
            news_layout.setSpacing(12)
            
            dot = QFrame()
            dot.setFixedSize(8, 8)
            dot.setStyleSheet("""
                background-color: #FF6B35;
                border-radius: 4px;
            """)
            news_layout.addWidget(dot)
            
            text_label = QLabel(news[0])
            text_label.setStyleSheet("""
                font-size: 14px;
                color: #E8E8E8;
            """)
            news_layout.addWidget(text_label, 1)
            
            date_label = QLabel(news[1])
            date_label.setStyleSheet("""
                font-size: 12px;
                color: #666666;
            """)
            news_layout.addWidget(date_label)
            
            layout.addLayout(news_layout)
        
        layout.addStretch()
        
        return card
    
    def _create_quick_actions_card(self) -> QFrame:
        """Create quick actions card"""
        
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(160)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)
        
        # Title
        title_label = QLabel("Quick Actions")
        title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #FFFFFF;
        """)
        layout.addWidget(title_label)
        
        # Action buttons grid
        actions_grid = QGridLayout()
        actions_grid.setSpacing(12)
        
        actions = [
            ("⚙", "Settings"),
            ("◫", "Mods"),
            ("📊", "Performance"),
            ("🔧", "Repair"),
        ]
        
        for i, action in enumerate(actions):
            btn = QPushButton(f"{action[0]}  {action[1]}")
            btn.setFixedHeight(44)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #1A1A1A;
                    border: 1px solid #1F1F1F;
                    border-radius: 8px;
                    color: #E8E8E8;
                    font-size: 13px;
                    font-weight: 500;
                    text-align: left;
                    padding-left: 16px;
                }
                QPushButton:hover {
                    border-color: #FF6B35;
                    background-color: #1F1F1F;
                }
            """)
            
            row = i // 2
            col = i % 2
            actions_grid.addWidget(btn, row, col)
        
        layout.addLayout(actions_grid)
        
        return card
    
    def _create_performance_card(self) -> QFrame:
        """Create performance summary card"""
        
        card = QFrame()
        card.setObjectName("card")
        card.setMinimumHeight(140)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)
        
        # Title
        title_label = QLabel("Performance Status")
        title_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #FFFFFF;
        """)
        layout.addWidget(title_label)
        
        # Metrics
        metrics_layout = QHBoxLayout()
        metrics_layout.setSpacing(24)
        
        metrics = [
            ("RAM", "4 GB", "2.1 GB used"),
            ("FPS", "Unlimited", "Optimized"),
            ("Render", "12 chunks", "Balanced"),
        ]
        
        for metric in metrics:
            m_layout = QVBoxLayout()
            m_layout.setSpacing(4)
            
            name_label = QLabel(metric[0])
            name_label.setStyleSheet("""
                font-size: 12px;
                color: #666666;
            """)
            m_layout.addWidget(name_label)
            
            value_label = QLabel(metric[1])
            value_label.setStyleSheet("""
                font-size: 18px;
                color: #FFFFFF;
                font-weight: 600;
            """)
            m_layout.addWidget(value_label)
            
            desc_label = QLabel(metric[2])
            desc_label.setStyleSheet("""
                font-size: 11px;
                color: #888888;
            """)
            m_layout.addWidget(desc_label)
            
            metrics_layout.addLayout(m_layout)
        
        layout.addLayout(metrics_layout)
        
        return card
    
    def update_play_button_state(self, state: str):
        """Update play button state (ready, launching, playing)"""
        
        states = {
            "ready": ("PLAY", "#playButton", True),
            "launching": ("LAUNCHING...", "#playButton", False),
            "playing": ("GAME RUNNING", "#playButton", False),
        }
        
        if state in states:
            text, style, enabled = states[state]
            self.play_button.setText(text)
            self.play_button.setEnabled(enabled)
