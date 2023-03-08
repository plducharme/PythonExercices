# Créer un arbre qui permet d'inserer une chaine de caracteres

class Noeud:

    def __init__(self, data):
        self.__data = data
        self.__enfants = []

    @property
    def data(self):
        return self.__data

    @property
    def enfants(self):
        return self.__enfants

    def ajout_noeud(self, noeud):
        pass

    def ajout_mot(self, mot):
        lettre = mot[0]
        if len(mot) == 1:
            mot = '*'
        else:
            mot = mot[1:]
        if lettre == '*':
            self.__enfants.append(Noeud('*'))
            return
        found = False
        for enfant in self.__enfants:
            if lettre == enfant.data:
                enfant.ajout_mot(mot)
                found = True
        if found is False:
            enfant = Noeud(lettre)
            self.__enfants.append(enfant)
            enfant.ajout_mot(mot)

    def imprimer_mots(self, string):
        lettre = self.data
        string += lettre
        if lettre == '*' and len(string) > 1:
            print('Found:\t' + string[1:len(string)-1])
            return
        for enfant in self.__enfants:
            enfant.imprimer_mots(string)

racine = Noeud('*')
racine.ajout_mot('test')
racine.ajout_mot('parapluie')
racine.ajout_mot('paratonnerre')
racine.imprimer_mots('')


