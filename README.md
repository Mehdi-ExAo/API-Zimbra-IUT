# API Zimbra (IUT Dijon)

## À propos
Ce script Python permet de récupérer (pour l'instant) uniquement le calendrier Zimbra. Grâce à ce dernier, on peut avoir une liste des cours d'une journée à partir de la date. On peut alors éviter de devoir ouvrir Zimbra toutes les 15 minutes parce qu'on est trop tête en l'air pour retenir quelques matières, numéro de salle ou encore ses horaires.

En-tout-cas grâce à de la sorcellerie et beaucoup de temps, vous pourrez grâce à cette API vous faire plaisir et faire par exemple un bot discord qui pourrais vous envoyer un message pour vous prévenir des cours à venir.

Vous vous demandez sûrement pourquoi du Python ? Je n'en ai aucune idée...

## Prérequis
- Python 3.x
- Bibliothèque `requests` (à installer avec `pip install requests`)
- Bibliothèque `BeautifulSoup` (à installer avec `pip install beautifulsoup4`)

## Exemple
```python
from Connexion import Connexion
from Cours import Cours
from Jour import Jour

#Identifiants Zimbra
login = "votre_nom_utilisateur"
mdp = "votre_mot_de_passe"
email = "exemple@iut-dijon.u-bourgogne.fr"

date = "20231123" #Pour 23/11/2023

connexion = Connexion(login, mdp, email)

# Depuis la connexion, on récupère un objet de type Jour depuis lequel on récupère tous les cours
liste_cours = connexion.getJour(date).GetCours()

# Pour tous nos cours dans notre liste, on affiche notre cour
for cours in liste_cours:
    print(str(cours))

```
Résultat :
![alt text](https://i.imgur.com/6qSyWuE.png)

## Informations
![alt text](https://i.imgur.com/JWq9e1d.png)

Voici le diagramme des classes, on y retrouve 4 classes.

- La première classe et le plus important, celle de la **Connexion**. C'est grâce à elle que l'on peut récupérer les cours depuis Zimbra. Elle prend en entrée un login, un mot de passe et une adresse email. Attention, je risque de vous choquer, il s'agit de vos identifiants Zimbra ! Le JsessionID et le AuthToken font partie des cookies nécessaires à la connexion. Bref, ils sont là si besoin. Au moment de getJour, vous aurez en retour un objet Jour. Pour le getJour, le paramètre date est comme suit : 20231123 pour le 23/11/2023.

- Dans un second temps, on retrouve la classe **Jour**, cette dernière garde en mémoire une liste de Cours. À laquelle on peut accéder avec la méthode getCours. Nous pouvons également récupérer un cours grâce à l'heure sous forme de string : "08h00" par exemple, vous retourneront, s'il y en a un, le cours de 8h00. Cette classe n'a peut-être pas de réel sens pour vous, mais le but initial de cet Api était de récupérer un mois entier, qui lui contiendrait des semaines... Je pense que vous avez compris.

- Vous retrouverez également la classe **Cours**, qui elle constitue un cours, on peut y récupérer l'emplacement du cours (salle), le sujet/matière et enfin l'heure du cour.

- Enfin, la classe **Magnifier** sert simplement à formater le nom des matières. En effet, une fois récupérer le nom des matières n'est pas complet. Vous pourrez donc en ajouter grâce à l'opération AddToMagnifiedClass. Tout cela afin d'avoir le nom des matières parfaitement affiché et/ou renommer les matières à votre guise.

Si tu as des questions, des recommandations ou des proposition n'hésite pas à me contacter.

## Crédits
- Aide :
    - [Maxime](https://github.com/MaximeLAFFAYE)
    - [Jeremie](https://github.com/JeremieVIEIRA)


- Idée : 
    - [API-OGE](https://github.com/Nicooow/API-OGE)


