#Récupérer les informations
import requests
from bs4 import BeautifulSoup
import csv
#Constante
my_url="https://www.gouv.bj/destination-benin/"
BASE_URL="https://www.gouv.bj/"


page=requests.get(my_url)
soup=BeautifulSoup(page.text,"html.parser")
datas=[]

#print(soup.find('h1'))
#print(soup.title.text)
#print(soup.select('h2,h3,p'))
#Je recupere le premier bloc de la ville
tmp=soup.find('div',class_='town')
#Get div parent
blocs_communes=tmp.parent
#Get tous les divs dont la classe est town
bloc_towns=blocs_communes.find_all('div',class_="town")
#Je get les noms des villes
print(blocs_communes.find_all('div',class_="town")[3].span()[0].text)
#Avoir la liste de toutes les villes
town_names=[town_div.span()[0].text for town_div in bloc_towns]

town_description=[town_div.find_all('span')[3].text for town_div in bloc_towns]

town_url=[town_div.find('a').attrs['href'] for town_div in bloc_towns]

town_picture=[town_div.find('image').attrs['href'] for town_div in bloc_towns]

#Transformer ça dans un structure de données
for name,desc,url,img in zip(town_names,town_description,town_url,town_picture):
    datas.append({
        "name":name,
        "description":desc,
        "url":BASE_URL+url ,
        "image":BASE_URL+img
    
    })
print(datas)


#Save in csv file
# Créer une liste pour les en-têtes
en_tete = datas[0].keys()

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w',encoding='utf-8') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(en_tete)
   # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
   for obj in datas:
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [obj.get('name'),obj.get('description'),obj.get('url'),obj.get('image')]
      writer.writerow(ligne)