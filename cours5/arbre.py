# Créer un arbre qui permet d'insérer une chaine de caractères
# Vous pouvez modifier comme bon vous semble

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
        pass

    def imprimer_mots(self, string):
        pass


racine = Noeud('*')
racine.ajout_mot('test')
racine.ajout_mot('parapluie')
racine.ajout_mot('paratonnerre')
racine.imprimer_mots('')


