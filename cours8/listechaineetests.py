from listechainee import ListeChainee, Noeud

#noeuds = [Noeud(x) for x in [3, 7, 1, 2, 8, 9, 5, 14, 23, 12, 25, 45, 4]]
noeuds = [Noeud(x) for x in [3, 7, 1]]


lc = ListeChainee(noeuds)
print(lc)
try:
    lc.enlever_noeud(3)
    print(lc)
except Exception as e:
    print(e)

try:
    lc.enlever_noeud(42)
    print(lc)
except Exception as e:
    print(e)

try:
    lc.ajout_fin(42)
    print(lc)
except Exception as e:
    print(e)

try:
    lc2 = ListeChainee()
    lc2.ajout_fin(42)
    print(lc2)
except Exception as e:
    print(e)

try:
    lc.ajout_apres(14, 8)
    print(lc)
except Exception as e:
    print(e)

try:
    lc.ajout_avant(7, 3)
    print(lc)
except Exception as e:
    print(e)
