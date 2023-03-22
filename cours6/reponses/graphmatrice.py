class Graph:

    def __init__(self):
        self.__matrice = []

    # ajout d'une arête
    def ajout_arete(self, ligne):
        self.__matrice.append(ligne)

    # Retourne True si un chemin existe entre les deux sommets
    def is_path(self, origine, destination, visite=[]):
        if self.__matrice[origine][destination] > 0:
            return True
        if origine in visite:
            return False
        else:
            visite.append(origine)

        for d in self.__matrice[origine]:
            if d > 0 and self.is_path(self.__matrice[origine].index(d), destination, visite):
                return True
        return False

    # Retourne le coût du chemin, -1 si le chemin n'existe pas
    def path_cost(self, origine, destination, visite=[]):
        total = 0
        if self.__matrice[origine][destination] > 0:
            total += self.__matrice[origine][destination]
            return total
        if origine in visite:
            return -1
        else:
            visite.append(origine)

        for d in self.__matrice[origine]:
            if d > 0:
                cout = self.path_cost(self.__matrice[origine].index(d), destination, visite)
                if cout > 0:
                    total += cout + d
                    return total
        return -1

    def has_cycle(self, sommet):
        return self.is_path(sommet, sommet, [])

g = Graph()
g.ajout_arete([0, 5, 4, 6, 0, 0])
g.ajout_arete([0, 0, 0, 0, 3, 0])
g.ajout_arete([0, 0, 0, 2, 0, 0])
g.ajout_arete([0, 0, 0, 0, 4, 0])
g.ajout_arete([7, 0, 0, 0, 0, 9])
g.ajout_arete([0, 0, 0, 0, 0, 0])

print(g.is_path(0, 3, []))
print(g.is_path(0, 4, []))
print(g.is_path(5, 0, []))

print(str(g.path_cost(0, 3)))
print(str(g.path_cost(0, 4, [])))
print(str(g.path_cost(5, 0, [])))
print(str(g.path_cost(1, 2, [])))

print(g.has_cycle(0))
print(g.has_cycle(3))
print(g.has_cycle(5))

