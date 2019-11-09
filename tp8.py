# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP8 --
Mots
"""


# 2
def concatener(lst):
    res = lst[0]
    i = 1
    while i < len(lst):
        res += " "+lst[i]
        i +=1
    return res

# 3
def est_present(m, c):
    for x in m:
        if x == c:
            return True
    return False
#ou
def est_present_bis(m, c):
    return c in m

# 4
def afficher(m):
    for c in m:
        print(c)

# 5
def nb_occurrences(m, c):
    res = 0
    for x in m:
        if x == c:
            res +=1
    print(res)

# 6
def mot_present(m1, m2):
    return m1 in m2
    

if __name__ == "__main__":
    
    print("exo 2:", \
          concatener(["a", "aa", "aaa", "aaaa"]))
    
    print("exo 3:", est_present("toto", "o"))
    
    print("exo 4:")
    afficher("toto")
    
    print("exo 5:")
    nb_occurrences("abaab", "a")
    
    print("exo 6:", mot_present("toto", "Bonjour toto"))