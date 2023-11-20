from typing import List
from Jour import *

class Semaine:
    def __init__(self, num_semaine, jours):
        # Attributs de la classe
        self.num_semaine = num_semaine
        self.jours = jours
        
    def GetJour(self, num_jour):
        for jour in self.jours:
            if jour.num_jour == num_jour:
                return jour
        return None
    
    def GetJour(self, libelle):
        for jour in self.jours:
            if jour.libelle == libelle:
                return jour
        return None
    
    def GetAllJour(self):
        return self.jours
    
    def __str__(self):
        semaine_str = f"Semaine {self.num_semaine}\n"
        for jour in self.jours:
            semaine_str += str(jour) + "\n"
        return semaine_str

