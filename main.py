### Un essai de mes fonctions

from construction import *
from verification import *
feuilles = ['Mehdi', 'Amor Ouahmed', 'etudiant', 'Data Science', 'AI', 'ENP', 'Ingénieur']
arbre = construction(feuilles)
print(f'Racine de Merkle des feuilles : {feuilles}:\n', arbre.hash_)
        
print(check(arbre, 'Mehdi'))
print(check(arbre, 'Meh'))
print(check(arbre, 'mehdi'))


### ©Mehdi AMOR OUAHMED, Oct 2023