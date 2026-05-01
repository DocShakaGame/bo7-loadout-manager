"""
Chargeur de données JSON
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

from models.weapon import Weapon, Category, Tier, Accessory
from config.settings import config
from utils.exceptions import DataLoaderError, InvalidJSONError

logger = logging.getLogger(__name__)


class DataLoader:
    """Gère le chargement et sauvegarde des données"""
    
    def __init__(self, json_file: Path = None):
        """
        Initialiser le loader
        
        Args:
            json_file: Chemin du fichier JSON (par défaut config.DEFAULT_JSON_FILE)
        """
        self.json_file = json_file or config.DEFAULT_JSON_FILE
        self.weapons: List[Weapon] = []
        self._load_data()
    
    def _load_data(self):
        """Charger les données depuis le JSON"""
        try:
            if not self.json_file.exists():
                logger.warning(f"⚠️ Fichier non trouvé : {self.json_file}")
                self.weapons = []
                return
            
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.weapons = self._parse_weapons(data.get("weapons", []))
            logger.info(f"✅ {len(self.weapons)} armes chargées")
            
        except json.JSONDecodeError as e:
            logger.error(f"❌ JSON invalide : {e}")
            raise InvalidJSONError(f"JSON invalide dans {self.json_file}")
        except Exception as e:
            logger.error(f"❌ Erreur lors du chargement : {e}")
            raise DataLoaderError(str(e))
    
    def _parse_weapons(self, weapons_data: List[Dict]) -> List[Weapon]:
        """Parser les données d'armes"""
        weapons = []
        for w in weapons_data:
            try:
                weapon = Weapon(
                    id=w.get("id", ""),
                    name=w.get("name", "Unknown"),
                    category=Category[w.get("category", "AR")],
                    tier=Tier[w.get("tier", "C")],
                    damage=float(w.get("damage", 0)),
                    range=float(w.get("range", 0)),
                    accuracy=float(w.get("accuracy", 0)),
                    magazine_capacity=int(w.get("magazine_capacity", 0)),
                    fire_rate=float(w.get("fire_rate", 0)),
                    description=w.get("description", ""),
                    meta_score=float(w.get("meta_score", 0)),
                    date_added=w.get("date_added", datetime.now().isoformat()),
                )
                weapons.append(weapon)
            except Exception as e:
                logger.warning(f"⚠️ Erreur parsing arme {w.get('name')} : {e}")
        
        return weapons
    
    def save_weapons(self, weapons: List[Weapon] = None):
        """Sauvegarder les armes en JSON"""
        try:
            weapons_to_save = weapons or self.weapons
            data = {
                "version": config.VERSION,
                "date_updated": datetime.now().isoformat(),
                "total": len(weapons_to_save),
                "weapons": [w.to_dict() for w in weapons_to_save],
            }
            
            self.json_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ {len(weapons_to_save)} armes sauvegardées")
            
        except Exception as e:
            logger.error(f"❌ Erreur sauvegarde : {e}")
            raise DataLoaderError(str(e))
    
    def get_weapons_by_tier(self, tier: str) -> List[Weapon]:
        """Obtenir les armes par tier"""
        return [w for w in self.weapons if w.tier.value == tier]
    
    def get_weapons_by_category(self, category: str) -> List[Weapon]:
        """Obtenir les armes par catégorie"""
        return [w for w in self.weapons if w.category.value == category]
    
    def search_weapon(self, query: str) -> List[Weapon]:
        """Chercher une arme par nom"""
        query = query.lower()
        return [w for w in self.weapons if query in w.name.lower()]
    
    def get_weapon_by_id(self, weapon_id: str) -> Optional[Weapon]:
        """Obtenir une arme par ID"""
        for w in self.weapons:
            if w.id == weapon_id:
                return w
        return None
    
    def get_stats(self) -> Dict[str, Any]:
        """Obtenir les statistiques"""
        return {
            "total": len(self.weapons),
            "by_tier": {
                tier: len(self.get_weapons_by_tier(tier))
                for tier in ["S", "A", "B", "C", "D"]
            },
            "by_category": {
                cat: len(self.get_weapons_by_category(cat))
                for cat in config.WEAPON_CATEGORIES.keys()
            },
            "avg_meta_score": (
                sum(w.meta_score for w in self.weapons) / len(self.weapons)
                if self.weapons else 0
            ),
        }


# Instance globale
loader = DataLoader()