"""
Configuration centralisée de l'application
"""

import os
from pathlib import Path
from typing import List, Dict, Any
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class Settings:
    """Configuration de l'application"""
    
    # ──────────────────────────────────────────────────────────────────────
    # PATHS
    # ──────────────────────────────────────────────────────────────────────
    
    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_DIR = PROJECT_ROOT / "data"
    JSON_DIR = DATA_DIR / "json"
    LOGS_DIR = PROJECT_ROOT / "logs"
    EXPORTS_DIR = DATA_DIR / "exports"
    
    # Fichiers
    DEFAULT_JSON_FILE = JSON_DIR / "bo7_weapons.json"
    SETTINGS_FILE = PROJECT_ROOT / ".settings.json"
    
    # ──────────────────────────────────────────────────────────────────────
    # APP CONFIG
    # ──────────────────────────────────────────────────────────────────────
    
    APP_TITLE = "BO7 · Loadout Planner — FR"
    APP_GEOMETRY = "1280x780"
    APP_MIN_SIZE = (1100, 650)
    VERSION = "1.0.0"
    BUILD = "20250101"
    AUTHOR = "DocShaka"
    REPO = "https://github.com/DocShakaGame/bo7-loadout-manager"
    
    # ──────────────────────────────────────────────────────────────────────
    # SCRAPER CONFIG
    # ──────────────────────────────────────────────────────────────────────
    
    CODMUNITY_BASE_URL = "https://codmunity.gg/fr/tier-list/bo7"
    SCRAPER_HEADLESS = os.getenv("SCRAPER_HEADLESS", "true").lower() == "true"
    SCRAPER_TIMEOUT = int(os.getenv("SCRAPER_TIMEOUT", 120000))
    SCRAPER_WAIT_TIME = int(os.getenv("SCRAPER_WAIT_TIME", 3))
    WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", 1280))
    WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", 780))
    
    # ──────────────────────────────────────────────────────────────────────
    # LOGGING
    # ──────────────────────────────────────────────────────────────────────
    
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    
    # ──────────────────────────────────────────────────────────────────────
    # COLORS (GitHub Dark)
    # ──────────────────────────────────────────────────────────────────────
    
    COLORS = {
        "bg": "#0d1117",
        "fg": "#c9d1d9",
        "bg_secondary": "#161b22",
        "fg_secondary": "#8b949e",
        "accent": "#58a6ff",
        "success": "#3fb950",
        "warning": "#d29922",
        "error": "#f85149",
        "border": "#30363d",
        "tier_s": "#ff6b6b",
        "tier_a": "#ffa500",
        "tier_b": "#ffd700",
        "tier_c": "#90ee90",
        "tier_d": "#87ceeb",
    }
    
    # ──────────────────────────────────────────────────────────────────────
    # TIERS
    # ──────────────────────────────────────────────────────────────────────
    
    TIER_LABELS = {
        "S": "🔥 S-Tier (Surpuissant)",
        "A": "⭐ A-Tier (Excellent)",
        "B": "👍 B-Tier (Bon)",
        "C": "📊 C-Tier (Moyen)",
        "D": "⚠️ D-Tier (Faible)",
    }
    
    # ──────────────────────────────────────────────────────────────────────
    # CATEGORIES
    # ──────────────────────────────────────────────────────────────────────
    
    WEAPON_CATEGORIES = {
        "AR": "Assault Rifle",
        "SMG": "Submachine Gun",
        "SG": "Shotgun",
        "SNR": "Sniper Rifle",
        "LMG": "Light Machine Gun",
        "TAC": "Tactical Rifle",
    }
    
    def __init__(self):
        """Initialiser et créer les répertoires"""
        self._ensure_directories()
    
    def _ensure_directories(self):
        """Créer les répertoires nécessaires"""
        for directory in [self.JSON_DIR, self.LOGS_DIR, self.EXPORTS_DIR]:
            directory.mkdir(parents=True, exist_ok=True)
    
    def get_accessories_for_category(self, category: str) -> List[str]:
        """Obtenir les accessoires recommandés pour une catégorie"""
        recommendations = {
            "AR": ["Lunette 3x", "Canon long", "Grip lourd"],
            "SMG": ["Réticule point rouge", "Canon court", "Crosse légère"],
            "SG": ["Réticule point rouge", "Canon court", "Crosse équilibrée"],
        }
        return recommendations.get(category, [])
    
    def get_perks_for_category(self, category: str) -> List[str]:
        """Obtenir les atouts recommandés"""
        return ["Tir rapide", "Santé bonus", "Détection des ennemis"]
    
    def get_equipment_for_category(self, category: str) -> List[str]:
        """Obtenir l'équipement recommandé"""
        return ["Grenade frag", "Semtex"]


# Instance globale
config = Settings()