"""
Application principale BO7 Loadout Manager
"""
import customtkinter as ctk
from loguru import logger
from services.weapon_service import weapon_service

logger.enable("ui.app")

def create_main_layout(root, weapons):
    """Créer la disposition principale"""
    
    # Frame principal
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Titre
    title_label = ctk.CTkLabel(
        main_frame,
        text="🔫 BO7 Loadout Manager",
        font=("Arial", 20, "bold")
    )
    title_label.pack(pady=10)
    
    # Info des armes
    info_label = ctk.CTkLabel(
        main_frame,
        text=f"📊 {len(weapons)} armes disponibles",
        font=("Arial", 12)
    )
    info_label.pack(pady=5)
    
    # Frame pour les boutons
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.pack(pady=10)
    
    # Bouton de test
    test_btn = ctk.CTkButton(
        button_frame,
        text="🔄 Recharger les armes",
        command=lambda: reload_weapons(info_label)
    )
    test_btn.pack(side="left", padx=5)
    
    # Bouton quitter
    quit_btn = ctk.CTkButton(
        button_frame,
        text="❌ Quitter",
        command=root.quit,
        fg_color="red"
    )
    quit_btn.pack(side="left", padx=5)
    
    # Texte de bienvenue
    welcome_label = ctk.CTkLabel(
        main_frame,
        text="Bienvenue ! L'application est prête.",
        font=("Arial", 11),
        text_color="gray"
    )
    welcome_label.pack(pady=20)

def reload_weapons(label):
    """Recharger et afficher les armes"""
    try:
        weapons = weapon_service.load_weapons()
        label.configure(text=f"📊 {len(weapons)} armes chargées")
        logger.info(f"✅ Armes rechargées : {len(weapons)}")
    except Exception as e:
        logger.error(f"❌ Erreur lors du rechargement : {e}")

def create_app():
    """Créer et retourner l'application principale"""
    try:
        logger.info("🚀 Initialisation de l'interface...")
        
        # Créer la fenêtre root
        root = ctk.CTk()
        root.title("BO7 Loadout Manager")
        root.geometry("1200x700")
        
        # Configuration du style
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Charger les armes
        weapons = weapon_service.load_weapons()
        logger.info(f"✅ {len(weapons)} armes chargées")
        
        # Créer les widgets principaux
        create_main_layout(root, weapons)
        
        # ✅ RETOURNER SEULEMENT root
        return root
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de la création de l'app : {e}")
        raise
