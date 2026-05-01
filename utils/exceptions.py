"""
Exceptions personnalisées
"""


class BO7Exception(Exception):
    """Exception de base"""
    pass


class ScraperError(BO7Exception):
    """Erreur scraper"""
    pass


class DataLoaderError(BO7Exception):
    """Erreur loader"""
    pass


class ValidationError(BO7Exception):
    """Erreur validation"""
    pass


class ConfigError(BO7Exception):
    """Erreur config"""
    pass


class NetworkError(ScraperError):
    """Erreur réseau"""
    pass


class ParsingError(ScraperError):
    """Erreur parsing"""
    pass


class TimeoutError(NetworkError):
    """Erreur timeout"""
    pass


class InvalidJSONError(DataLoaderError):
    """JSON invalide"""
    pass