"""
Service de gestion des armes
"""
import json
from pathlib import Path
from loguru import logger
from typing import List, Dict, Optional

# Configuration
DATA_DIR = Path(__file__).parent.parent / "data" / "json"
DATA_FILE = DATA_DIR / "bo7_weapons.json"

class WeaponService:
    """Service pour gérer les armes"""
    
    def __init__(self):
        self.data_file = DATA_FILE
        self.logger = logger
        self._ensure_data_dir()
    
    def _ensure_data_dir(self):
        """S'assurer que le répertoire existe"""
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            self._create_empty_data()
    
    def _create_empty_data(self):
        """Créer un fichier JSON vide avec données de test"""
        data = {
            "weapons": [
                {
                    "id": 1,
                    "name": "XM4",
                    "type": "Assault Rifle",
                    "damage": 40,
                    "range": 60,
                    "accuracy": 70,
                    "rof": 750
                },
                {
                    "id": 2,
                    "name": "GPMG-7",
                    "type": "Light Machine Gun",
                    "damage": 35,
                    "range": 55,
                    "accuracy": 60,
                    "rof": 700
                },
                {
                    "id": 3,
                    "name": "LW3A1 Frostline",
                    "type": "Sniper Rifle",
                    "damage": 100,
                    "range": 100,
                    "accuracy": 95,
                    "rof": 50
                }
            ],
            "last_updated": None
        }
        self.save_data(data)
        self.logger.info("✅ Données initiales créées")
    
    def load_weapons(self) -> List[Dict]:
        """Charger toutes les armes"""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get("weapons", [])
            return []
        except Exception as e:
            self.logger.error(f"❌ Erreur de chargement : {e}")
            return []
    
    def get_weapon_by_id(self, weapon_id: int) -> Optional[Dict]:
        """Récupérer une arme par ID"""
        weapons = self.load_weapons()
        for weapon in weapons:
            if weapon.get("id") == weapon_id:
                return weapon
        return None
    
    def get_weapons_by_type(self, weapon_type: str) -> List[Dict]:
        """Récupérer les armes d'un type spécifique"""
        weapons = self.load_weapons()
        return [w for w in weapons if w.get("type") == weapon_type]
    
    def add_weapon(self, weapon: Dict) -> bool:
        """Ajouter une arme"""
        try:
            data = self._load_all_data()
            
            # Générer un ID unique
            max_id = max([w.get("id", 0) for w in data["weapons"]], default=0)
            weapon["id"] = max_id + 1
            
            data["weapons"].append(weapon)
            self.save_data(data)
            self.logger.info(f"✅ Arme ajoutée : {weapon.get('name')}")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'ajout : {e}")
            return False
    
    def update_weapon(self, weapon_id: int, updates: Dict) -> bool:
        """Mettre à jour une arme"""
        try:
            data = self._load_all_data()
            
            for weapon in data["weapons"]:
                if weapon.get("id") == weapon_id:
                    weapon.update(updates)
                    self.save_data(data)
                    self.logger.info(f"✅ Arme mise à jour : {weapon.get('name')}")
                    return True
            
            self.logger.warning(f"⚠️ Arme non trouvée : {weapon_id}")
            return False
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la mise à jour : {e}")
            return False
    
    def delete_weapon(self, weapon_id: int) -> bool:
        """Supprimer une arme"""
        try:
            data = self._load_all_data()
            
            original_count = len(data["weapons"])
            data["weapons"] = [w for w in data["weapons"] if w.get("id") != weapon_id]
            
            if len(data["weapons"]) < original_count:
                self.save_data(data)
                self.logger.info(f"✅ Arme supprimée : {weapon_id}")
                return True
            
            self.logger.warning(f"⚠️ Arme non trouvée : {weapon_id}")
            return False
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la suppression : {e}")
            return False
    
    def _load_all_data(self) -> Dict:
        """Charger toutes les données (interne)"""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {"weapons": [], "last_updated": None}
        except Exception as e:
            self.logger.error(f"❌ Erreur de chargement : {e}")
            return {"weapons": [], "last_updated": None}
    
    def save_data(self, data: Dict) -> bool:
        """Sauvegarder les données"""
        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.logger.info(f"✅ Données sauvegardées")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erreur de sauvegarde : {e}")
            return False
    
    def get_stats(self) -> Dict:
        """Obtenir les statistiques"""
        weapons = self.load_weapons()
        types = {}
        
        for weapon in weapons:
            weapon_type = weapon.get("type", "Unknown")
            types[weapon_type] = types.get(weapon_type, 0) + 1
        
        return {
            "total_weapons": len(weapons),
            "types": types
        }

# Instance globale
weapon_service = WeaponService()
