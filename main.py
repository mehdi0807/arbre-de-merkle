### Un essai de mes fonctions

from construction import *
from verification import *

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script.py <list_of_leaves>")
        sys.exit(1)

    feuilles = sys.argv[1:]
    arbre = construction(feuilles)
    print("Racine de Merkle:", arbre.hash_)

    while True:
        element = input("Enter an element to check (or 'exit' to quit): ")
        
        if element == 'exit':
            break

        resultat = check(arbre, element)
        if resultat == False:
            print(resultat, f". L'élément : '{element}' ne fait pas partie des feuilles de cet arbre")
        else:
            print(resultat[0], f". L'élément : '{element}' fait partie des feuilles de cet arbre")
            print("Il est présent dans ces hashes:", resultat[1])


### ©Mehdi AMOR OUAHMED, Oct 2023