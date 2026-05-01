"""
Point d'entrée de l'application BO7 Loadout Manager
"""
import sys
from pathlib import Path

# Ajouter le répertoire racine au path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from ui.app import create_app
    from utils.logger import setup_logger
    
    if __name__ == "__main__":
        logger = setup_logger("main")
        logger.info("🚀 Démarrage de l'application BO7 Loadout Manager...")
        
        app = create_app()
        app.mainloop()
        
        logger.info("👋 Application fermée")
except Exception as e:
    print(f"❌ Erreur au démarrage : {e}")
    import traceback
    traceback.print_exc()
