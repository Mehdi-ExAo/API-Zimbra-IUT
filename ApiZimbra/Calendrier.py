class Calendrier:
    def __init__(self, semaines):
        self.semains = semaines
        
    def GetSemaine(numSemaine):
        return self.semaines[numSemaine]
    
    def GetAllSemaines():
        return self.semaines
    
    def __str__(self):
        Afficher = "Calendrier :"
        for semaine in self.semaines:
            Afficher+= str(semaine)
        