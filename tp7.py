# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP7 --
Listes d'entiers
"""


# 1
def est_vide(lst):
    return len(lst) == 0

def est_vide_bis(lst):
    return lst == []

# 2
def maximum(lst):
    n = len(lst)
    res = lst[0]
    for i in range(n):
        if lst[i] > res:
            res = lst[i]
    return res

# 3
def somme(lst):
    n = len(lst)
    res = 0
    for i in range(n):
        res += lst[i]
    return res

# 4
def moyenne(lst):
    return somme(lst)/len(lst)

# 5
def tous_egaux(lst):
    n = len(lst)
    x = lst[0]
    for i in range(n):
        if lst[i] != x:
            return False
    return True

# 6
def produit_scalaire(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += v1[i]*v2[i]
    return res

# 7
def egaux(v1, v2):
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            return False
    return True

# 8
def est_triee(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

if __name__ == "__main__":
    
    print("exo 1",  est_vide( [] ) )
    print("exo 2",  maximum([1, 3, 2]))
    print("exo 3",  somme([1, 3, 2]))
    print("exo 4",  moyenne([1, 3, 2]))
    print("exo 5",  tous_egaux([3, 3, 3]))
    print("exo 6",  produit_scalaire([3, 3, 3], [1, 2, 1]))
    print("exo 7",  egaux([3, 3, 3], [1, 2, 1]))
    print("exo 8",  est_triee([1, 2, 3, 3]))