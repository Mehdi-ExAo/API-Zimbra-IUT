class Calendrier:
    def __init__(self, semaines):
        self.semaines = semaines
        
    def GetSemaine(self, numSemaine):
        return self.semaines[numSemaine]
    
    def GetAllSemaines(self):
        return self.semaines
    
    def __str__(self):
        Afficher = "Calendrier :"
        for semaine in self.semaines:
            Afficher+= str(semaine)
        