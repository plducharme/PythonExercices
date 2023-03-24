class Noeud:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if not isinstance(self.data, str):
            return str(self.data)
        return self.data


class ListeChainee:
    """Permet de créer une liste chainée et de la manipuler

    Méthodes:
    -------
    ajout_fin(self, data)
    ajout_apres(self, cible_data, data)
    ajout_avant(self, cible_data, data)
    enlever_noeud(self, cible_data)

    """
    def __init__(self, noeuds=None):
        """
        Constructeur permettant d'instancier une liste Chainée
        :param noeuds: liste de Noeud optionels pour initialiser la liste

        """
        self.tete = None
        if noeuds is not None:
            noeud_courant = None
            for noeud in noeuds:
                if self.tete is None:
                    self.tete = noeud
                else:
                    noeud_courant.next = noeud
                noeud_courant = noeud

    def __repr__(self):
        noeuds = []
        noeud = self.tete

        while noeud is not None:
            data = noeud.data
            if not isinstance(data, str):
                data = str(data)
            noeuds.append(data)
            noeud = noeud.next
        noeuds.append('None')
        return ' -> '.join(noeuds)

    def __iter__(self):
        noeud = self.tete
        while noeud.next is not None:
            yield noeud
            noeud = noeud.next

    def ajout_fin(self, data):
        if self.tete is None:
            raise Exception('Liste Chainee vide')
        courant = self.tete
        for noeud in self:
            courant = noeud
        courant.next = Noeud(data)

    def ajout_apres(self, cible_data, data):
        if self.tete is None:
            raise Exception('Liste Chainee vide')

        for noeud in self:
            if noeud.data == cible_data:
                nouveau = Noeud(data)
                nouveau.next = noeud.next
                noeud.next = nouveau
                return

        raise Exception('Noeud ' + str(cible_data) + ' inexistant')

    def ajout_avant(self, cible_data, data):
        if self.tete is None:
            raise Exception('Liste Chainee vide')

        if self.tete.data == cible_data:
            nouveau = Noeud(data)
            nouveau.next = self.tete
            self.tete = nouveau
            return

        precedent = self.tete
        for noeud in self:
            if noeud.data == cible_data:
                nouveau = Noeud(data)
                precedent.next = nouveau
                nouveau.next = noeud
                return
            precedent = noeud

        raise Exception('Noeud ' + str(cible_data) + ' inexistant')

    def enlever_noeud(self, cible_data):
        if self.tete is None:
            raise Exception('Liste Chainee vide')

        if self.tete.data == cible_data:
            self.tete = self.tete.next
            return

        precedent = self.tete
        for noeud in self:
            if noeud.data == cible_data:
                precedent.next = noeud.next
                return
            precedent = noeud

        raise Exception('Noeud ' + str(cible_data) + ' inexistant')