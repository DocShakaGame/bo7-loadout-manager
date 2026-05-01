"""
Constantes du projet
"""

from pathlib import Path

# ────────────────────────────────────────────────────────────────────────────
# PATHS
# ────────────────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
JSON_DIR = DATA_DIR / "json"
LOGS_DIR = PROJECT_ROOT / "logs"
DEFAULT_JSON_FILE = JSON_DIR / "bo7_weapons.json"

# Créer les répertoires s'ils n'existent pas
JSON_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# ────────────────────────────────────────────────────────────────────────────
# SCRAPER
# ────────────────────────────────────────────────────────────────────────────

CODMUNITY_BASE_URL = "https://codmunity.gg/fr/tier-list/bo7"
SCRAPER_TIMEOUT = 30  # secondes
SCRAPER_WAIT_TIME = 2  # secondes entre chaque page

# ────────────────────────────────────────────────────────────────────────────
# UI COLORS (GitHub Dark Theme)
# ────────────────────────────────────────────────────────────────────────────

UI_COLORS = {
    "bg": "#0d1117",           # Background principal
    "fg": "#c9d1d9",           # Texte principal
    "bg_secondary": "#161b22", # Background secondaire
    "fg_secondary": "#8b949e", # Texte secondaire
    "accent": "#58a6ff",       # Accent bleu
    "success": "#3fb950",      # Vert succès
    "warning": "#d29922",      # Jaune warning
    "error": "#f85149",        # Rouge erreur
    "border": "#30363d",       # Bordure
    
    # Tiers
    "tier_s": "#ff6b6b",       # Rouge S
    "tier_a": "#ffa500",       # Orange A
    "tier_b": "#ffd700",       # Or B
    "tier_c": "#90ee90",       # Vert C
    "tier_d": "#87ceeb",       # Bleu D
}

# ────────────────────────────────────────────────────────────────────────────
# TIERS & LABELS
# ────────────────────────────────────────────────────────────────────────────

TIER_LABELS = {
    "S": "🔥 S-Tier (Surpuissant)",
    "A": "⭐ A-Tier (Excellent)",
    "B": "👍 B-Tier (Bon)",
    "C": "📊 C-Tier (Moyen)",
    "D": "⚠️ D-Tier (Faible)",
}

TIER_NOTES = {
    "S": "Arme dominante au méta",
    "A": "Très compétitive",
    "B": "Viable en ranked",
    "C": "Utilisable mais non-optimal",
    "D": "Non recommandée",
}

# ────────────────────────────────────────────────────────────────────────────
# CATEGORIES D'ARMES
# ────────────────────────────────────────────────────────────────────────────

WEAPON_CATEGORIES = {
    "AR": "Assault Rifle",
    "SMG": "Submachine Gun",
    "SG": "Shotgun",
    "SNR": "Sniper Rifle",
    "LMG": "Light Machine Gun",
    "TAC": "Tactical Rifle",
    "MB": "Melee Weapon",
    "PS": "Pistol",
}

# ────────────────────────────────────────────────────────────────────────────
# ACCESSOIRES
# ────────────────────────────────────────────────────────────────────────────

ACCESSOIRES = {
    "scopes": [
        "Réticule point rouge",
        "Lunette 3x",
        "Lunette 4x",
        "Lunette 6x",
        "Lunette 8x",
    ],
    "barrels": [
        "Canon court",
        "Canon long",
        "Canon tactique",
        "Suppresseur",
    ],
    "stocks": [
        "Crosse légère",
        "Crosse équilibrée",
        "Crosse lourde",
    ],
    "grips": [
        "Grip léger",
        "Grip standard",
        "Grip lourd",
    ],
    "magazines": [
        "Chargeur standard",
        "Chargeur étendu",
        "Chargeur haute capacité",
    ],
}

# ────────────────────────────────────────────────────────────────────────────
# ATOUTS (PERKS)
# ────────────────────────────────────────────────────────────────────────────

ATOUTS = {
    "perk1": [
        "Tir rapide",
        "Équilibre",
        "Contrôle",
        "Détection",
    ],
    "perk2": [
        "Santé bonus",
        "Rapidité",
        "Camouflage",
        "Résistance",
    ],
    "perk3": [
        "Détection des ennemis",
        "Récupération rapide",
        "Vigilance",
        "Résilience",
    ],
}

# ────────────────────────────────────────────────────────────────────────────
# EQUIPEMENTS
# ────────────────────────────────────────────────────────────────────────────

EQUIPEMENTS = [
    "Grenade frag",
    "Grenade incendiaire",
    "Grenade stun",
    "Semtex",
    "C4",
    "Drone de surveillance",
    "Claymore",
    "Mine bonheur",
]

# ────────────────────────────────────────────────────────────────────────────
# APP CONFIG
# ────────────────────────────────────────────────────────────────────────────

APP_TITLE = "BO7 · Loadout Planner — FR"
APP_GEOMETRY = "1280x780"
APP_MIN_SIZE = (1100, 650)
APP_THEME = "dark"
APP_LANGUAGE = "FR"

# ────────────────────────────────────────────────────────────────────────────
# LOGGING
# ────────────────────────────────────────────────────────────────────────────

LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# ────────────────────────────────────────────────────────────────────────────
# SOURCES
# ────────────────────────────────────────────────────────────────────────────

SOURCES = [
    "https://codmunity.gg/fr/tier-list/bo7",
]

# ────────────────────────────────────────────────────────────────────────────
# VERSION
# ────────────────────────────────────────────────────────────────────────────

VERSION = "1.0.0"
BUILD = "20250101"
AUTHOR = "DocShaka"