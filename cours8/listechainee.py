class Noeud:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class ListeChainee:

    def __init__(self, noeuds=None):
        self.tete = None

    def __repr__(self):
        pass