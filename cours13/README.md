# JSON
- Créer la classe représentant une auto basée sur le fichier cars.json (https://github.com/vega/vega/blob/main/docs/data/cars.json)
- Lire le fichier cars.json pour retourner la liste d'autos et créer les objets correspondants
- Trier les autos en ordre croissant de consommation (Miles_per_Gallon) en utilisant un tri par insertion
- Écrire la liste triée dans le fichier autos.json

# CSV
- Créer une classe représentant le plan d'immigration du Québec 2023
- Lire le fichier plan_immigration_quebec_2023.csv (https://www.donneesquebec.ca/recherche/dataset/plan-d-immigration-du-quebec-2023/resource/8c2212c3-4917-4aa4-b395-9371cf8573ea)
- Créer la liste d'objets de la classe
- Sauvegarder une copie de cette liste dans un fichier gzip
- Effacer la liste d'objets de la classe
- Lire la copie de la liste et recréer la liste
- Recréer le fichier original sous un nom différent
- Comparer les deux fichiers
  - Peut être fait programmatiquement en lisant les deux fichiers
  - Possible de copier le contenu d'un fichier dans le presse-papier et le comparer dans PyCharm

# XML
## DOM
- Utiliser xml.dom.minidom pour lire le fichier offre-emploi.xml (https://www.donneesquebec.ca/recherche/dataset/offres-d-emploi/resource/82280f10-a8d4-4714-91d2-11f32a2be220)
- Utiliser getElementsByTagName pour aller chercher la liste de OffresEmploi dans le document
- Créer une classe OffresEmploi
- Pour chaque élément de la liste, créer l'objet de la classe OffresEmploi
## SAX
- Utiliser xml.sax pour implémenter un Handler dérivant de xml.sax.ContentHandler
- Lire le fichier offre-emploi.xml
- Afficher à la console le nom de l'élément traversé et son contenu
## Etree
- Utiliser xml.etree.ElementTree pour créer un nouveau fichier xml (offres.xml)
- Réutiliser le code du DOM parser pour lire le fichier offre-emploi.xml et créer la collection de OffresEmploi
- Recréer dans le fichier offres.xml le format original de offre-emploi.xml à partir de votre liste d'objets OffresEmploi
- Comparer les fichiers

