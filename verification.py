from sha_256 import *
from construction import *
def verification(tree, element):
    hashes = []
    if not isinstance(tree.left, merkle_tree):   # If the sons are leaves
        hashes.append(tree.hash_)
        return element in tree.right or element in tree.left, hashes

    resultat_right, hashes_right = verification(tree.right, element)
    resultat_left, hashes_left = verification(tree.left, element)

    hashes.extend(hashes_right)
    hashes.extend(hashes_left)

    return resultat_right or resultat_left, hashes

def check(tree, element):
    resultat, hashes = verification(tree, element)
    if resultat:  # if the element is one of the tree's node we take also the hashes where it is present
        return resultat, hashes
    else:
        return resultat
        
### ©Mehdi AMOR OUAHMED, Oct 2023