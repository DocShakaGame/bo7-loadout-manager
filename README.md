# BO7 Loadout Planner 🎮

**Gestionnaire professionnel de loadouts pour Black Ops 7 - FR Edition**

## Features 🎯

- 📊 Gestion complète des armes et loadouts
- 🔄 Scraper automatique pour mise à jour des données
- 🎨 Interface moderne (Tkinter - Thème GitHub Dark)
- 💾 Sauvegarde JSON persistante
- 🔍 Filtrage avancé (catégorie, tier, recherche)
- 📋 Copie codes loadout au presse-papiers
- 📤 Export CSV

## Installation ⚙️

### Prérequis
- Python 3.9+
- pip

### Setup

```bash
# Clone le repo
git clone https://github.com/USERNAME/bo7-loadout-manager.git
cd bo7-loadout-manager

# Virtual env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dépendances
pip install -r requirements.txt

# Playwright
playwright install chromium
