class GraphListe:

    def __init__(self):
        self.__liste = {}

    # ajout d'une arête
    def ajout_arete(self, origine, destination, poids):
        if origine in self.__liste:
            self.__liste[origine].append((destination, poids))
        else:
            self.__liste[origine] = [(destination, poids)]
        if destination not in self.__liste:
            self.__liste[destination] = []

    # Retourne True si un chemin existe entre les deux sommets
    def is_path(self, origine, destination, visite=[]):
        for s in self.__liste[origine]:
            d, p = s
            if d == destination:
                return True
        if origine in visite:
            return False
        else:
            visite.append(origine)

        for s in self.__liste[origine]:
            d, p = s
            if self.is_path(d, destination, visite):
                return True
        return False

    # Retourne le coût du chemin, -1 si le chemin n'existe pas
    def path_cost(self, origine, destination, visite=[]):
        total = 0
        for s in self.__liste[origine]:
            d, p = s
            if d == destination:
                total += p
                return total
        if origine in visite:
            return -1
        else:
            visite.append(origine)

        for s in self.__liste[origine]:
            d, p = s
            cout = self.path_cost(d, destination, visite)
            if cout > 0:
                total += cout + p
                return total
        return -1

    def has_cycle(self, sommet):
        return self.is_path(sommet, sommet, [])


g = GraphListe()
g.ajout_arete(0, 1, 5)
g.ajout_arete(0, 2, 4)
g.ajout_arete(0, 3, 6)
g.ajout_arete(1, 4, 3)
g.ajout_arete(2, 3, 2)
g.ajout_arete(3, 4, 4)
g.ajout_arete(4, 0, 7)
g.ajout_arete(4, 5, 1)

print(g.is_path(0, 3, []))
print(g.is_path(0, 4, []))
print(g.is_path(5, 0, []))

print(str(g.path_cost(0, 3, [])))
print(str(g.path_cost(0, 4, [])))
print(str(g.path_cost(5, 0, [])))
print(str(g.path_cost(1, 2, [])))

print(g.has_cycle(0))
print(g.has_cycle(3))
print(g.has_cycle(5))