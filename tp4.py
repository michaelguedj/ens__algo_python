# -*- coding: utf-8 -*-
"""
@author: Dr Michael GUEDJ

Algorithmique --
TP4 --
Boucles "Pour"
"""


# 1
def dix():
    for i in range(10):
        print(i)

        
# 2
def n_premiers_entiers(n):
    for i in range(n):
        print(i)
        
# 3
def n_premiers_entiers_carre(n):
    for i in range(n):
        print(i*i)
 
# 4
def n_premiers_entiers_pairs(n):
    for i in range(n):
        if i%2 == 0:
            print(i)
        
# 5
def n_premiers_entiers_impairs(n):
    for i in range(n):
        if i%2 == 1:
            print(i)
            
# 6
def _10_fois_coucou():
    for i in range(10):
        print("coucou")
        
# 7
def n_fois_coucou(n):
    for i in range(n):
        print("coucou")
        
# 8
def somme_n_premiers_entiers(n):
    res = 0
    for i in range(n):
        res += i
    return res

# 9
def somme_n_premiers_carres(n):
    res = 0
    for i in range(n):
        res += i*i
    return res

# 10
def somme_n_premiers_pairs(n):
    res = 0
    for i in range(n):
        if i%2 == 0:
            res += i
    return res

# 11
def somme_n_premiers_impairs(n):
    res = 0
    for i in range(n):
        if i%2 == 1:
            res += i
    return res

# 12
def somme_n_premiers_pairs_carre(n):
    res = 0
    for i in range(n):
        if i%2 == 0:
            res += i*i
    return res

# 13
def toto(n):
    res = 0
    for i in range(n):
        if i%3 == 0:
            res += i
    return res

# 14
def toto2(n, k):
    res = 0
    for i in range(n):
        if i%k == 0:
            res += i
    return res

# 15
def toto_bis(n):
    return toto2(n,3)


if __name__ == "__main__":

    print("exo 1:")
    dix()
    
    print("exo 2:")
    n_premiers_entiers(5)
    
    print("exo 3:")
    n_premiers_entiers_carre(5)
    
    print("exo 4:")
    n_premiers_entiers_pairs(10)
    
    print("exo 5:")
    n_premiers_entiers_impairs(10)
    
    print("exo 6:")
    _10_fois_coucou()
    
    print("exo 7:")
    n_fois_coucou(5)
    
    print("exo 8:", somme_n_premiers_entiers(5))    # 10
    
    print("exo 9:",  somme_n_premiers_carres(5))    # 30
    
    print("exo 10:",  somme_n_premiers_pairs(10))   # 20
    
    print("exo 11:",  somme_n_premiers_impairs(10)) # 25
    
    print("exo 12:",  somme_n_premiers_pairs_carre(5)) # 20
    
    print("exo 13:", toto(10))  # 18
    
    print("exo 14:", toto2(10, 3))  # 18
    
    print("exo 15:", toto_bis(10) == toto(10))  # True