import math
import time
from abc import ABC, abstractmethod
from developeur import Developeur
from station_comptage import *


class Tri(ABC):

    @abstractmethod
    def trier(self, tableau):
        pass


class TriInsertion(Tri):

    def trier(self, tableau):
        for i in range(1, len(tableau)):
            courant = tableau[i]
            p = i
            while p > 0 and tableau[p - 1] > courant:
                tableau[p] = tableau[p - 1]
                p = p - 1
            tableau[p] = courant


class TriSelection(Tri):

    def trier(self, tableau):
        for i in range(0, len(tableau)):

            minimum = tableau[i]
            min_index = i

            # itérer sur le reste du tableau pour chercher la plus petite valeur
            for j in range(i, len(tableau)):

                if tableau[j] < minimum:
                    minimum = tableau[j]
                    min_index = j

            # échanger l'élément à l'index i avec le minimum trouvé
            temp = tableau[i]
            tableau[i] = tableau[min_index]
            tableau[min_index] = temp


class TriFusion(Tri):

    def trier(self, tableau):
        # diviser le tableau en sous-tableau
        longueur = len(tableau)
        # Si la longueur est 1, on ne peut plus diviser le tableau
        if longueur < 2:
            return
        # trouver le milieu pour diviser (plancher de la division)
        milieu = math.floor(longueur / 2)  # équivalent à "longueur // 2"
        tableau_gauche = tableau[0:milieu]
        tableau_droite = tableau[milieu:longueur]
        # Appelle récursivement pour continuer à diviser puis fusionner
        self.trier(tableau_gauche)
        self.trier(tableau_droite)
        self.fusion(tableau_gauche, tableau_droite, tableau)

    @staticmethod
    def fusion(tableau_gauche, tableau_droite, tableau):
        longueur_gauche = len(tableau_gauche)
        longueur_droite = len(tableau_droite)
        i, j, k = 0, 0, 0
        # fusionner en triant les deux petits tableaux
        while i < longueur_gauche and j < longueur_droite:
            if tableau_gauche[i] <= tableau_droite[j]:
                tableau[k] = tableau_gauche[i]
                i += 1
            else:
                tableau[k] = tableau_droite[j]
                j += 1
            k += 1
        # Ajouter les éléments restants dans une des deux listes
        while i < longueur_gauche:
            tableau[k] = tableau_gauche[i]
            i += 1
            k += 1
        while j < longueur_droite:
            tableau[k] = tableau_droite[j]
            j += 1
            k += 1


class TriBulles(Tri):

    def trier(self, tableau):
        for i in range(0, len(tableau) - 1):
            deja_trie = True
            # parcours les éléments de gauche à droite et les échanges au besoin
            for j in range(0, len(tableau) - 1 - i):
                if tableau[j + 1] < tableau[j]:
                    temp = tableau[j]
                    tableau[j] = tableau[j + 1]
                    tableau[j + 1] = temp
                    deja_trie = False
            # on a fait une passe complète sans changer d'éléments, le tableau est déjà trié
            if deja_trie is True:
                return


class TriRapide(Tri):

    def trier(self, tableau):
        self.tri_rapide(tableau, 0, len(tableau))

    def tri_rapide(self, tableau, debut, fin):
        if debut >= fin:
            return
        pivot = self.partition(tableau, debut, fin - 1)
        self.tri_rapide(tableau, debut, pivot)
        self.tri_rapide(tableau, pivot + 1, fin)

    @staticmethod
    def partition(tableau, debut, fin):
        pivot = tableau[fin]
        index = debut
        for i in range(debut, fin):
            if tableau[i] <= pivot:
                temp = tableau[i]
                tableau[i] = tableau[index]
                tableau[index] = temp
                index += 1
        temp = tableau[index]
        tableau[index] = pivot
        tableau[fin] = temp
        return index


tris = [TriInsertion(), TriSelection(), TriFusion(), TriBulles(), TriRapide()]

for tri in tris:
    devs = Developeur.generate_devs(15)
    out = ''
    for dev in devs:
        out += repr(dev)
    print('Initial: [ ' + out + ' ]')
    print('Tri' + str(tri.__class__))
    debut = time.time_ns()
    tri.trier(devs)
    temps = (time.time_ns() - debut) / 1000000000
    out = ''
    for dev in devs:
        out += repr(dev)
    print('Resultat: [ ' + out + ' ]')
    print(f'Tri effectue en {temps:1f}s\n==============================')


for tri in tris:
    stations = StationComptage.from_csv()
    for k, v in stations.items():
        print('Station:\t' + k)
        print('Tri:\t' + str(tri.__class__) + ' sur ' + str(len(v.comptage)) + ' elements')
        debut = time.time_ns()
        tri.trier(v.comptage)
        temps = (time.time_ns() - debut) / 1000000000
        moyenne = temps / len(v.comptage)
        print(f'Tri effectue en {temps:1f}s\tmoyenne: {moyenne:1f}/element\n========================')








