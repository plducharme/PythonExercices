# Créer une fonction qui génère une séquence infinie sans causer de boucle infinie
# yield permet de retourner une valeur pour une itération, permettant de transformer une fonction en générateur
def sequence_infini():
    num = 0
    while True:
        yield num
        num += 1


# utiliser un generateur pour generer des nombres
gen = sequence_infini()
for i in range(0, 10):
    print(next(gen))



