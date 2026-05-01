"""
Modèles de données pour les armes BO7
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
from enum import Enum


class Tier(str, Enum):
    """Énumération des tiers"""
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class Category(str, Enum):
    """Énumération des catégories"""
    AR = "AR"
    SMG = "SMG"
    SG = "SG"
    SNR = "SNR"
    LMG = "LMG"
    TAC = "TAC"


@dataclass
class Accessory:
    """Accessoire d'arme"""
    name: str
    description: str = ""
    category: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Weapon:
    """Modèle d'une arme"""
    id: str
    name: str
    category: Category
    tier: Tier
    damage: float = 0.0
    range: float = 0.0
    accuracy: float = 0.0
    magazine_capacity: int = 0
    fire_rate: float = 0.0
    description: str = ""
    accessories: List[Accessory] = field(default_factory=list)
    perks: List[str] = field(default_factory=list)
    equipment: List[str] = field(default_factory=list)
    meta_score: float = 0.0
    date_added: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir en dictionnaire"""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "tier": self.tier.value,
            "damage": self.damage,
            "range": self.range,
            "accuracy": self.accuracy,
            "magazine_capacity": self.magazine_capacity,
            "fire_rate": self.fire_rate,
            "description": self.description,
            "accessories": [a.to_dict() for a in self.accessories],
            "perks": self.perks,
            "equipment": self.equipment,
            "meta_score": self.meta_score,
            "date_added": self.date_added,
        }
    
    def to_simple_dict(self) -> Dict[str, Any]:
        """Convertir en dictionnaire simplifié"""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "tier": self.tier.value,
            "meta_score": self.meta_score,
        }
    
    def __str__(self):
        return f"[{self.tier}] {self.name} ({self.category.value})"
    
    def __repr__(self):
        return f"<Weapon: {self.name}>"


@dataclass
class Loadout:
    """Loadout complet (primaire + secondaire + équipement)"""
    id: str
    name: str
    primary_weapon: Weapon
    secondary_weapon: Optional[Weapon] = None
    equipment: List[str] = field(default_factory=list)
    perks: List[str] = field(default_factory=list)
    notes: str = ""
    date_created: str = ""
    date_modified: str = ""
    is_favorite: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertir en dictionnaire"""
        return {
            "id": self.id,
            "name": self.name,
            "primary_weapon": self.primary_weapon.to_dict(),
            "secondary_weapon": self.secondary_weapon.to_dict() if self.secondary_weapon else None,
            "equipment": self.equipment,
            "perks": self.perks,
            "notes": self.notes,
            "date_created": self.date_created,
            "date_modified": self.date_modified,
            "is_favorite": self.is_favorite,
        }
    
    def __str__(self):
        secondary = f" + {self.secondary_weapon.name}" if self.secondary_weapon else ""
        return f"{self.name}: {self.primary_weapon.name}{secondary}"