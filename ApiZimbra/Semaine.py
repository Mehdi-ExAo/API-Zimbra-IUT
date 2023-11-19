class Semaine:
    def __init__(self, numSemaine, jours):
        self.numSemaine = numSemaine
        self.jours = jours
        
    def GetJour(numJour):
        return ""

    def GetJour(libele):
        return ""
        
    def GetAllJour():
        return self.jours
        
    def __str__(self):
        Affichage = f"Semaine : {self.numSemaine} \n"
        for jour in self.jours:
            Affichage+= str(jour)
        