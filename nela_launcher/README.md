# Nela Launcher

**Minimal outside. Powerful inside.**

A premium modern Minecraft launcher built with Python 3.12+ and PySide6, designed exclusively for Fabric 1.16.5.

## Brand Identity

- **Name:** Nela Launcher
- **Tagline:** Launch clean. Built for Fabric. Designed for players.
- **Style:** Nothing OS inspired industrial minimalism
- **Palette:** Monochrome black/graphite/white with subtle orange accent

## Features

- 🎯 Fabric 1.16.5 only support
- 🎨 Premium Nothing OS-inspired UI
- 🔐 Microsoft authentication
- 📦 30+ curated mods
- 🎮 Skin studio with 3D preview
- ⚡ Performance center with presets
- 🔄 Automatic updates
- 📊 Profile management
- 🛠️ Diagnostic tools

## Project Structure

```
nela_launcher/
├── app/                 # Application bootstrap
├── assets/              # Icons, images, fonts
├── config/              # Configuration files
├── core/                # Launcher engine
├── dialogs/             # Custom dialogs
├── pages/               # UI pages
├── services/            # Background services
├── utils/               # Utilities
├── widgets/             # Reusable UI components
├── styles/              # Styling system
├── logs/                # Log files
├── profiles/            # User profiles
├── mods/                # Mod manifests
└── main.py              # Entry point
```

## Requirements

- Python 3.12+
- PySide6
- requests
- aiohttp

## Installation

```bash
pip install -r requirements.txt
python main.py
```

## Build

```bash
pyinstaller --name="Nela Launcher" --windowed --icon=assets/icons/icon.ico main.py
```

## License

Proprietary - All rights reserved
