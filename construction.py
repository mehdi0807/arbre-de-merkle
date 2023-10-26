from sha_256 import *
class arbre_merkle:
    def __init__(self, gauche, droit):
        self.gauche = gauche
        self.droit = droit
        if isinstance(gauche, arbre_merkle):  # Si les noeud ne sont pas des feuilles, ils sont des arbres et on prends leurs racines
            gauche = gauche.hash_
            droit = droit.hash_
        else:  # Si le noeuds sont des feuilles on prend leurs hashes
            gauche = sha_256(gauche)
            droit = sha_256(droit)
        a = gauche
        b = droit
        hash_ab = sha_256(a+b)
        self.hash_ = hash_ab

def construction(liste):
    l = len(liste)
    if (int(l / 2) == l / 2):  # If even
        parents = []
        for i in range(int(l / 2)):
            parents.append(arbre_merkle(liste[2 * i], liste[2 * i + 1]))
    else:  # If odd
        parents = []
        for i in range(int(l / 2)):
            parents.append(arbre_merkle(liste[2 * i], liste[2 * i + 1]))
        parents.append(arbre_merkle(liste[-1], liste[-1]))
    if len(parents) == 1:
        return parents[0]
    else:
        return construction(parents)


### ©Mehdi AMOR OUAHMED, Oct 2023