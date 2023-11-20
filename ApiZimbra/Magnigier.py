from Cours import Cours

class Magnifier:
    
    MagnifiedClass = {
      "TP R3.13 Communication ...": "TP R3.13 Communication professionnelle",
      "CM Besoin client, ..." : "CM Besoin client, Marketing 10",
      "TP  R3.05 programmation ..." : "TD R3.05 Programmation Systeme",
      "TP R3.05 programmation ..." : "TD R3.05 Programmation Systeme",
      "CM R3.10 Management des ..." : "CM R3.10 Management des Systèmes d'Information",
      "TP R3.07 SQL dans un ..." : "TP R3.07 SQL dans un Langage de Programmation",
      "TD R3.08 Probabilités ..." : "TD R3.08 Probabilités",
      "TP R3.04 Qualité de ..." : "TP R3.04 Qualité de Développement",
      "TP R3.08 Probabilités ..." : "TP R3.08 Probabilités",
      "CM R3.01 Développement ..." : "CM R3.01 Développement Web",
      "CM R3.11 Droit des ..." : "CM R3.11 Droit des Contrats et du Numérique",
      "CM R3.07 SQL dans un .." : "CM R3.07 SQL dans un Langage de Programmation",
      "TD R3.10 Management des ..." : "TD R3.10 Management des Systèmes d'Information",
      "TD R3.09 Cryptographie ..." : "TD R3.09 Cryptographie et Sécurité",
      "CM R3.04 Qualité de ..." : "CM R3.04 Qualité de Développement",
      "SAE 3 TD Besoin client ..." : "SAE 3 TD Besoin client Enjeux Marketing",
      "SAE 3 B TD Faire une ..." : "SAE 3 B TD Faire une formation en anglais",
      "TD R3.11 Droit des ..." : "TD R3.11 Droit des Contrats et du Numérique",
    }
    
    @staticmethod
    def Magnify(cour):
        if cour.sujet in Magnifier.MagnifiedClass:
            cour.sujet = Magnifier.MagnifiedClass[cour.sujet]
            
        return cour
    
    @classmethod
    def AddToMagnifiedClass(cls, original, magnified):
        cls.MagnifiedClass[original] = magnified