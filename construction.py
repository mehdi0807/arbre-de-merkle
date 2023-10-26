from sha_256 import *
class merkle_tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        if isinstance(left, merkle_tree):  # If the nopdes are not leaves, they are trees and we take their roots
            left = left.hash_
            right = right.hash_
        else:  # If the nodes are leaves we take their hashes
            left = sha_256(left)
            right = sha_256(right)
        a = left
        b = right
        hash_ab = sha_256(a+b)
        self.hash_ = hash_ab

def construction(list_):
    l = len(list_)
    if (int(l / 2) == l / 2):
        parents = []
        for i in range(int(l / 2)):
            parents.append(merkle_tree(list_[2 * i], list_[2 * i + 1]))
    else:  # If odd
        parents = []
        for i in range(int(l / 2)):
            parents.append(merkle_tree(list_[2 * i], list_[2 * i + 1]))
        parents.append(merkle_tree(list_[-1], list_[-1]))
    if len(parents) == 1:
        return parents[0]
    else:
        return construction(parents)


### ©Mehdi AMOR OUAHMED, Oct 2023