"""
Nela Launcher - Premium Minecraft Fabric 1.16.5 Launcher
Main Entry Point

Minimal outside. Powerful inside.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QFont, QFontDatabase

from app.bootstrap import NelaApplication
from utils.logger import setup_logger


def main():
    """Main entry point for Nela Launcher"""
    
    # Enable High DPI scaling
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    # Create application instance
    app = QApplication(sys.argv)
    app.setApplicationName("Nela Launcher")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Nela")
    
    # Set application style
    app.setStyle("Fusion")
    
    # Setup logging
    logger = setup_logger()
    logger.info("Starting Nela Launcher...")
    
    # Create and show main application
    nela_app = NelaApplication()
    nela_app.show()
    
    # Run event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
