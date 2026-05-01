"""
Service de mise à jour des données d'armes
"""
import json
from pathlib import Path
from datetime import datetime
from loguru import logger

# Configuration
DATA_DIR = Path(__file__).parent.parent / "data" / "json"
DATA_FILE = DATA_DIR / "bo7_weapons.json"

class UpdaterService:
    """Service de mise à jour des données"""
    
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
        """Créer un fichier JSON vide"""
        data = {
            "weapons": [],
            "last_updated": datetime.now().isoformat()
        }
        self.save_data(data)
    
    def load_data(self):
        """Charger les données du JSON"""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {"weapons": [], "last_updated": None}
        except Exception as e:
            self.logger.error(f"Erreur de chargement : {e}")
            return {"weapons": [], "last_updated": None}
    
    def save_data(self, data):
        """Sauvegarder les données en JSON"""
        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.logger.info(f"✅ Données sauvegardées : {self.data_file}")
        except Exception as e:
            self.logger.error(f"Erreur de sauvegarde : {e}")
    
    def update_last_modified(self):
        """Mettre à jour la date de dernière modification"""
        data = self.load_data()
        data["last_updated"] = datetime.now().isoformat()
        self.save_data(data)

# Instance globale
updater_service = UpdaterService()
