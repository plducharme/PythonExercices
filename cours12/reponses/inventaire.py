import os
import pickle
import random
import datetime


class Inventaire:
    def __init__(self, no_produit, qte, maj):
        self.__no_produit = no_produit
        self.__qte = qte
        self.__maj = maj

    @property
    def no_produit(self):
        return self.__no_produit

    @property
    def qte(self):
        return self.__qte

    @property
    def maj(self):
        return self.__maj

    @staticmethod
    def generer_inventaire(nombre):
        inventaires = []
        for i in range(0, nombre):
            inventaires.append(Inventaire(i+1, random.randint(1, 15), datetime.datetime.now()))
        return inventaires

    @staticmethod
    def serialiser(objet):
       with open('./tmp/' + str(objet.no_produit) + '.pickle', 'wb') as pickle_out:
           pickle.dump(objet, pickle_out)

    @staticmethod
    def serialiser_objets(liste):
        for obj in liste:
            Inventaire.serialiser(obj)

    @staticmethod
    def serialiser_liste(liste):
        with open('./tmp/liste.pickle', 'wb') as pickle_out:
            pickle.dump(liste, pickle_out)

    @staticmethod
    def deserialiser(filename):
        with open('./tmp/'+filename, 'rb') as pickle_in:
            obj = pickle.load(pickle_in)
        return obj

    @staticmethod
    def deserialiser_liste(filename):
        with open('./tmp/liste.pickle', 'rb') as pickle_in:
            obj = pickle.load(pickle_in)
        return obj

    @staticmethod
    def deserialiser_tous():
        fichiers = os.listdir('./tmp')
        liste = []
        for fichier in fichiers:
            if not fichier.startswith('liste'):
                with open('./tmp/'+fichier, 'rb') as pickle_in:
                    liste.append(pickle.load(pickle_in))
        return liste


inventaires = Inventaire.generer_inventaire(50)
Inventaire.serialiser_objets(inventaires)
Inventaire.serialiser_liste(inventaires)

nouvelle_liste = Inventaire.deserialiser_liste('liste.pickle')
liste_objets = Inventaire.deserialiser_tous()

print(nouvelle_liste)
