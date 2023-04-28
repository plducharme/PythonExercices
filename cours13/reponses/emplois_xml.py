from xml.dom import minidom

class OffreEmploi:

    def __init__(self, emploi_id, date_debut_postuler, date_limite_postuler, titre_emploi, nom_orgnisation, emplacement,
                 statut_emploi, secteur_emploi, quart_de_travail, breve_description, exigences):
        self.__emploi_id = emploi_id
        self.__date_debut_postuler = date_debut_postuler
        self.__date_limite_postuler = date_limite_postuler
        self.__titre_emploi = titre_emploi
        self.__nom_orgnisation = nom_orgnisation
        self.__emplacement = emplacement
        self.__exigences = exigences
        self.__breve_description = breve_description
        self.__quart_de_travail = quart_de_travail
        self.__secteur_emploi = secteur_emploi
        self.__statut_emploi = statut_emploi

    def __repr__(self):
        return f'emploi_id: {self.__emploi_id} date_debut_postuler: {self.__date_debut_postuler}' +\
            f' date_limite_postuler: {self.__date_limite_postuler} titre_emploi: {self.__titre_emploi}' +\
            f' nom_orgnisation: {self.__nom_orgnisation} emplacementr: {self.__emplacement}' +\
            f' exigences: {self.__exigences}  breve_description: {self.__breve_description}' +\
            f' quart_de_travail: {self.__quart_de_travail} secteur_emploi: {self.__secteur_emploi}' +\
            f' statut_emploi: {self.__statut_emploi}'

    # Retourne la liste de tous les objets OffreEmploi dans le fichier XML passé en paramètre
    @staticmethod
    def from_xml(filename):
        # Parse le fichier pour obtenir un Document, le document contient des éléments
        document = minidom.parse(filename)
        # On va chercher la liste de toutes les balises (Elements) OffreEmploi
        # getElementsByTagName("OffresEmploi") va chercher toutes les balises (ELement) se nommant "OffresEmploi"
        offres_elems = document.getElementsByTagName("OffresEmploi")
        # Liste des objets OffreEmploi qui vont être créés
        offres_obj = []
        # Pour chaque élément, on va créer l'offre à partir des sous-éléments Comme ce sont des éléments uniques,
        # ils sont situés à l'index 0 de ce qui est retourné par getElementsByTagName()
        for offre in offres_elems:
            emploi_id = offre.getElementsByTagName('Emploi_ID')[0].firstChild.data
            date_debut_postuler_elem = offre.getElementsByTagName('Date_debut_postuler')[0]
            date_debut_postuler = OffreEmploi.get_text_from_element(date_debut_postuler_elem)
            date_limite_elem = offre.getElementsByTagName('Date_limite_postuler')[0]
            date_limite_postuler = OffreEmploi.get_text_from_element(date_limite_elem)
            titre_emploi_elem = offre.getElementsByTagName('Titre_emploi')[0]
            titre_emploi = OffreEmploi.get_text_from_element(titre_emploi_elem)
            nom_orgnisation = offre.getElementsByTagName('Nom_orgnisation')[0].firstChild.data
            emplacement = offre.getElementsByTagName('Emplacement')[0].firstChild.data
            statut_emploi = offre.getElementsByTagName('Statut_emploi')[0].firstChild.data
            secteur_emploi = offre.getElementsByTagName('Secteur_emploi')[0].firstChild.data
            quart_elem = offre.getElementsByTagName('Quart_de_travail')[0]
            quart_de_travail = OffreEmploi.get_text_from_element(quart_elem)
            breve_description_elem = offre.getElementsByTagName('Breve_description')[0]
            breve_description = OffreEmploi.get_text_from_element(breve_description_elem)
            exigences_elem = offre.getElementsByTagName('Exigences')[0]
            exigences = OffreEmploi.get_text_from_element(exigences_elem)
            offre_emploi = OffreEmploi(emploi_id, date_debut_postuler, date_limite_postuler, titre_emploi,
                                       nom_orgnisation, emplacement, statut_emploi, secteur_emploi, quart_de_travail,
                                       breve_description, exigences)
            offres_obj.append(offre_emploi)
        return offres_obj

    @staticmethod
    def get_text_from_element(element):
        # Si vous regarder la structure d'un élément, le texte se situe dans le premier enfant (firstChild) dans
        # l'attribut data
        if element.firstChild is not None:
            return element.firstChild.data
        else:
            return None


# Exemple pour créer les objets OffreEmploi à partir du fichier xml
offres_emploi = OffreEmploi.from_xml('offre-emploi.xml')
for offre_obj in offres_emploi:
    print(offre_obj)


# Exemple pour aller chercher un attribut dans un élément
xml_str = '<test id="123456"></test>'
doc = minidom.parseString(xml_str)
test_elem = doc.getElementsByTagName('test')[0]
test_id = test_elem.getAttribute('id')
print(test_id)

# Le seul enfant du document est la balise racine. Les sous-éléments d'un Element sont dans une liste "childNodes"
xml_str = '<racine><enfant nom="Aurelie"></enfant><enfant nom="Mathis"></enfant></racine>'
doc = minidom.parseString(xml_str)
racine_elem = doc.firstChild
enfants_elems = racine_elem.childNodes
for elem in enfants_elems:
    print(elem.getAttribute("nom"))





