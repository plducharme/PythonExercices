#
Dans listechainee.py
- Ajouter la Docstrings pour la classe
- Implémenter Node.\__repr__(self)
- Implémenter ListeChainee.\__iter__(self) pour parcourir la liste avec un itérateur
  + Ajouter la gestion d'exceptions
- Compléter le constructeur de ListeChainee pour l'initialiser avec les noeuds passés en argument
- Implémenter les méthodes suivantes dans ListeChainee (en incluant la gestion d'exceptions, docstrings):
  + ajout_fin(self, data): permet d'ajouter à la fin
  + ajout_apres(self, cible_data, data): permet d'ajouter data après le cible_data
  + ajout_avant(self, cible_data, data)
  + enlever_noeud(self, cible_data)
#
Dans listedoublechainee.py
- Ajouter la Docstrings pour la classe
- Implémenter Node.\__repr__(self)
- Implémenter ListeDoubleChainee.\__iter__(self) pour parcourir la liste avec un itérateur
  + Ajouter la gestion d'exceptions
- Compléter le constructeur de ListeChainee pour l'initialiser avec les noeuds passés en argument
- Implémenter les méthodes suivantes dans ListeDoubleChainee (en incluant la gestion d'exceptions, docstrings):
  + ajout_fin(self, data): permet d'ajouter à la fin
  + ajout_apres(self, cible_data, data): permet d'ajouter data après le cible_data
  + ajout_avant(self, cible_data, data)
  + enlever_noeud(self, cible_data)
#
Sans avoir vu les tris:
- Essayer d'implémenter une fonction tri(self) qui permet de trier les éléments de la liste
  + Le faire pour ListeChainee et ListDoubleChainee
- Implémenter une ListeChaineeCirculaire
  + Une liste dont le dernier élément réfère vers la "tete" au lieu de None
#
