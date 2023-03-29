from abc import ABC, abstractmethod
from developeur import Developeur


class Tri(ABC):

    @abstractmethod
    def trier(self, tableau):
        pass


class TriInsertion(Tri):

    def trier(self, tableau):
        pass


class TriSelection(Tri):

    def trier(self, tableau):
        pass


class TriFusion(Tri):

    def trier(self, tableau):
        pass


class TriBulles(Tri):

    def trier(self, tableau):
        pass


class TriRapide(Tri):

    def trier(self, tableau):
        pass


tris = [TriInsertion(), TriSelection(), TriFusion(), TriBulles(), TriRapide()]

for tri in tris:
    devs = Developeur.generate_devs(15)
    out = ''
    for dev in devs:
        out += repr(dev)
    print('Initial: [ ' + out + ' ]')
    print('Tri' + str(tri.__class__))
    tri.trier(devs)
    out = ''
    for dev in devs:
        out += repr(dev)
    print('Resultat: [ ' + out + ' ]\n')








