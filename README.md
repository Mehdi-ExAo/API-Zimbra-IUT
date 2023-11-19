# Scraper Calendrier Zimbra (IUT Dijon)

## Aperçu
Ce script Python offre des fonctionnalités pour extraire les informations du calendrier à partir de l'interface web Zimbra de l'IUT Dijon de l'Université de Bourgogne. Il utilise la bibliothèque `requests` pour les requêtes HTTP et `BeautifulSoup` pour l'analyse HTML.

## Prérequis
- Python 3.x
- Bibliothèque `requests` (à installer avec `pip install requests`)
- Bibliothèque `BeautifulSoup` (à installer avec `pip install beautifulsoup4`)

# Documentation

## Récupération du JsessionID
Le getJsessionID prend en charge l'authentification. Elle utilise les identifiants fournis pour établir une session et retourne la valeur du cookie JSESSIONID, essentiel pour les requêtes.
```python
login = "votre_nom_utilisateur"
mdp = "votre_mot_de_passe"

JSESSIONID = getJsessionID(login, mdp)
```

## Récupération du AuthToken
Le getAuthToken obtient le token d'authentification ZM_AUTH_TOKEN nécessaire pour accéder à Zimbra. Elle utilise les identifiants pour récupérer ce token, qui peut être utiliser.
```python
login = "votre_nom_utilisateur"
mdp = "votre_mot_de_passe"

ZM_AUTH_TOKEN = getAuthToken(login, mdp)
```

## Récupération des Cours
Le getCalendar utilise les fonctions précédentes pour récupérer les horaires de cours depuis le calendrier Zimbra. Elle retourne une liste d'objets Cours représentant les informations sur chaque cours, y compris le lieu, le sujet, l'heure et le jour.
```python
login = "votre_nom_utilisateur"
mdp = "votre_mot_de_passe"

liste_cours = getCalendar(login, mdp)

for cours in liste_cours:
    print(cours)
```
![alt text](https://i.imgur.com/ewmWJwD.png)
