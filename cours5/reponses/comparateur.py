class Book:

    def __init__(self, titre, nb_pages, prix):
        # Définir le constructeur
        self.__titre = titre
        self.__nb_pages = nb_pages
        self.__prix = prix

    # getters et setters
    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, titre):
        self.__titre = titre

    @property
    def nb_pages(self):
        return self.__nb_pages

    @nb_pages.setter
    def nb_pages(self, nb_pages):
        self.__nb_pages = nb_pages

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        self.__prix = prix


    # Coût par page
    def cout_par_page(self):
        return self.__prix/self.__nb_pages

    # Comparateur
    # __lt__ implémente l'opérateur '<' qui est utilisé par sort() et sorted()
    def __lt__(self, other):
        return self.cout_par_page() < other.cout_par_page()
    # Note: il y a une fonction pour chaque opérateur qui peut être implémenté
    # __le__ : less or equal (<=)
    # __gt__ : greater than (>)
    # __ge__ : greater equal (>=)
    # __eq__ : equal (==)
    # __ne__ : not equal (!=)
    # __and__ : boolean 'and'
    # __or__ : boolean 'or'
    # __add__ : addition (+)
    # __sub__ : soustraction (-)
    # et encore plus...

    # Fonction d'affichage
    # cet fonction est appelée par certaines fonctions builtin de python comme print(), son but est d'être lisible
    # doit retourner une string
    def __str__(self):
        return '{titre:\t' + self.__titre + '\tnb de pages:\t' + str(self.__nb_pages) + '\tprix:\t' \
            + str(self.prix) + '\tcout par page:\t' + str(self.cout_par_page()) + '}'

    # Cet fonction est appelée aussi pour l'affichage mais son but est d'être non ambigüe, si __str__ n'est pas
    # implémentée mais __repr__ l'est, __str__ == __repr__ par défaut. Dans notre cas, on va retourner __str__
    def __repr__(self):
        return self.__str__()

biblio = [Book('Python pour tous', 256, 10.99),
          Book('Structure de donnees pour le plaisir', 512, 12.95),
          Book('Le monde des comparateurs', 420, 18.99)]

# Sorted via key et lambda
liste = sorted(biblio, key=lambda x: x.cout_par_page())
for livre in liste:
    print(livre)
print('===========================')
# Sorted via __lt__
liste = sorted(biblio)
for livre in liste:
    print(livre)

