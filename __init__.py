"""
BO7 Loadout Manager
"""

__version__ = "1.0.0"
__author__ = "DocShaka"

from config.settings import config
from services.weapon_service import weapon_service
from services.updater_service import updater_service

__all__ = [
    "config",
    "weapon_service",
    "updater_service",
]
