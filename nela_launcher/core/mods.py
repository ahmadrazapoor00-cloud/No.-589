"""
Nela Launcher Mod System
Manages curated modpack for Fabric 1.16.5
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime


class ModManager:
    """Manages Minecraft mods for Fabric 1.16.5"""
    
    # Curated mod list for Fabric 1.16.5
    CURATED_MODS = [
        # Performance
        {
            "id": "sodium",
            "name": "Sodium",
            "description": "Modern rendering engine for massive FPS improvements",
            "category": "performance",
            "version": "mc1.16.5-0.2.0",
            "required": True,
            "impact": "high",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "lithium",
            "name": "Lithium",
            "description": "Game physics, mob AI and entity ticking optimizations",
            "category": "performance",
            "version": "mc1.16.5-0.6.6",
            "required": False,
            "impact": "high",
            "side": "server",
            "dependencies": [],
        },
        {
            "id": "phosphor",
            "name": "Phosphor",
            "description": "Lighting engine optimizations",
            "category": "performance",
            "version": "mc1.16.3-0.7.1",
            "required": False,
            "impact": "medium",
            "side": "both",
            "dependencies": [],
        },
        {
            "id": "starlight",
            "name": "Starlight",
            "description": "Rewrite of Minecraft's lighting engine",
            "category": "performance",
            "version": "1.0.0-RC1",
            "required": False,
            "impact": "high",
            "side": "both",
            "dependencies": [],
        },
        # Visual Polish
        {
            "id": "iris",
            "name": "Iris Shaders",
            "description": "Modern shaders support with excellent performance",
            "category": "visual",
            "version": "1.1.0",
            "required": False,
            "impact": "medium",
            "side": "client",
            "dependencies": ["sodium"],
        },
        {
            "id": "continuity",
            "name": "Continuity",
            "description": "Connected textures support",
            "category": "visual",
            "version": "1.0.0",
            "required": False,
            "impact": "low",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "visual_overhaul",
            "name": "Visual Overhaul",
            "description": "Particle and visual enhancements",
            "category": "visual",
            "version": "1.4.0",
            "required": False,
            "impact": "low",
            "side": "client",
            "dependencies": [],
        },
        # Quality of Life
        {
            "id": "appleskin",
            "name": "AppleSkin",
            "description": "Shows food saturation and hunger values",
            "category": "qol",
            "version": "mc1.16.4-1.0.11",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "journeymap",
            "name": "JourneyMap",
            "description": "Real-time mapping with waypoints",
            "category": "qol",
            "version": "5.7.1",
            "required": False,
            "impact": "low",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "jei",
            "name": "JEI (Just Enough Items)",
            "description": "View recipes and item information",
            "category": "qol",
            "version": "7.7.1.123",
            "required": False,
            "impact": "low",
            "side": "both",
            "dependencies": [],
        },
        {
            "id": "mouse_tweaks",
            "name": "Mouse Tweaks",
            "description": "Enhanced inventory management",
            "category": "qol",
            "version": "2.14",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "inventory_profiles",
            "name": "Inventory Profiles",
            "description": "Advanced inventory management tools",
            "category": "qol",
            "version": "fabric-mc1.16.4-0.8.2",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        # HUD / Interface
        {
            "id": "armor_hud",
            "name": "Armor Status HUD",
            "description": "Displays armor durability on screen",
            "category": "hud",
            "version": "1.2.0",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "status_effect_hud",
            "name": "Status Effect HUD",
            "description": "Shows active potion effects",
            "category": "hud",
            "version": "1.0.4",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "coordinates_hud",
            "name": "Coordinates HUD",
            "description": "Display coordinates and dimension",
            "category": "hud",
            "version": "1.1.2",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "keystrokes",
            "name": "Keystrokes",
            "description": "Display pressed keys on screen",
            "category": "hud",
            "version": "1.0.0",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "ping_display",
            "name": "Ping Display",
            "description": "Show server ping in corner",
            "category": "hud",
            "version": "1.0.0",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        # Utility
        {
            "id": "worldedit",
            "name": "WorldEdit",
            "description": "In-game world editor for creators",
            "category": "utility",
            "version": "7.2.5",
            "required": False,
            "impact": "none",
            "side": "both",
            "dependencies": [],
        },
        {
            "id": "replaymod",
            "name": "Replay Mod",
            "description": "Record and share gameplay sessions",
            "category": "utility",
            "version": "2.6.1",
            "required": False,
            "impact": "medium",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "screenshot_viewer",
            "name": "Screenshot Viewer",
            "description": "Browse screenshots in-game",
            "category": "utility",
            "version": "1.2.0",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        # Chat Improvements
        {
            "id": "chat_heads",
            "name": "Chat Heads",
            "description": "Show player heads in chat",
            "category": "chat",
            "version": "0.4.0",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "chat_filter",
            "name": "Chat Filter",
            "description": "Filter unwanted chat messages",
            "category": "chat",
            "version": "1.0.0",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        # Fabric API (Required)
        {
            "id": "fabric_api",
            "name": "Fabric API",
            "description": "Core Fabric API required by most mods",
            "category": "core",
            "version": "0.34.9+1.16",
            "required": True,
            "impact": "none",
            "side": "both",
            "dependencies": [],
        },
        # Additional Performance
        {
            "id": "lazydfu",
            "name": "LazyDFU",
            "description": "Defers initialization for faster startup",
            "category": "performance",
            "version": "0.1.3",
            "required": False,
            "impact": "medium",
            "side": "both",
            "dependencies": [],
        },
        {
            "id": "krypton",
            "name": "Krypton",
            "description": "Networking stack improvements",
            "category": "performance",
            "version": "0.1.3",
            "required": False,
            "impact": "low",
            "side": "both",
            "dependencies": [],
        },
        {
            "id": "ferritecore",
            "name": "FerriteCore",
            "description": "Memory usage reductions",
            "category": "performance",
            "version": "2.1.0",
            "required": False,
            "impact": "high",
            "side": "both",
            "dependencies": [],
        },
        # Visual Extras
        {
            "id": "entity_culling",
            "name": "Entity Culling",
            "description": "Skip rendering entities behind blocks",
            "category": "visual",
            "version": "1.3.0",
            "required": False,
            "impact": "medium",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "smooth_boot",
            "name": "Smooth Boot",
            "description": "Smoother game startup experience",
            "category": "performance",
            "version": "1.4.0",
            "required": False,
            "impact": "low",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "borderless_mining",
            "name": "Borderless Mining",
            "description": "True fullscreen without alt-tab issues",
            "category": "qol",
            "version": "1.0.2",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "zoomify",
            "name": "Zoomify",
            "description": "Optifine-like zoom feature",
            "category": "qol",
            "version": "2.0.0",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
        {
            "id": "animatica",
            "name": "Animatica",
            "description": "Custom animated textures support",
            "category": "visual",
            "version": "0.4+1.16",
            "required": False,
            "impact": "none",
            "side": "client",
            "dependencies": [],
        },
    ]
    
    def __init__(self, mods_dir: str = "mods"):
        self.mods_dir = Path(mods_dir)
        self.mods_dir.mkdir(exist_ok=True)
        self.mods_state_file = self.mods_dir / "mods_state.json"
        self.mods_state = self._load_state()
    
    def _load_state(self) -> Dict[str, Any]:
        """Load mod enable/disable state"""
        if self.mods_state_file.exists():
            try:
                with open(self.mods_state_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        
        # Default: enable all required mods, disable optional
        state = {"enabled": []}
        for mod in self.CURATED_MODS:
            if mod["required"]:
                state["enabled"].append(mod["id"])
        
        self._save_state(state)
        return state
    
    def _save_state(self, state: Dict[str, Any]):
        """Save mod state to file"""
        with open(self.mods_state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
        self.mods_state = state
    
    def get_all_mods(self) -> List[Dict]:
        """Get all curated mods"""
        return self.CURATED_MODS.copy()
    
    def get_mod_by_id(self, mod_id: str) -> Optional[Dict]:
        """Get a specific mod by ID"""
        for mod in self.CURATED_MODS:
            if mod["id"] == mod_id:
                return mod.copy()
        return None
    
    def get_mods_by_category(self, category: str) -> List[Dict]:
        """Get mods filtered by category"""
        return [mod.copy() for mod in self.CURATED_MODS if mod["category"] == category]
    
    def is_mod_enabled(self, mod_id: str) -> bool:
        """Check if a mod is enabled"""
        return mod_id in self.mods_state.get("enabled", [])
    
    def toggle_mod(self, mod_id: str, enabled: bool):
        """Enable or disable a mod"""
        mod = self.get_mod_by_id(mod_id)
        if not mod:
            return False
        
        # Can't disable required mods
        if not enabled and mod["required"]:
            return False
        
        if enabled:
            if mod_id not in self.mods_state["enabled"]:
                self.mods_state["enabled"].append(mod_id)
        else:
            if mod_id in self.mods_state["enabled"]:
                self.mods_state["enabled"].remove(mod_id)
        
        self._save_state(self.mods_state)
        return True
    
    def get_enabled_mods(self) -> List[Dict]:
        """Get list of enabled mods"""
        enabled_ids = self.mods_state.get("enabled", [])
        return [mod for mod in self.CURATED_MODS if mod["id"] in enabled_ids]
    
    def get_disabled_mods(self) -> List[Dict]:
        """Get list of disabled mods"""
        enabled_ids = self.mods_state.get("enabled", [])
        return [mod for mod in self.CURATED_MODS if mod["id"] not in enabled_ids]
    
    def reset_to_defaults(self):
        """Reset all mod states to defaults"""
        self.mods_state = {"enabled": []}
        for mod in self.CURATED_MODS:
            if mod["required"]:
                self.mods_state["enabled"].append(mod["id"])
        self._save_state(self.mods_state)
    
    def get_categories(self) -> List[str]:
        """Get unique mod categories"""
        categories = set()
        for mod in self.CURATED_MODS:
            categories.add(mod["category"])
        return sorted(list(categories))
    
    def search_mods(self, query: str) -> List[Dict]:
        """Search mods by name or description"""
        query = query.lower()
        results = []
        for mod in self.CURATED_MODS:
            if query in mod["name"].lower() or query in mod["description"].lower():
                results.append(mod.copy())
        return results
    
    def has_conflicts(self, mod_id: str) -> List[str]:
        """Check for potential mod conflicts"""
        # Simplified conflict detection
        conflicts = []
        mod = self.get_mod_by_id(mod_id)
        if not mod:
            return conflicts
        
        # Example: Starlight conflicts with Phosphor
        if mod_id == "starlight":
            if self.is_mod_enabled("phosphor"):
                conflicts.append("phosphor")
        elif mod_id == "phosphor":
            if self.is_mod_enabled("starlight"):
                conflicts.append("starlight")
        
        return conflicts
