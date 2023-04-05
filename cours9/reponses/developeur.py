import random


class Developeur:

    def __init__(self, prenom, nom, salaire):
        self.__prenom = prenom
        self.__nom = nom
        self.__salaire = salaire

    def __repr__(self):
        return '{Nom: ' + self.__nom + '\tPrenom: ' + self.__prenom + '\tSalaire: ' + str(self.__salaire) + '}\t'

    def __lt__(self, other):
        return self.__salaire < other.salaire

    def __le__(self, other):
        return self.__salaire <= other.salaire

    def __gt__(self, other):
        return self.__salaire > other.salaire

    # Getters, dans ce cas ci, les setters ne sont pas utilisés, mais il est bien de les implémenter
    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, prenom):
        self.__prenom = prenom

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def salaire(self):
        return self.__salaire

    @salaire.setter
    def salaire(self, salaire):
        self.__salaire = salaire

    @classmethod
    def generate_devs(cls, nombre):
        devs = []
        noms = ('Martin', 'Bernard', 'Petit', 'Pujol', 'Jimenez', 'Cabrera', 'Lamine', 'Stewart', 'Doe')
        prenoms = ('Jean', 'Jeanne', 'Sarah', 'Paul', 'Lina', 'Armand', 'Mohamed', 'Seifeddine', 'Hossam', 'Xiaofan')
        for i in range(0, nombre):
            devs.append(cls(prenoms[random.randint(0, len(prenoms) - 1)], noms[random.randint(0, len(noms) - 1)],
                            random.randint(55000, 97000)))
        return devs


