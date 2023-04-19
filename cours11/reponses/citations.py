# Lire le fichier ligne par ligne
# Creer une classe Citation pour representer une citation (citation, auteur)
# Pour chaque ligne dans citations.txt, creer un objet Citation
# Creer une methode statique qui va retourner une citation au hasard a partir d'une liste d'objets Citation
# Creer une methode statique pour trier les citations par ordre alphabetique
#   (sans utiliser sort, votre choix d'algo)
# Creer une methode statique pour trier les citations par ordre alphabetique de l'auteur
#   (sans utiliser sort, votre choix d'algo)
# Creer une methode pour ecrire chaque citation dans un fichier texte dans le repertoire "tmp"
#   Le nom de fichier doit etre le nom de l'auteur, si existant, ajoute la citation au fichier
# Creer une methode statique pour lire tous les fichiers du repertoire tmp et
#   recreer le fichier original sous le nom 'citations_nouveau.txt'
# Comparer les fichiers
import os
import random


class Citation:

    def __init__(self, citation, auteur):
        self.__citation = citation
        self.__auteur = auteur

    @property
    def citation(self):
        return self.__citation

    @property
    def auteur(self):
        return self.__auteur

    def to_file(self):
        with open(f'./tmp/{self.__auteur}.txt', 'a') as writer:
            writer.write(f'{self.__citation}\n')

    def __repr__(self):
        return f'Citation: {self.__citation}~{self.__auteur}'

    @staticmethod
    def from_file(filename):
        with open(filename, 'r') as reader:
            liste = []
            for ligne in reader:
                obj = ligne.split('~')
                citation = obj[0]
                # On enleve les espaces devant le nom de l'auteur si existant
                auteur = obj[1].lstrip().rstrip('\n')
                liste.append(Citation(citation, auteur))
            return liste

    @staticmethod
    def citation_du_jour(citations):
        citation = citations[random.randint(0, len(citations))]
        return f"{citation.citation} --- {citation.auteur}"

    @staticmethod
    def trier_citations(citations):
        for i in range(0, len(citations)):

            minimum = citations[i].citation
            min_index = i

            # itérer sur le reste du tableau pour chercher la plus petite valeur
            for j in range(i, len(citations)):

                if citations[j].citation < minimum:
                    minimum = citations[j].citation
                    min_index = j

            # échanger l'élément à l'index i avec le minimum trouvé
            temp = citations[i]
            citations[i] = citations[min_index]
            citations[min_index] = temp

    @staticmethod
    def trier_auteurs(citations):
        for i in range(1, len(citations)):
            courant = citations[i]
            p = i
            while p > 0 and citations[p - 1].auteur > courant.auteur:
                citations[p] = citations[p - 1]
                p = p - 1
            citations[p] = courant

    @staticmethod
    def to_original_file(filepath_src, filename):

        with open(filename, 'w') as writer:
            for file in os.listdir(filepath_src):
                with open(f'./tmp/{file}', 'r') as reader:
                    filename = file.removesuffix('.txt')
                    for line in reader:
                        line = line.rstrip('\n')
                        writer.write(f'{line}~{filename}\n')

    @staticmethod
    def clean_tmp():
        for file in os.listdir('./tmp'):
            os.remove('./tmp/'+file)

    @staticmethod
    def afficher_liste(citations):
        for citation in citations:
            print(citation)


liste = Citation.from_file('citations.txt')

print(Citation.citation_du_jour(liste))

Citation.trier_citations(liste)
Citation.afficher_liste(liste)
print('-------------------------------------------')
Citation.trier_auteurs(liste)
Citation.afficher_liste(liste)
print('-------------------------------------------')

Citation.clean_tmp()
for citation in liste:
    citation.to_file()

Citation.to_original_file('./tmp', 'citations_nouveau.txt')





