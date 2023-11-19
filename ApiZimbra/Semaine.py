from typing import List
from Jour import *

class Semaine:
    def __init__(self, num_semaine: int, jours: List[Jour]):
        """
        Constructeur de la classe Semaine.

        Args:
            num_semaine (int): Le numéro de la semaine.
            jours (List[Jour]): Liste des jours de la semaine.
        """
        # Attributs de la classe
        self.num_semaine = num_semaine
        self.jours = jours
        
    def GetJour(self, num_jour: int) -> Jour or None:
        """
        Récupère un jour en fonction du numéro de jour.

        Args:
            num_jour (int): Le numéro du jour à rechercher.

        Returns:
            Jour or None: Le jour trouvé ou None si aucun jour correspondant n'est trouvé.
        """
        for jour in self.jours:
            if jour.num_jour == num_jour:
                return jour
        return None
    
    def GetJour(self, libelle: str) -> Jour or None:
        """
        Récupère un jour en fonction du libellé.

        Args:
            libelle (str): Le libellé du jour à rechercher.

        Returns:
            Jour or None: Le jour trouvé ou None si aucun jour correspondant n'est trouvé.
        """
        for jour in self.jours:
            if jour.libelle == libelle:
                return jour
        return None
    
    def GetAllJour(self) -> List[Jour]:
        """
        Récupère tous les jours de la semaine.

        Returns:
            List[Jour]: Liste de tous les jours de la semaine.
        """
        return self.jours
    
    def __str__(self):
        """
        Méthode spéciale utilisée pour obtenir une représentation en chaîne de caractères de l'objet.

        Returns:
            str: Une chaîne représentant les détails de la semaine et de ses jours.
        """
        semaine_str = f"Semaine {self.num_semaine}\n"
        for jour in self.jours:
            semaine_str += str(jour) + "\n"
        return semaine_str

