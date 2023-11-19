class Magnifier:
    
    MagnifiedClass = {
      "Communication ...": "Communication professionnelle",
    }
    
    @staticmethod
    def Magnify(cour):
        if cour.sujet in Magnifier.MagnifiedClass:
            cour.contenu = Magnifier.MagnifiedClass[cour.sujet]
        return cour
    
    
    