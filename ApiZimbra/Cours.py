class Cours:
    def __init__(self, emplacement: str, sujet: str, heure: float):
        """
        Constructeur de la classe Cours.

        Args:
            emplacement (str): L'emplacement du cours.
            sujet (str): Le sujet du cours.
            heure (float): L'heure du cours.
            jour (str): Le jour du cours.
        """
        # Attributs de la classe
        self.emplacement = emplacement
        self.sujet = sujets
        self.heure = heure

    def __str__(self):
        """
        Méthode spéciale utilisée pour obtenir une représentation en chaîne de caractères de l'objet.

        Returns:
            str: Une chaîne représentant les détails du cours.
        """
        return f"{self.heure} {self.sujet} {self.emplacement}"
