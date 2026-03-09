"""
Nela Launcher Configuration System
Manages application settings, profiles, and preferences
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime


class ConfigManager:
    """Manages application configuration and settings"""
    
    DEFAULT_CONFIG = {
        "launcher": {
            "theme": "dark",
            "language": "en",
            "close_on_launch": False,
            "check_updates": True,
            "animations_enabled": True,
            "reduced_motion": False,
        },
        "minecraft": {
            "version": "1.16.5",
            "loader": "fabric",
            "java_path": "",
            "memory_min": 512,
            "memory_max": 4096,
            "render_distance": 12,
            "fullscreen": False,
        },
        "paths": {
            "install_dir": "",
            "mods_dir": "",
            "screenshots_dir": "",
            "logs_dir": "",
        },
        "profile": {
            "current": "default",
            "last_played": None,
        },
        "user": {
            "logged_in": False,
            "username": "",
            "uuid": "",
            "token": "",
        },
        "performance": {
            "preset": "balanced",
            "motion_blur": False,
            "motion_blur_intensity": 0.5,
            "vsync": True,
            "fps_limit": 260,
        }
    }
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    return self._merge_configs(self.DEFAULT_CONFIG, loaded)
            except (json.JSONDecodeError, IOError):
                pass
        
        # Create default config
        self.config = self.DEFAULT_CONFIG.copy()
        self.save()
        return self.config
    
    def _merge_configs(self, default: Dict, loaded: Dict) -> Dict:
        """Recursively merge loaded config with defaults"""
        result = default.copy()
        for key, value in loaded.items():
            if key in result:
                if isinstance(value, dict) and isinstance(result[key], dict):
                    result[key] = self._merge_configs(result[key], value)
                else:
                    result[key] = value
        return result
    
    def save(self):
        """Save current configuration to file"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get a configuration value using dot notation
        
        Args:
            key_path: Dot-separated path (e.g., "minecraft.memory_max")
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path: str, value: Any):
        """
        Set a configuration value using dot notation
        
        Args:
            key_path: Dot-separated path
            value: Value to set
        """
        keys = key_path.split('.')
        config = self.config
        
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        config[keys[-1]] = value
        self.save()
    
    def reset_to_defaults(self):
        """Reset configuration to defaults"""
        self.config = self.DEFAULT_CONFIG.copy()
        self.save()
    
    def get_all(self) -> Dict[str, Any]:
        """Get entire configuration"""
        return self.config


class ProfileManager:
    """Manages Minecraft profiles"""
    
    DEFAULT_PROFILE = {
        "name": "Default",
        "version": "1.16.5",
        "loader": "fabric",
        "memory_max": 4096,
        "java_args": "",
        "mods_enabled": [],
        "performance_preset": "balanced",
        "created": None,
        "last_played": None,
        "icon": "default",
    }
    
    def __init__(self, profiles_dir: str = "profiles"):
        self.profiles_dir = Path(profiles_dir)
        self.profiles_dir.mkdir(exist_ok=True)
        self.profiles = self._load_profiles()
    
    def _load_profiles(self) -> Dict[str, Dict]:
        """Load all profiles from directory"""
        profiles = {}
        
        for profile_file in self.profiles_dir.glob("*.json"):
            try:
                with open(profile_file, 'r', encoding='utf-8') as f:
                    profile_data = json.load(f)
                    profile_name = profile_file.stem
                    profiles[profile_name] = profile_data
            except (json.JSONDecodeError, IOError):
                continue
        
        # Create default profile if none exist
        if not profiles:
            default_profile = self.DEFAULT_PROFILE.copy()
            default_profile["created"] = datetime.now().isoformat()
            profiles["default"] = default_profile
            self.save_profile("default", default_profile)
        
        return profiles
    
    def get_profile(self, name: str) -> Optional[Dict]:
        """Get a specific profile"""
        return self.profiles.get(name)
    
    def save_profile(self, name: str, profile: Dict):
        """Save a profile"""
        profile_file = self.profiles_dir / f"{name}.json"
        with open(profile_file, 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)
        self.profiles[name] = profile
    
    def create_profile(self, name: str, base_profile: Optional[str] = None) -> Dict:
        """Create a new profile"""
        if base_profile and base_profile in self.profiles:
            profile = self.profiles[base_profile].copy()
        else:
            profile = self.DEFAULT_PROFILE.copy()
        
        profile["name"] = name
        profile["created"] = datetime.now().isoformat()
        
        self.save_profile(name, profile)
        return profile
    
    def delete_profile(self, name: str) -> bool:
        """Delete a profile"""
        if name in self.profiles and name != "default":
            profile_file = self.profiles_dir / f"{name}.json"
            if profile_file.exists():
                profile_file.unlink()
            del self.profiles[name]
            return True
        return False
    
    def list_profiles(self) -> list:
        """List all profile names"""
        return list(self.profiles.keys())
    
    def update_last_played(self, name: str):
        """Update last played timestamp for a profile"""
        if name in self.profiles:
            self.profiles[name]["last_played"] = datetime.now().isoformat()
            self.save_profile(name, self.profiles[name])
