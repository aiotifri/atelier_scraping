import csv 
import requests
from bs4 import BeautifulSoup
datas=[]
url="https://www.gouv.bj/destination-benin/"
BASE_URL="https://www.gouv.bj"
page=requests.get(url)
print(type(page.text))
soup=BeautifulSoup(page.text,"html.parser")
blocs_town=soup.find_all("div",class_="town")

name_town=[town.span()[0].text for town in blocs_town ]
desc_town=[town.find_all('span')[3].text for town in blocs_town]
pic_town=[BASE_URL+town.find('image').attrs['href'] for town in blocs_town]
url_town=[BASE_URL+town.find('a').attrs['href'] for town in blocs_town]

for name,desc,img,url in zip(name_town,desc_town,pic_town,url_town):
    datas.append(
        {
            "name":name,
            "desc":desc,
            "img":img,
            "url":url
        }
    )   

print(datas)

#Save in csv file
# Créer une liste pour les en-têtes
en_tete = datas[0].keys()

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('communebenin.csv', 'w',encoding='utf-8') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(en_tete)
   # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
   for obj in datas:
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [obj['name'],obj['desc'],obj['url'],obj['img']]
      writer.writerow(ligne)

