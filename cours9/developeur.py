import random


class Developeur:

    def __init__(self, prenom, nom, salaire):
        self.__prenom = prenom
        self.__nom = nom
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


