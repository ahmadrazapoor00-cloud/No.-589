# Nela Launcher - Complete Project Documentation

## Overview

Nela Launcher is a premium, modern Minecraft launcher built exclusively for Fabric 1.16.5. It features a Nothing OS-inspired industrial minimalism design with a focus on performance, elegance, and user experience.

---

## Brand Identity

### Name
**Nela Launcher**

### Tagline
- "Minimal outside. Powerful inside."
- "Launch clean."
- "Built for Fabric. Designed for players."

### Visual Style
- **Inspiration:** Nothing OS industrial minimalism
- **Palette:** Monochrome (black/graphite/white) with subtle orange accent (#FF6B35)
- **Feel:** Premium, futuristic, gaming-tech, elegant

### Logo Concept
- Strong geometric "N" monogram
- Industrial tech aesthetic
- Works well on dark backgrounds
- Can incorporate dot-matrix or ring elements

---

## Technical Architecture

### Tech Stack
- **Language:** Python 3.12+
- **UI Framework:** PySide6 (Qt for Python)
- **Data Storage:** JSON for configs, profiles, manifests
- **Networking:** requests/aiohttp for downloads
- **Threading:** QThread for background tasks
- **Packaging:** PyInstaller ready

### Folder Structure
```
nela_launcher/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── app/                   # Application bootstrap
│   ├── __init__.py
│   └── bootstrap.py       # Main window & initialization
├── assets/                # Static resources
│   ├── icons/             # Application icons
│   ├── images/            # Images and textures
│   └── fonts/             # Custom fonts
├── config/                # Configuration files
│   └── config.json        # User settings
├── core/                  # Core launcher logic
│   ├── __init__.py
│   ├── config.py          # Config & profile management
│   ├── mods.py            # Mod management system
│   └── launcher.py        # Minecraft launch engine
├── dialogs/               # Custom dialogs
│   └── __init__.py
├── pages/                 # UI pages
│   ├── __init__.py
│   ├── splash_page.py     # Animated splash screen
│   ├── welcome_page.py    # Onboarding page
│   ├── login_page.py      # Authentication page
│   └── home_dashboard.py  # Main dashboard
├── services/              # Background services
│   └── __init__.py
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── logger.py          # Logging system
├── widgets/               # Reusable UI components
│   ├── __init__.py
│   ├── title_bar.py       # Custom title bar
│   └── sidebar.py         # Navigation sidebar
├── styles/                # Styling system
│   ├── __init__.py
│   └── stylesheet.py      # Main QSS stylesheet
├── logs/                  # Log files
├── profiles/              # User profiles
└── mods/                  # Mod files & manifests
```

---

## Design System

### Color Palette
```css
/* Primary Colors */
--bg-primary: #0A0A0A;
--bg-secondary: #0F0F0F;
--bg-card: #111111;
--bg-hover: #1A1A1A;

/* Accent */
--accent-primary: #FF6B35;
--accent-hover: #FF7B4D;
--accent-active: #E55A2B;

/* Text */
--text-primary: #FFFFFF;
--text-secondary: #E8E8E8;
--text-muted: #A0A0A0;
--text-disabled: #666666;

/* Borders */
--border-subtle: #1F1F1F;
--border-default: #2A2A2A;
--border-strong: #3A3A3A;

/* Status */
--success: #10B981;
--warning: #F59E0B;
--error: #EF4444;
```

### Typography
- **Font Family:** Inter, Segoe UI, Arial
- **Heading:** 28-56px, weight 700
- **Subheading:** 18px, weight 600
- **Body:** 14px, weight 400-500
- **Caption:** 12px, weight 600, uppercase

### Spacing Scale
- 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px

### Border Radius
- Small: 6px
- Default: 8px
- Medium: 12px
- Large: 16px
- XL: 20px

---

## Core Features

### 1. Launcher Core
- Launch Minecraft 1.16.5 Fabric exclusively
- Java detection and management
- Memory allocation control
- Launch command construction
- Directory management
- File validation
- Error recovery

### 2. Authentication
- Microsoft OAuth integration
- Offline mode support
- Session management
- Skin synchronization

### 3. Profile System
- Create/delete/duplicate profiles
- Per-profile settings
- Performance presets
- Mod configurations
- Custom icons/banners

### 4. Mod Manager
- 30+ curated mods across categories:
  - **Performance:** Sodium, Lithium, Phosphor, Starlight, etc.
  - **Visual:** Iris Shaders, Continuity, Entity Culling
  - **QoL:** JourneyMap, JEI, AppleSkin, Mouse Tweaks
  - **HUD:** Armor Status, Coordinates, Keystrokes, Ping Display
  - **Utility:** WorldEdit, Replay Mod, Screenshot Viewer
  - **Chat:** Chat Heads, Chat Filter
- Enable/disable toggles
- Conflict detection
- Dependency management
- Impact indicators

### 5. Skin Studio
- Live 3D skin preview
- Rotate model view
- Slim/classic model switch
- Upload local skins
- Account skin sync
- Skin history

### 6. Performance Center
- RAM allocation slider (512MB - 16GB)
- Performance presets:
  - Low-end
  - Balanced
  - Performance
  - Creator/Recording
- Motion blur toggle with intensity slider
- VSync control
- FPS limiter
- Render distance adjustment

### 7. Update System
- Launcher self-updates
- Modpack updates
- Version changelogs
- Background update checks
- Rollback capability

### 8. Settings
- Launcher preferences
- Theme options
- Animation controls
- Install paths
- Download settings
- Log verbosity
- Close-on-launch toggle

### 9. Diagnostics
- Readable log viewer
- Copy log functionality
- Open log folder
- Crash summaries
- Repair suggestions

---

## UI Pages

### 1. Splash Screen
- Animated Nela logo
- Loading dots animation
- Version display
- Fade transitions

### 2. Welcome Page
- Hero greeting
- Feature highlight cards
- Get Started CTA
- Learn More option

### 3. Login Page
- Microsoft sign-in button
- Offline mode option
- Feature benefits list
- Status messages

### 4. Home Dashboard
- Giant Play button
- Current profile card
- System status indicators
- News/updates feed
- Quick actions grid
- Performance summary

### 5. Play Page
- Launch configuration
- Mod selection
- Performance settings
- Launch confirmation

### 6. Profiles Page
- Profile list/grid
- Create new profile
- Edit profile settings
- Delete/duplicate actions

### 7. Mods Page
- Category tabs
- Search functionality
- Mod cards with toggles
- Impact badges
- Conflict warnings

### 8. Skin Studio
- 3D model preview
- Skin upload
- Model type selector
- Skin history

### 9. Performance Center
- RAM slider
- Preset cards
- Advanced settings
- Motion blur controls

### 10. Updates Page
- Available updates list
- Changelog viewer
- Update all button
- Individual update toggles

### 11. Settings Page
- Categorized settings
- Search functionality
- Reset to defaults
- Import/export configs

### 12. Logs Page
- Log file viewer
- Filter by level
- Copy/open actions
- Crash report analysis

### 13. About Page
- App information
- Credits
- Links
- License info

---

## UX Micro-interactions

### Animations
- Page transitions (fade/slide)
- Button hover states
- Card hover elevations
- Loading skeletons
- Progress animations
- Dot loading indicators
- Toggle switches
- Slider value updates

### Feedback
- Hover highlights on interactive elements
- Press state feedback
- Loading spinners
- Success/error toasts
- Progress indicators
- Status badges

### States
- Empty states with illustrations
- Loading states with skeletons
- Error states with recovery options
- Success confirmations
- Disabled state styling

---

## Mod Categories & Bundle Logic

### Performance Bundle (Recommended)
- Sodium (required)
- Lithium
- FerriteCore
- LazyDFU
- Krypton
- Smooth Boot

### Visual Bundle
- Iris Shaders
- Continuity
- Entity Culling
- Animatica
- Visual Overhaul

### QoL Bundle
- JourneyMap
- JEI
- AppleSkin
- Mouse Tweaks
- Zoomify
- Borderless Mining

### HUD Bundle
- Armor Status HUD
- Status Effect HUD
- Coordinates HUD
- Keystrokes
- Ping Display

### Creator Bundle
- WorldEdit
- Replay Mod
- Screenshot Viewer

---

## Security & Compliance

### Strictly Prohibited
- ❌ No Forge support
- ❌ No multi-version support
- ❌ No hacked client features
- ❌ No cheats (aimbot, killaura, reach, fly, xray)
- ❌ No anti-cheat bypass
- ❌ No packet exploits
- ❌ No piracy/cracked launcher logic
- ❌ No malicious telemetry
- ❌ No account stealing
- ❌ No session abuse
- ❌ No copied Feather/Lunar assets

### Allowed Features
- ✅ Fair-play visual enhancements
- ✅ Performance optimizations
- ✅ Quality of life improvements
- ✅ Creator tools
- ✅ HUD displays (non-advantageous)
- ✅ Menu/UI polish

---

## Installation Flow

1. **Splash Screen** - Animated logo (3 seconds)
2. **Welcome Screen** - Introduction and features
3. **Login** - Microsoft auth or offline mode
4. **Install Location** - Choose installation directory
5. **Java Detection** - Auto-detect or guided setup
6. **Fabric Setup** - Install Fabric loader 1.16.5
7. **Modpack Install** - Download curated mods
8. **Progress States** - Elegant progress visualization
9. **Home Dashboard** - Enter main interface
10. **Launch** - Ready to play

---

## Packaging & Distribution

### PyInstaller Build
```bash
pyinstaller --name="Nela Launcher" \
            --windowed \
            --icon=assets/icons/icon.ico \
            --add-data="assets:assets" \
            --add-data="config:config" \
            --hidden-import=PySide6 \
            main.py
```

### Platform Support
- Windows 10/11 (primary)
- macOS (optional)
- Linux (optional)

---

## Future Enhancements

### Phase 2
- Cloud save synchronization
- Friend system integration
- Server browser
- Mod auto-updates
- Theme customization
- Plugin system

### Phase 3
- Mobile companion app
- Web dashboard
- Community features
- Mod marketplace
- Analytics dashboard (opt-in)

---

## Development Guidelines

### Code Quality
- Type hints throughout
- Docstrings for public APIs
- Separation of concerns
- DRY principles
- Error handling
- Logging everywhere

### UI/UX Standards
- Consistent spacing
- Proper hierarchy
- Accessible contrast
- Keyboard navigation
- Responsive layouts
- Smooth animations

### Testing
- Unit tests for core logic
- Integration tests for launcher
- UI testing with pytest-qt
- Manual QA checklist

---

## License

Proprietary - All rights reserved

---

## Contact

For questions, support, or contributions, please refer to the official Nela Launcher repository.
