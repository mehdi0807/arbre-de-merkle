from sha_256 import *
from construction import *
def verification(tree, element):
    hashes = []
    if not isinstance(tree.gauche, tree_merkle):   # If the sons are nodes
        hashes.append(tree.hash_)
        return element in tree.droit or element in tree.gauche, hashes

    resultat_droit, hashes_droit = verification(tree.droit, element)
    resultat_gauche, hashes_gauche = verification(tree.gauche, element)

    hashes.extend(hashes_droit)
    hashes.extend(hashes_gauche)

    return resultat_droit or resultat_gauche, hashes

def check(tree, element):
    resultat, hashes = verification(tree, element)
    if resultat:  # if the element is one of the tree's node we take also the hashes where it's present
        return resultat, hashes
    else:
        return resultat
        
### ©Mehdi AMOR OUAHMED, Oct 2023