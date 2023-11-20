import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from Cours import Cours
from Jour import Jour

class Connexion:    
    def __init__(self, login, password, mailAdress):
        self.login_url = "https://iut-dijon.u-bourgogne.fr/zimbra/?loginOp=login"
        self.main_url = "https://iut-dijon.u-bourgogne.fr/zimbra/m/zmain"
        self.zimbra_server = 'https://iut-dijon.u-bourgogne.fr'
        self.email_address = mailAdress
        self.login= login
        self.password = password
        self.url = f'{self.zimbra_server}/home/{self.email_address}/Inbox/?fmt=sync&auth=sc'


    def getJsessionID(self):
        login_data = {
                "loginOp": "login",
                "login_csrf": "bef4b61b-610a-420b-a00a-b0f062a5f558",
                "username": self.login,
                "password": self.password,
                "client": "preferred"
            }
        login_response = requests.post(self.login_url, data=login_data)
        main_response = requests.get(self.main_url, cookies=login_response.cookies)
        return main_response.cookies.get('JSESSIONID')
    
    
    def getAuthToken(self):
        response = requests.get(self.url, auth=(self.login, self.password), cookies={}, allow_redirects=False)
        return response.cookies.get('ZM_AUTH_TOKEN')

    def getCalendar(self):
        jsessionid_main = self.getJsessionID()
        zm_auth_token = self.getAuthToken()
        
        calendar_url = f'{self.zimbra_server}/zimbra/m/zmain;jsessionid={jsessionid_main}?ajax=true&st=cal'

        response = requests.get(calendar_url, auth=(self.login, self.password), cookies={'JSESSIONID': jsessionid_main, 'ZM_TEST': 'true','ZM_AUTH_TOKEN': zm_auth_token}, allow_redirects=False)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        zh_app_content_elements = soup.find_all('div', class_='zo_cal_mlist')
        
        
        liste_cours = []
        caledrier = []
        
        jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
        
        index_jour_actuel = 0
        
        
        for day in zh_app_content_elements:
            if index_jour_actuel == 5:
                index_jour_actuel = 0
            
            liste_cours = []
                
            events = day.find_all('div', class_='zo_cal_listi')
                
            
            for element in events:
                heure_cours_str = element.find(class_='zo_cal_listi_time').text.strip()
                sujet_cours = element.find(class_='zo_cal_listi_subject').text.strip()
                emplacement_cours = element.find(class_='zo_cal_listi_location').text.strip()
            
                liste_cours.append(Cours(emplacement_cours, sujet_cours, heure_cours_str)) 


            jour = Jour(liste_cours, jours_semaine[index_jour_actuel], index_jour_actuel)
            caledrier.append(jour)
            index_jour_actuel += 1

        return caledrier
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

