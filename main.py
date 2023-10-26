### To use it try python main.py node1 node2 node3 ...

from construction import *
from verification import *

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script.py <list_of_leaves>")
        sys.exit(1)

    leaves = sys.argv[1:]
    tree = construction(leaves)
    print("Merkle's root:", tree.hash_)

    while True:
        element = input("Enter an element to check (or 'exit' to quit): ")
        
        if element == 'exit':
            break

        resultat = check(tree, element)
        if resultat == False:
            print(resultat, f". The element : '{element}' is not one of the tree's leaves")
        else:
            print(resultat[0], f". L'élément : '{element}' is one of the tree's leaves")
            print("It is present in these hashes:", resultat[1])


### ©Mehdi AMOR OUAHMED, Oct 2023