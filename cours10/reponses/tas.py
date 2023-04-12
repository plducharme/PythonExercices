class Tas:

    def __init__(self, tableau):
        self.__tableau = tableau

    @property
    def tableau(self):
        return self.__tableau

    @tableau.setter
    def tableau(self, tableau):
        self.__tableau = tableau

    def creer_tas(self):

        # trouve l'index du dernier pere
        index_dernier_pere = len(self.__tableau) // 2 - 1

        # On commence par le dernier pere insere et on tasse les peres de droite a gauche et de bas en haut
        for i in range(index_dernier_pere, -1, -1):
            self.tamisage_min(i)

    def tamisage_min(self, index):
        index_min = index
        index_fils_gauche = 2 * index + 1
        index_fils_droit = 2 * index + 2

        # Compare le pere avec le fils gauche pour determine si un des fils est plus petit
        if index_fils_gauche < len(self.__tableau) and self.__tableau[index_fils_gauche] < self.__tableau[index]:
            index_min = index_fils_gauche
        if index_fils_droit < len(self.__tableau) and self.__tableau[index_fils_droit] < self.__tableau[index_min]:
            index_min = index_fils_droit
        if index_min != index:
            # On a trouve le plus petit fils, plus petit que le pere. On les permute
            self.__tableau[index], self.__tableau[index_min] = self.__tableau[index_min], self.__tableau[index]
            self.tamisage_min(index_min)

    def enlever(self):
        racine = self.__tableau[0]
        dernier_element = self.__tableau.pop(len(self.__tableau)-1)
        self.__tableau[0] = dernier_element
        self.tamisage_min(0)
        return racine

    def ajouter(self, item):
        self.__tableau.append(item)
        self.creer_tas()

    def remplacer(self, item):
        racine = self.__tableau[0]
        self.__tableau[0] = item
        self.tamisage_min(0)
        return racine




liste = [56, 24, 28, 13, 34, 12, 3, 19, 42]

tas = Tas(liste)
tas.creer_tas()

print(tas.tableau)
tas.enlever()
print(tas.tableau)
tas.ajouter(15)
print(tas.tableau)
tas.remplacer(72)
print(tas.tableau)