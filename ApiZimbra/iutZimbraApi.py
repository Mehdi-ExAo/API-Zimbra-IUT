import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

login_url = "https://iut-dijon.u-bourgogne.fr/zimbra/?loginOp=login"
main_url = "https://iut-dijon.u-bourgogne.fr/zimbra/m/zmain"
zimbra_server = 'https://iut-dijon.u-bourgogne.fr'
email_address = 'el-mehdi.bouabdalli@iut-dijon.u-bourgogne.fr'


class Cours:
    def __init__(self, emplacement, sujet, heure, jour):
        self.emplacement = emplacement
        self.sujet = sujet
        self.heure = heure
        self.jour = jour

    def __str__(self):
        return f"{self.jour} {self.heure} {self.sujet} {self.emplacement}"
    
def getJsessionID(login, mdp):
    login_data = {
            "loginOp": "login",
            "login_csrf": "bef4b61b-610a-420b-a00a-b0f062a5f558",
            "username": login,
            "password": mdp,
            "client": "preferred"
        }
    
    login_response = requests.post(login_url, data=login_data)
    main_response = requests.get(main_url, cookies=login_response.cookies)
    jsessionid = main_response.cookies.get('JSESSIONID')
    
    return jsessionid
    

def getAuthToken(login, mdp):
    url = f'{zimbra_server}/home/{email_address}/Inbox/?fmt=sync&auth=sc'
    response = requests.get(url, auth=(login, mdp), cookies={}, allow_redirects=False)
    return response.cookies.get('ZM_AUTH_TOKEN')

def getCalendar(login, mdp):
    jsessionid_main = getJsessionID(login, mdp)
    
    zm_auth_token = getAuthToken(login, mdp)
    
    url = f'{zimbra_server}/zimbra/m/zmain;jsessionid={jsessionid_main}?ajax=true&st=cal'
    
    response = requests.get(url, auth=(login, mdp), cookies={'JSESSIONID': jsessionid_main, 'ZM_TEST': 'true','ZM_AUTH_TOKEN': zm_auth_token}, allow_redirects=False)
    pageweb = response.text
    
    soup = BeautifulSoup(pageweb, 'html.parser')
    
    tab = []
    
    zh_app_content_elements = soup.find_all(class_='zo_cal_listi')
    
    liste_cours = []
    
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    heure_cours_precedent = datetime.strptime("00:00", "%H:%M").time()
    
    index_jour_actuel = 0
    
    for element in soup.find_all(class_='zo_cal_listi'):
        heure_cours_str = element.find(class_='zo_cal_listi_time').text.strip()
        sujet_cours = element.find(class_='zo_cal_listi_subject').text.strip()
        emplacement_cours = element.find(class_='zo_cal_listi_location').text.strip()
    
        heure_cours = datetime.strptime(heure_cours_str, '%H:%M').time()
    
        if heure_cours < heure_cours_precedent: 
            index_jour_actuel += 1
    
        if index_jour_actuel == 5:
            index_jour_actuel = 0
    
    
        jour_cours = jours_semaine[index_jour_actuel]
        
        heure_cours_precedent = heure_cours
    
        info_cours = Cours(emplacement_cours, sujet_cours, heure_cours, jour_cours)
    
        liste_cours.append(info_cours)
    
    return liste_cours



                
