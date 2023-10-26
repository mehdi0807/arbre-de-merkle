### Pour exécuter le script sur terminal utilisez : python verification.py element

from sha_256 import *
from construction import *
def verification(arbre, element):
    hashes = []
    if not isinstance(arbre.gauche, arbre_merkle):   # Si les fils sont des feuilles
        hashes.append(arbre.hash_)
        return element in arbre.droit or element in arbre.gauche, hashes

    resultat_droit, hashes_droit = verification(arbre.droit, element)
    resultat_gauche, hashes_gauche = verification(arbre.gauche, element)

    hashes.extend(hashes_droit)
    hashes.extend(hashes_gauche)

    return resultat_droit or resultat_gauche, hashes

def check(arbre, element):
    resultat, hashes = verification(arbre, element)
    if resultat:  # Si l'élément fait partie des feuilles de l'arbre on prend les hashes du chemain parcouru
        return resultat, hashes
    else:
        return resultat

if __name__ == "__main__":
    import sys
    element = sys.argv[1]
    arbre = construction(['Mehdi', 'Amor Ouahmed', 'etudiant', 'Data Science', 'AI', 'ENP', 'Ingénieur'])
    resultat = check(arbre, element)
    if resultat == False:
        print(resultat, f". L'élément : '{element}' ne fait pas partie des feuilles de cet arbre")
    else:
        print(resultat[0], f". L'élément : '{element}' fait partie des feuilles de cet arbre")
        print("Il est présent dans ces hashes:", resultat[1])
        
### ©Mehdi AMOR OUAHMED, Oct 2023