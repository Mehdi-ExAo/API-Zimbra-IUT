from Cours import *

class Jour:
    def __init__(self, Cours):
        
        self.Cours = Cours
        
    
    def GetCours(self):
        """
        Récupère la liste des cours pour la journée.

        Returns:
            List[Cour]: Liste des cours pour la journée.
        """
        return self.Cours
        
    def GetCoursParHeure(self, heure: float) -> Cours or None:
        """
       Récupère un cours en fonction de l'heure.

       Args:
           heure (float): L'heure du cours à rechercher.

       Returns:
           Cour or None: Le cours trouvé ou None si aucun cours n'est trouvé.
       """
        for cours in self.Cours:
            if cours.heure == heure:
                return cours
        return None
            
    def __str__(self):
        """
       Méthode spéciale utilisée pour obtenir une représentation en chaîne de caractères de l'objet.

       Returns:
           str: Une chaîne représentant les détails du jour et de ses cours.
       """
        Aafficher = f"======= {self.libelle} ======= \n"
        for cours in self.Cours:
            Aafficher+= str(cours)
            
        return Aafficher
            
        
        