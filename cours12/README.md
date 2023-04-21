# Exercices 

## Sérialisation/Désérialisation
1) Créer une classe Inventaire dans inventaire.py
   1) Un inventaire associe un numéro de produit à une quantité disponible et à une date à laquelle il a été mis-à-jour
2) Créer une méthode qui génère 50 objets Inventaire
   1) Il ne peut y avoir de doublon de produits
      1) Le numéro de produit doit être entre 1 et 50  
   2) la quantité devrait se situer entre 1 et 15
   3) la date devrait être celle courante (datetime)
3) Créer une méthode pour sérialiser les objets dans leur fichier individuel
4) Créer une méthode pour désérialiser les objets à partir de leur fichier individuel
5) Créer une méthode qui sérialise la liste d'objets dans un fichier
6) Créer une méthode qui désérialise la liste d'objets
7) Créer une méthode pour mettre à jour sur disque un objet sérialisé


## Création d'un service de cache de base
Les caches ont généralement certaines caractéristiques :
- Une taille maximale d'entrées
- Un âge maximal pour rester dans la cache
- Une taille maximale en espace

Dans cache.py:
1) Créer une classe CacheServer
2) Créer une méthode get_objet(self, key) qui retourne l'objet en cache
3) Créer une méthode has_objet(self, key) qui vérifie si l'objet existe
4) Créer une méthode del_objet(self, key) qui enlève l'objet du cache
5) Créer une méthode replace_objet(self, obj) qui remplace l'objet dans la cache
6) Créer une méthode add_objet(self, obj)

Dans cached_serveur.py:
1) Importer les modules cache et inventaire
2) Créer un constructeur qui initialise le cache et l'inventaire sur disque
   1) On va faire une cache à la demande, on va mettre en cache seulement les objets demandés
3) Créer une méthode pour aller chercher un objet
   1) On regarde d'abord dans la cache si l'objet y est
      1) S'il y est, on le retourne
      2) Sinon, on va le désérialiser, l'ajouter à la cache et le retourner
4) En gardant le compte de temps, écrire un jeu de tests pour aller chercher des objets qui sont dans la cache et des objets qui ne sont pas dans la cache
5) Si le temps le permet:
   1) Mettre à jour les objets sérialisés et mettre à jour la cache
   2) Ajouter la fonctionnalité qui limite le nombre d'entrées dans la cache
   3) Ajouter la fonctionnalité qui limite la taille de la cache
   4) Ajouter la fonctionnalité qui limite l'âge des objets en cache

