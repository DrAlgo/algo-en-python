#coding: utf-8
TAILLE_MAX_FILE = 100

class FileFIFO:
    """implementation d'une file FIFO dans un tableau
    de taille fixe TAILLE_MAX_FILE"""

    def __init__(self):
        self.entree = 0
        self.sortie = 0
        self.donnees = [None] * TAILLE_MAX_FILE


    def fileEstVide(self):
        """indique si la file est vide"""
        return self.sortie == self.entree


    def fileEstPleine(self):
        """indique si la file est pleine"""
        return (self.sortie == self.entree + 1) or\
            (self.sortie == 0 and self.entree == TAILLE_MAX_FILE - 1)


    def ajouter(self, element):
        if self.fileEstPleine():
            raise Exception("erreur : la file est pleine !")
        else:
            #insertion de l'element
            self.donnees[self.entree] = element
            #on augmente l'entree en bouclant
            self.entree += 1
            if self.entree == TAILLE_MAX_FILE:
                self.entree = 0


    def defiler(self):
        if self.fileEstVide():
            raise Exception("erreur : la pile est vide !")
        else:
            #on stocke l'element a renvoyer
            element = self.donnees[self.sortie]
            #on augmente la sortie circulairement
            self.sortie += 1
            if self.sortie == TAILLE_MAX_FILE:
                self.sortie = 0
            return element

    def longueur(self):
        """renvoie le nb d'éléments dans la file"""
        if self.sortie <= self.entree:
            return self.entree - self.sortie
        else:
            return self.entree + TAILLE_MAX_FILE - self.sortie


    def __str__(self):
        """permet d'afficher avec print les elements de la file"""

        if self.sortie < self.entree:
            return str(self.donnees[self.sortie : self.entree])
        else:
            return str(self.donnees[self.sortie:] +\
                self.donnees[:self.entree])

