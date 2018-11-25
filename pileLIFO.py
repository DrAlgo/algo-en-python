#coding: utf-8
TAILLE_MAX_PILE = 100

class PileLIFO:
        """une pile implementee
        dans un tableau de taille fixe TAILLE_MAX_PILE"""

        def __init__(self):
                self.sommet = -1            # pile vide
                self.donnees = [None] * TAILLE_MAX_PILE

        def estVide(self):
                """indique si la pile est vide"""
                return self.sommet == -1


        def estPleine(self):
                """indique si la pile est pleine"""
                return self.sommet == TAILLE_MAX_PILE -1


        def empiler(self, element):
                """ajoute l'element au sommet de la pile"""

                if self.estPleine():
                        raise Exception("erreur : la pile est pleine !")
                else:
                        self.sommet += 1
                        self.donnees[self.sommet] = element

        def depiler(self):
                """supprime l'element au sommet dela pile
                et le renvoie"""

                if self.estVide():
                        raise Exception("erreur : la pile est vide !")
                else:
                        self.sommet -= 1
                        return self.donnees[self.sommet + 1]

        def __str__(self):
                """permet de faire un print"""
                return str(self.donnees[0:self.sommet + 1])

